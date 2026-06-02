import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures.hash_table import HashTable
from algorithms.hard_mining import get_hard_examples
from complexity.feature_extractor import extract_features, FEATURE_SIZE
from data.complexity_dataset import SAMPLES, CLASS_NAMES

# ── Hiperparámetros ───────────────────────────────────────────────────────────
NUM_CLASSES  = 7
HIDDEN1      = 64
HIDDEN2      = 32
LEARNING_RATE = 0.01
EPOCHS       = 200
BATCH_SIZE   = 8
CLIP_VALUE   = 1.0     # gradient clipping
NOISE_STD    = 0.01    # augmentation


# ── Activaciones ──────────────────────────────────────────────────────────────

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


# ── Servicio principal ────────────────────────────────────────────────────────

class ComplexityModelService:

    def __init__(self):
        # Pesos de la red (2 capas ocultas)
        self.W1 = None; self.b1 = None
        self.W2 = None; self.b2 = None
        self.W3 = None; self.b3 = None

        self.is_trained   = False
        self.accuracy     = 0.0
        self.metrics      = HashTable()
        self.hard_examples = []

    # ── Dataset ───────────────────────────────────────────────────────────────

    def _build_balanced_dataset(self, seed=42):
        np.random.seed(seed)
        X_raw = np.array([extract_features(c) for c, _ in SAMPLES])
        y_raw = np.array([label for _, label in SAMPLES])

        from collections import Counter
        counts = Counter(y_raw.tolist())
        max_count = max(counts.values())

        X_list = list(X_raw)
        y_list = list(y_raw)

        for cls in range(NUM_CLASSES):
            indices = np.where(y_raw == cls)[0]
            needed  = max_count - len(indices)
            for _ in range(needed):
                idx   = np.random.choice(indices)
                noise = np.random.normal(0, NOISE_STD, FEATURE_SIZE)
                X_list.append(np.clip(X_raw[idx] + noise, 0, 1))
                y_list.append(cls)

        X = np.array(X_list)
        y = np.array(y_list)

        # Shuffle y split 80/20
        perm    = np.random.permutation(len(X))
        split   = int(len(X) * 0.8)
        tr, te  = perm[:split], perm[split:]
        return X[tr], X[te], y[tr], y[te]

    # ── Forward ───────────────────────────────────────────────────────────────

    def _forward(self, x):
        self._h1_in  = x @ self.W1 + self.b1
        self._h1_out = relu(self._h1_in)
        self._h2_in  = self._h1_out @ self.W2 + self.b2
        self._h2_out = relu(self._h2_in)
        self._o_in   = self._h2_out @ self.W3 + self.b3
        self._o_out  = softmax(self._o_in)
        return self._o_out

    # ── Backprop ──────────────────────────────────────────────────────────────

    def _backward(self, x, y_enc, lr):
        d3 = clip_grad(self._o_out - y_enc)
        self.W3 -= lr * np.outer(self._h2_out, d3)
        self.b3 -= lr * d3

        d2 = clip_grad((d3 @ self.W3.T) * (self._h2_in > 0))
        self.W2 -= lr * np.outer(self._h1_out, d2)
        self.b2 -= lr * d2

        d1 = clip_grad((d2 @ self.W2.T) * (self._h1_in > 0))
        self.W1 -= lr * np.outer(x, d1)
        self.b1 -= lr * d1

    # ── Entrenamiento ─────────────────────────────────────────────────────────

    def train_model(self) -> dict:
        X_train, X_test, y_train, y_test = self._build_balanced_dataset()

        # One-hot
        Y_train = np.zeros((len(y_train), NUM_CLASSES))
        Y_train[np.arange(len(y_train)), y_train] = 1

        # Inicializar pesos (He initialization)
        np.random.seed(42)
        self.W1 = np.random.randn(FEATURE_SIZE, HIDDEN1) * np.sqrt(2/FEATURE_SIZE)
        self.b1 = np.zeros(HIDDEN1)
        self.W2 = np.random.randn(HIDDEN1,     HIDDEN2) * np.sqrt(2/HIDDEN1)
        self.b2 = np.zeros(HIDDEN2)
        self.W3 = np.random.randn(HIDDEN2,  NUM_CLASSES) * np.sqrt(2/HIDDEN2)
        self.b3 = np.zeros(NUM_CLASSES)

        # Early stopping
        best_acc = 0.0
        best_weights = None
        losses_all = []

        for epoch in range(EPOCHS):
            perm    = np.random.permutation(len(X_train))
            correct = 0
            ep_losses = []

            # ── Batch SGD con cola de lotes (RA3) ────────────────────────────
            from data_structures.queue import Queue
            batch_queue = Queue()
            for start in range(0, len(X_train), BATCH_SIZE):
                batch_queue.enqueue(perm[start:start + BATCH_SIZE])

            while not batch_queue.is_empty():
                batch_idx = batch_queue.dequeue()
                for i in batch_idx:
                    output = self._forward(X_train[i])
                    if np.argmax(output) == y_train[i]:
                        correct += 1
                    loss = float(np.mean((output - Y_train[i]) ** 2))
                    ep_losses.append(loss)
                    losses_all.append(loss)
                    self._backward(X_train[i], Y_train[i], LEARNING_RATE)

            acc      = correct / len(X_train) * 100
            avg_loss = float(np.mean(ep_losses))

            # Guardar en HashTable (RA3)
            self.metrics.set(f"epoch_{epoch+1}_acc",  round(acc, 2))
            self.metrics.set(f"epoch_{epoch+1}_loss", round(avg_loss, 6))

            # Early stopping
            if acc > best_acc:
                best_acc = acc
                best_weights = (
                    self.W1.copy(), self.b1.copy(),
                    self.W2.copy(), self.b2.copy(),
                    self.W3.copy(), self.b3.copy(),
                )

            if (epoch + 1) % 25 == 0:
                print(
                    f"Epoch {epoch+1:3d}/{EPOCHS} | "
                    f"Acc: {acc:.1f}% | "
                    f"Loss: {avg_loss:.4f} | "
                    f"Best: {best_acc:.1f}%"
                )

        # Restaurar mejor modelo
        self.W1, self.b1, self.W2, self.b2, self.W3, self.b3 = best_weights

        # Hard mining con heap (RA2)
        self.hard_examples = get_hard_examples(losses_all, k=5)

        # Evaluación en test
        correct = sum(
            1 for i in range(len(X_test))
            if int(np.argmax(self._forward(X_test[i]))) == y_test[i]
        )
        self.accuracy   = correct / len(X_test) * 100
        self.is_trained = True

        print(f"\n✅ Entrenamiento completo")
        print(f"   Train samples : {len(X_train)}")
        print(f"   Test  samples : {len(X_test)}")
        print(f"   Test accuracy : {self.accuracy:.1f}%")

        return {
            "status":         "trained",
            "train_samples":  len(X_train),
            "test_samples":   len(X_test),
            "epochs":         EPOCHS,
            "test_accuracy":  round(self.accuracy, 2),
            "best_train_acc": round(best_acc, 2),
        }

    # ── Predicción ────────────────────────────────────────────────────────────

    def predict_complexity(self, code: str) -> dict:
        if not self.is_trained:
            raise RuntimeError("Modelo no entrenado. Llama /train_complexity primero.")

        features     = extract_features(code)
        probabilities = self._forward(features)
        pred_class   = int(np.argmax(probabilities))
        confidence   = float(probabilities[pred_class])

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

    # ── Métricas ──────────────────────────────────────────────────────────────

    def get_training_metrics(self) -> dict:
        result = {}
        for epoch in range(1, EPOCHS + 1):
            acc  = self.metrics.get(f"epoch_{epoch}_acc")
            loss = self.metrics.get(f"epoch_{epoch}_loss")
            if acc is not None:
                result[f"epoch_{epoch}"] = {"accuracy": acc, "loss": loss}
        return result

    def get_hard_examples(self) -> list:
        return self.hard_examples


