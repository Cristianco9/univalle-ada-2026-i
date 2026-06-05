"""
complexity_model_service.py
---------------------------
MLP desde cero (NumPy puro) para clasificar complejidad algorítmica.

Arquitectura: input(12) → hidden1(64, ReLU) → hidden2(32, ReLU) → output(7, Softmax)
Clases: O(1), O(log n), O(n), O(n log n), O(n²), O(n³), O(2^n)

Mejoras v2:
  - 500 épocas máximo
  - Early stopping con patience=50
  - Learning rate decay cada 100 épocas
  - Momentum en SGD (acelera convergencia)
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures.hash_table import HashTable
from algorithms.hard_mining import get_hard_examples
from complexity.feature_extractor import extract_features, FEATURE_SIZE
from data.complexity_dataset import SAMPLES, CLASS_NAMES

# ── Hiperparámetros ───────────────────────────────────────────────────────────
NUM_CLASSES    = 7
HIDDEN1        = 64
HIDDEN2        = 32
LEARNING_RATE  = 0.01
LR_DECAY       = 0.5
LR_DECAY_EVERY = 150
MOMENTUM       = 0.9
EPOCHS         = 500
PATIENCE       = 80
BATCH_SIZE     = 8
CLIP_VALUE     = 1.0
NOISE_STD      = 0.02


def relu(x):
    return np.maximum(0, x)

def softmax(x):
    e = np.exp(x - np.max(x))
    return e / e.sum()

def clip_grad(g, clip=CLIP_VALUE):
    norm = np.linalg.norm(g)
    if norm > clip:
        return g * clip / norm
    return g


class ComplexityModelService:

    def __init__(self):
        self.W1 = self.b1 = None
        self.W2 = self.b2 = None
        self.W3 = self.b3 = None
        self.vW1 = self.vb1 = None
        self.vW2 = self.vb2 = None
        self.vW3 = self.vb3 = None
        self.is_trained    = False
        self.accuracy      = 0.0
        self.metrics       = HashTable()
        self.hard_examples = []
        self.epochs_run    = 0

    def _build_balanced_dataset(self, seed=42):
        np.random.seed(seed)
        X_raw = np.array([extract_features(c) for c, _ in SAMPLES])
        y_raw = np.array([label for _, label in SAMPLES])

        from collections import Counter
        max_count = max(Counter(y_raw.tolist()).values())
        X_list, y_list = list(X_raw), list(y_raw)

        for cls in range(NUM_CLASSES):
            indices = np.where(y_raw == cls)[0]
            for _ in range(max_count - len(indices)):
                idx = np.random.choice(indices)
                noise = np.random.normal(0, NOISE_STD, FEATURE_SIZE)
                X_list.append(np.clip(X_raw[idx] + noise, 0, 1))
                y_list.append(cls)

        X, y = np.array(X_list), np.array(y_list)
        perm  = np.random.permutation(len(X))
        split = int(len(X) * 0.8)
        return X[perm[:split]], X[perm[split:]], y[perm[:split]], y[perm[split:]]

    def _forward(self, x):
        self._h1_in  = x @ self.W1 + self.b1
        self._h1_out = relu(self._h1_in)
        self._h2_in  = self._h1_out @ self.W2 + self.b2
        self._h2_out = relu(self._h2_in)
        self._o_in   = self._h2_out @ self.W3 + self.b3
        self._o_out  = softmax(self._o_in)
        return self._o_out

    def _backward(self, x, y_enc, lr):
        d3 = clip_grad(self._o_out - y_enc)
        self.vW3 = MOMENTUM * self.vW3 - lr * np.outer(self._h2_out, d3)
        self.vb3 = MOMENTUM * self.vb3 - lr * d3
        self.W3 += self.vW3
        self.b3 += self.vb3

        d2 = clip_grad((d3 @ self.W3.T) * (self._h2_in > 0))
        self.vW2 = MOMENTUM * self.vW2 - lr * np.outer(self._h1_out, d2)
        self.vb2 = MOMENTUM * self.vb2 - lr * d2
        self.W2 += self.vW2
        self.b2 += self.vb2

        d1 = clip_grad((d2 @ self.W2.T) * (self._h1_in > 0))
        self.vW1 = MOMENTUM * self.vW1 - lr * np.outer(x, d1)
        self.vb1 = MOMENTUM * self.vb1 - lr * d1
        self.W1 += self.vW1
        self.b1 += self.vb1

    def train_model(self) -> dict:
        X_train, X_test, y_train, y_test = self._build_balanced_dataset()

        Y_train = np.zeros((len(y_train), NUM_CLASSES))
        Y_train[np.arange(len(y_train)), y_train] = 1

        np.random.seed(42)
        self.W1 = np.random.randn(FEATURE_SIZE, HIDDEN1) * np.sqrt(2/FEATURE_SIZE)
        self.b1 = np.zeros(HIDDEN1)
        self.W2 = np.random.randn(HIDDEN1,      HIDDEN2) * np.sqrt(2/HIDDEN1)
        self.b2 = np.zeros(HIDDEN2)
        self.W3 = np.random.randn(HIDDEN2,   NUM_CLASSES) * np.sqrt(2/HIDDEN2)
        self.b3 = np.zeros(NUM_CLASSES)

        self.vW1 = np.zeros_like(self.W1); self.vb1 = np.zeros_like(self.b1)
        self.vW2 = np.zeros_like(self.W2); self.vb2 = np.zeros_like(self.b2)
        self.vW3 = np.zeros_like(self.W3); self.vb3 = np.zeros_like(self.b3)

        best_acc, best_weights, patience_ctr = 0.0, None, 0
        losses_all = []
        lr = LEARNING_RATE

        for epoch in range(EPOCHS):
            if epoch > 0 and epoch % LR_DECAY_EVERY == 0:
                lr *= LR_DECAY
                print(f"  📉 LR decay → {lr:.5f}")

            perm      = np.random.permutation(len(X_train))
            correct   = 0
            ep_losses = []

            from data_structures.queue import Queue
            batch_queue = Queue()
            for start in range(0, len(X_train), BATCH_SIZE):
                batch_queue.enqueue(perm[start:start + BATCH_SIZE])

            while not batch_queue.is_empty():
                for i in batch_queue.dequeue():
                    output = self._forward(X_train[i])
                    if np.argmax(output) == y_train[i]:
                        correct += 1
                    loss = float(np.mean((output - Y_train[i]) ** 2))
                    ep_losses.append(loss)
                    losses_all.append(loss)
                    self._backward(X_train[i], Y_train[i], lr)

            acc      = correct / len(X_train) * 100
            avg_loss = float(np.mean(ep_losses))

            self.metrics.set(f"epoch_{epoch+1}_acc",  round(acc, 2))
            self.metrics.set(f"epoch_{epoch+1}_loss", round(avg_loss, 6))

            if acc > best_acc:
                best_acc, patience_ctr = acc, 0
                best_weights = (
                    self.W1.copy(), self.b1.copy(),
                    self.W2.copy(), self.b2.copy(),
                    self.W3.copy(), self.b3.copy(),
                )
            else:
                patience_ctr += 1

            if (epoch + 1) % 50 == 0:
                print(
                    f"Epoch {epoch+1:3d}/{EPOCHS} | "
                    f"Acc: {acc:.1f}% | "
                    f"Loss: {avg_loss:.4f} | "
                    f"Best: {best_acc:.1f}% | "
                    f"LR: {lr:.5f} | "
                    f"Patience: {patience_ctr}/{PATIENCE}"
                )

            if patience_ctr >= PATIENCE:
                print(f"\n⏹ Early stopping en época {epoch+1}")
                break

        self.epochs_run = epoch + 1
        self.W1, self.b1, self.W2, self.b2, self.W3, self.b3 = best_weights
        self.hard_examples = get_hard_examples(losses_all, k=5)

        correct = sum(
            1 for i in range(len(X_test))
            if int(np.argmax(self._forward(X_test[i]))) == y_test[i]
        )
        self.accuracy   = correct / len(X_test) * 100
        self.is_trained = True

        print(f"\n✅ Entrenamiento completo")
        print(f"   Épocas ejecutadas : {self.epochs_run}")
        print(f"   Best train acc    : {best_acc:.1f}%")
        print(f"   Test accuracy     : {self.accuracy:.1f}%")

        return {
            "status":         "trained",
            "train_samples":  len(X_train),
            "test_samples":   len(X_test),
            "epochs":         self.epochs_run,
            "best_train_acc": round(best_acc, 2),
            "test_accuracy":  round(self.accuracy, 2),
        }

    def predict_complexity(self, code: str) -> dict:
        if not self.is_trained:
            raise RuntimeError("Modelo no entrenado. Usa /train_complexity primero.")

        features      = extract_features(code)
        probabilities = self._forward(features)
        pred_class    = int(np.argmax(probabilities))
        confidence    = float(probabilities[pred_class])

        top3_idx = np.argsort(probabilities)[::-1][:3]
        top3 = [
            {
                "complexity":  CLASS_NAMES[int(i)],
                "probability": round(float(probabilities[i]), 4),
            }
            for i in top3_idx
        ]

        return {
            "complexity": CLASS_NAMES[pred_class],
            "confidence": round(confidence, 4),
            "top3":       top3,
        }

    def get_training_metrics(self) -> dict:
        result = {}
        for epoch in range(1, self.epochs_run + 1):
            acc  = self.metrics.get(f"epoch_{epoch}_acc")
            loss = self.metrics.get(f"epoch_{epoch}_loss")
            if acc is not None:
                result[f"epoch_{epoch}"] = {"accuracy": acc, "loss": loss}
        return result

    def get_hard_examples(self) -> list:
        return self.hard_examples


complexity_model_service = ComplexityModelService()