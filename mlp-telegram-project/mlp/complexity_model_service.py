"""
complexity_model_service.py
---------------------------

Implementación de un modelo de Red Neuronal Multicapa (MLP)
desarrollado desde cero utilizando NumPy para la clasificación
de complejidad algorítmica a partir de fragmentos de código fuente.

Este módulo constituye el núcleo de inteligencia artificial
del sistema y permite entrenar, evaluar y realizar predicciones
sobre la complejidad temporal de algoritmos utilizando técnicas
de aprendizaje supervisado.

Arquitectura de la Red:
-----------------------
                Input Layer
               (12 Features)
                      │
                      ▼
           Hidden Layer 1 (64)
                ReLU Activation
                      │
                      ▼
           Hidden Layer 2 (32)
                ReLU Activation
                      │
                      ▼
             Output Layer (7)
             Softmax Activation
                      │
                      ▼
     ┌─────────────────────────────┐
     │ O(1)                        │
     │ O(log n)                    │
     │ O(n)                        │
     │ O(n log n)                  │
     │ O(n²)                       │
     │ O(n³)                       │
     │ O(2ⁿ)                       │
     └─────────────────────────────┘

Características:
----------------
- Implementación de una red neuronal desde cero.
- Propagación hacia adelante (Forward Propagation).
- Retropropagación del error (Backpropagation).
- Función de activación ReLU.
- Función de salida Softmax.
- Optimización mediante SGD con Momentum.
- Gradient Clipping para evitar explosión de gradientes.
- Learning Rate Decay adaptativo.
- Early Stopping para prevenir sobreajuste.
- Balanceo automático del conjunto de entrenamiento.
- Evaluación mediante Accuracy.
- Predicción probabilística con Top-3 resultados.
- Identificación de ejemplos difíciles (Hard Mining).

Complejidades Clasificadas:
---------------------------
0 → O(1)
1 → O(log n)
2 → O(n)
3 → O(n log n)
4 → O(n²)
5 → O(n³)
6 → O(2ⁿ)

Dependencias Internas:
----------------------
- feature_extractor.py
    Extracción de características del código fuente.

- complexity_dataset.py
    Dataset de entrenamiento y etiquetas.

- hash_table.py
    Almacenamiento eficiente de métricas de entrenamiento.

- queue.py
    Gestión de mini-batches durante el entrenamiento.

- hard_mining.py
    Identificación de muestras con mayor error.

Algoritmos Utilizados:
----------------------
- Multilayer Perceptron (MLP)
- Stochastic Gradient Descent (SGD)
- Momentum Optimization
- Softmax Classification
- ReLU Activation
- Early Stopping
- Gradient Clipping
- Data Augmentation mediante ruido gaussiano

Tecnologías Utilizadas:
-----------------------
- Python
- NumPy
- Redes Neuronales Artificiales
- Machine Learning
- Estructuras de Datos Personalizadas

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures.hash_table import HashTable
from algorithms.hard_mining import get_hard_examples
from complexity.feature_extractor import extract_features, FEATURE_SIZE
from data.complexity_dataset import SAMPLES, CLASS_NAMES


# ── Hiperparámetros ───────────────────────────────────────────────────────────

NUM_CLASSES = 7

HIDDEN1 = 64
HIDDEN2 = 32

LEARNING_RATE = 0.01
LR_DECAY = 0.5
LR_DECAY_EVERY = 150

MOMENTUM = 0.9

EPOCHS = 500
PATIENCE = 80
BATCH_SIZE = 8

CLIP_VALUE = 1.0
NOISE_STD = 0.02


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
        self.W1 = None
        self.b1 = None

        self.W2 = None
        self.b2 = None

        self.W3 = None
        self.b3 = None

        self.vW1 = None
        self.vb1 = None

        self.vW2 = None
        self.vb2 = None

        self.vW3 = None
        self.vb3 = None

        self.is_trained = False
        self.accuracy = 0.0

        self.metrics = HashTable()
        self.hard_examples = []

        self.epochs_run = 0

    def _build_balanced_dataset(self, seed=42):
        np.random.seed(seed)

        X_raw = np.array(
            [extract_features(code) for code, _ in SAMPLES]
        )

        y_raw = np.array(
            [label for _, label in SAMPLES]
        )

        from collections import Counter

        max_count = max(
            Counter(y_raw.tolist()).values()
        )

        X_list = list(X_raw)
        y_list = list(y_raw)

        for cls in range(NUM_CLASSES):
            indices = np.where(y_raw == cls)[0]

            for _ in range(max_count - len(indices)):
                idx = np.random.choice(indices)

                noise = np.random.normal(
                    0,
                    NOISE_STD,
                    FEATURE_SIZE
                )

                X_list.append(
                    np.clip(X_raw[idx] + noise, 0, 1)
                )

                y_list.append(cls)

        X = np.array(X_list)
        y = np.array(y_list)

        perm = np.random.permutation(len(X))
        split = int(len(X) * 0.8)

        return (
            X[perm[:split]],
            X[perm[split:]],
            y[perm[:split]],
            y[perm[split:]]
        )

    def _forward(self, x):
        self._h1_in = x @ self.W1 + self.b1
        self._h1_out = relu(self._h1_in)

        self._h2_in = self._h1_out @ self.W2 + self.b2
        self._h2_out = relu(self._h2_in)

        self._o_in = self._h2_out @ self.W3 + self.b3
        self._o_out = softmax(self._o_in)

        return self._o_out

    def _backward(self, x, y_enc, lr):

        d3 = clip_grad(self._o_out - y_enc)

        self.vW3 = (
            MOMENTUM * self.vW3
            - lr * np.outer(self._h2_out, d3)
        )

        self.vb3 = (
            MOMENTUM * self.vb3
            - lr * d3
        )

        self.W3 += self.vW3
        self.b3 += self.vb3

        d2 = clip_grad(
            (d3 @ self.W3.T) * (self._h2_in > 0)
        )

        self.vW2 = (
            MOMENTUM * self.vW2
            - lr * np.outer(self._h1_out, d2)
        )

        self.vb2 = (
            MOMENTUM * self.vb2
            - lr * d2
        )

        self.W2 += self.vW2
        self.b2 += self.vb2

        d1 = clip_grad(
            (d2 @ self.W2.T) * (self._h1_in > 0)
        )

        self.vW1 = (
            MOMENTUM * self.vW1
            - lr * np.outer(x, d1)
        )

        self.vb1 = (
            MOMENTUM * self.vb1
            - lr * d1
        )

        self.W1 += self.vW1
        self.b1 += self.vb1

    def train_model(self) -> dict:

        X_train, X_test, y_train, y_test = (
            self._build_balanced_dataset()
        )

        Y_train = np.zeros(
            (len(y_train), NUM_CLASSES)
        )

        Y_train[
            np.arange(len(y_train)),
            y_train
        ] = 1

        np.random.seed(42)

        self.W1 = (
            np.random.randn(
                FEATURE_SIZE,
                HIDDEN1
            ) * np.sqrt(2 / FEATURE_SIZE)
        )

        self.b1 = np.zeros(HIDDEN1)

        self.W2 = (
            np.random.randn(
                HIDDEN1,
                HIDDEN2
            ) * np.sqrt(2 / HIDDEN1)
        )

        self.b2 = np.zeros(HIDDEN2)

        self.W3 = (
            np.random.randn(
                HIDDEN2,
                NUM_CLASSES
            ) * np.sqrt(2 / HIDDEN2)
        )

        self.b3 = np.zeros(NUM_CLASSES)

        self.vW1 = np.zeros_like(self.W1)
        self.vb1 = np.zeros_like(self.b1)

        self.vW2 = np.zeros_like(self.W2)
        self.vb2 = np.zeros_like(self.b2)

        self.vW3 = np.zeros_like(self.W3)
        self.vb3 = np.zeros_like(self.b3)

        best_acc = 0.0
        best_weights = None
        patience_ctr = 0

        losses_all = []

        lr = LEARNING_RATE

        for epoch in range(EPOCHS):

            if epoch > 0 and epoch % LR_DECAY_EVERY == 0:
                lr *= LR_DECAY
                print(f"📉 LR decay → {lr:.5f}")

            perm = np.random.permutation(
                len(X_train)
            )

            correct = 0
            ep_losses = []

            from data_structures.queue import Queue

            batch_queue = Queue()

            for start in range(
                0,
                len(X_train),
                BATCH_SIZE
            ):
                batch_queue.enqueue(
                    perm[start:start + BATCH_SIZE]
                )

            while not batch_queue.is_empty():

                for i in batch_queue.dequeue():

                    output = self._forward(
                        X_train[i]
                    )

                    if (
                        np.argmax(output)
                        == y_train[i]
                    ):
                        correct += 1

                    loss = float(
                        np.mean(
                            (output - Y_train[i]) ** 2
                        )
                    )

                    ep_losses.append(loss)
                    losses_all.append(loss)

                    self._backward(
                        X_train[i],
                        Y_train[i],
                        lr
                    )

            acc = (
                correct
                / len(X_train)
                * 100
            )

            avg_loss = float(
                np.mean(ep_losses)
            )

            self.metrics.set(
                f"epoch_{epoch + 1}_acc",
                round(acc, 2)
            )

            self.metrics.set(
                f"epoch_{epoch + 1}_loss",
                round(avg_loss, 6)
            )

            if acc > best_acc:

                best_acc = acc
                patience_ctr = 0

                best_weights = (
                    self.W1.copy(),
                    self.b1.copy(),
                    self.W2.copy(),
                    self.b2.copy(),
                    self.W3.copy(),
                    self.b3.copy(),
                )

            else:
                patience_ctr += 1

            if (epoch + 1) % 50 == 0:
                print(
                    f"Epoch {epoch + 1:3d}/{EPOCHS} | "
                    f"Acc: {acc:.1f}% | "
                    f"Loss: {avg_loss:.4f} | "
                    f"Best: {best_acc:.1f}% | "
                    f"LR: {lr:.5f} | "
                    f"Patience: {patience_ctr}/{PATIENCE}"
                )

            if patience_ctr >= PATIENCE:
                print(
                    f"\n⏹ Early stopping en época {epoch + 1}"
                )
                break

        self.epochs_run = epoch + 1

        (
            self.W1,
            self.b1,
            self.W2,
            self.b2,
            self.W3,
            self.b3,
        ) = best_weights

        self.hard_examples = get_hard_examples(
            losses_all,
            k=5
        )

        correct = sum(
            1
            for i in range(len(X_test))
            if int(
                np.argmax(
                    self._forward(X_test[i])
                )
            )
            == y_test[i]
        )

        self.accuracy = (
            correct
            / len(X_test)
            * 100
        )

        self.is_trained = True

        print("\n✅ Entrenamiento completo")
        print(f"Épocas ejecutadas : {self.epochs_run}")
        print(f"Best train acc    : {best_acc:.1f}%")
        print(f"Test accuracy     : {self.accuracy:.1f}%")

        return {
            "status": "trained",
            "train_samples": len(X_train),
            "test_samples": len(X_test),
            "epochs": self.epochs_run,
            "best_train_acc": round(best_acc, 2),
            "test_accuracy": round(self.accuracy, 2),
        }

    def predict_complexity(self, code: str) -> dict:

        if not self.is_trained:
            raise RuntimeError(
                "Modelo no entrenado. Usa /train_complexity primero."
            )

        features = extract_features(code)

        probabilities = self._forward(features)

        pred_class = int(
            np.argmax(probabilities)
        )

        confidence = float(
            probabilities[pred_class]
        )

        top3_idx = np.argsort(
            probabilities
        )[::-1][:3]

        top3 = [
            {
                "complexity": CLASS_NAMES[int(i)],
                "probability": round(
                    float(probabilities[i]),
                    4
                ),
            }
            for i in top3_idx
        ]

        return {
            "complexity": CLASS_NAMES[pred_class],
            "confidence": round(confidence, 4),
            "top3": top3,
        }

    def get_training_metrics(self) -> dict:

        result = {}

        for epoch in range(
            1,
            self.epochs_run + 1
        ):
            acc = self.metrics.get(
                f"epoch_{epoch}_acc"
            )

            loss = self.metrics.get(
                f"epoch_{epoch}_loss"
            )

            if acc is not None:
                result[f"epoch_{epoch}"] = {
                    "accuracy": acc,
                    "loss": loss,
                }

        return result

    def get_hard_examples(self) -> list:
        return self.hard_examples


complexity_model_service = ComplexityModelService()