# Instancia global
complexity_model_service = ComplexityModelService()


if __name__ == "__main__":
    print("=" * 55)
    print("  MLP — Clasificador de Complejidad Algorítmica")
    print(f"  Arquitectura: {FEATURE_SIZE} → {HIDDEN1} → {HIDDEN2} → {NUM_CLASSES}")
    print(f"  Dataset: {len(SAMPLES)} snippets, {NUM_CLASSES} clases")
    print("=" * 55)

    result = complexity_model_service.train_model()

    print("\nPruebas de predicción:")
    tests = [
        ("def get(arr): return arr[0]",                                         "O(1)"),
        ("for i in range(n):\n  for j in range(n):\n    pass",                 "O(n²)"),
        ("def fib(n):\n  if n<=1: return n\n  return fib(n-1)+fib(n-2)",       "O(2^n)"),
        ("def bs(arr,t):\n  lo,hi=0,len(arr)-1\n  while lo<=hi:\n    mid=(lo+hi)//2\n    if arr[mid]==t: return mid\n    elif arr[mid]<t: lo=mid+1\n    else: hi=mid-1\n  return -1", "O(log n)"),
        ("sorted(arr)",                                                         "O(n log n)"),
        ("for i in range(n):\n  for j in range(n):\n    for k in range(n):\n    pass", "O(n³)"),
        ("for x in arr:\n  total += x",                                        "O(n)"),
    ]
    correct = 0
    for code, expected in tests:
        pred = complexity_model_service.predict_complexity(code)
        ok   = "✅" if pred["complexity"] == expected else "❌"
        if pred["complexity"] == expected:
            correct += 1
        print(
            f"  {ok} Esperado: {expected:10s} | "
            f"Predicho: {pred['complexity']:10s} | "
            f"Conf: {pred['confidence']:.1%}"
        )
    print(f"\nResultado: {correct}/{len(tests)} = {correct/len(tests):.0%}")