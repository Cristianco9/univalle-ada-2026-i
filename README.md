**Autores:** 

- Cristian Camilo Cortes Ortiz - 202478542

- Katherine Arboleda Ocoro - 202478504

**Universidad del Valle**  

**Programa:** Tecnología en Desarrollo de Software

**Asignatura:** Análisis y Diseño de Algoritmos

**Profesor:** Daniel Quintero Capera  

**Fecha:** 06 Junio 2026



# MLP Algorithm Complexity Classifier

## Descripción del Proyecto

Este proyecto implementa un **Perceptrón Multicapa (MLP) desde cero** usando 
únicamente NumPy, capaz de clasificar la complejidad algorítmica de
de código Python enviados a través de un **bot de Telegram**.

El sistema recibe un algoritmo como entrada y responde con su notación Big-O 
clasificada en una de las siguientes categorías:

| Clase | Complejidad | Ejemplo típico |
|-------|-------------|----------------|
| 0 | O(1) | Acceso directo a array o diccionario |
| 1 | O(log n) | Búsqueda binaria |
| 2 | O(n) | Recorrido lineal |
| 3 | O(n log n) | Merge sort, sorted() |
| 4 | O(n²) | Bubble sort, doble bucle |
| 5 | O(n³) | Multiplicación de matrices |
| 6 | O(2^n) | Fibonacci recursivo, subconjuntos |

### Arquitectura del sistema

```
Usuario (Telegram)
      ↓
Bot de Telegram (python-telegram-bot)
      ↓
API REST (FastAPI + Uvicorn)
      ↓
MLP Clasificador (NumPy puro)
      ↓
Feature Extractor (AST de Python)
      ↓
Dataset de snippets etiquetados
```

### Pipeline del MLP

```
Código Python
      ↓
Feature Extractor (AST) → vector[12]
      ↓
MLP: input(12) → hidden1(64, ReLU) → hidden2(32, ReLU) →
     output(7, Softmax)
      ↓
Clase de complejidad + probabilidades Top-3 + gráfica PNG
```

### Módulos implementados

El proyecto implementa y analiza algorítmicamente los siguientes módulos:

- **MLP desde cero** — forward pass, backpropagation, SGD con momentum,
  gradient clipping, early stopping y learning rate decay
- **Feature Extractor** — análisis de AST para extraer 12 features
  numéricas del código
- **Complexity Plotter** — generación de gráficas de complejidad espacio-
  temporal con Matplotlib, retornadas como imagen PNG
- **Dataset** — 142 snippets etiquetados y balanceados con augmentation
  gaussiana
- **Hard Mining** — selección de ejemplos difíciles con heap
  (`heapq.nlargest`) → O(n log k)
- **Quickselect** — cálculo de mediana en O(n) promedio vs O(n log n)
  con sort
- **Top-K** — comparativa heap vs sort para selección de k mejores pérdidas
- **Cola de lotes** — procesamiento de batches con estructura Queue →
  O(1) enqueue/dequeue
- **HashTable** — almacenamiento de métricas por época → O(1) amortizado

---

## Estructura del Proyecto

```
mlp-telegram-project/
  algorithms/
    hard_mining.py             ← Top-k con heap (RA2)
    quickselect.py             ← Mediana en O(n) (RA2)
    top_k.py                   ← Heap vs Sort benchmark (RA2)
  api/
    app.py                     ← API REST con FastAPI
  bot/
    telegram_bot.py            ← Bot de Telegram
  complexity/
    feature_extractor.py       ← AST → vector de features
    complexity_plotter.py      ← Generador de gráficas PNG
  data/
    complexity_dataset.py      ← 142 snippets etiquetados
  data_structures/
    hash_table.py              ← HashTable para métricas (RA3)
    queue.py                   ← Cola de lotes (RA3)
  experiments/
    benchmark.py               ← Benchmark Top-K
    quickselect_benchmark.py   ← Benchmark Quickselect
    plot_benchmark.py          ← Gráficas de escalado
  mlp/
    complexity_model_service.py ← MLP clasificador principal
  tests/
    test_hard_mining.py
    test_hash_table.py
    test_queue.py
    test_quickselect.py
  utils/
    batch_loader.py            ← Crea batches con Queue
    encoding.py                ← One-hot encoding
  .env                         ← Variables de entorno (no subir a git)
  requirements.txt
  README.md
```

---

## Instalación

### Requisitos previos

- Python 3.11 o superior
- pip

### 1. Clonar el repositorio

```bash
git clone https://github.com/Cristianco9/univalle-ada-2026-i
cd univalle-ada-2026-i/mlp-telegram-project/
```

### 2. Crear el entorno virtual

```bash
python3 -m venv .venv
```

### 3. Activar el entorno virtual

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
TELEGRAM_BOT_TOKEN=tu_token_de_telegram
API_URL=http://localhost:8000
```

> Para obtener un token de Telegram, habla con
> [@BotFather](https://t.me/BotFather) en Telegram y crea un nuevo bot
> con `/newbot`.

---

## Lanzar el proyecto

Necesitas dos terminales abiertas simultáneamente.

### Terminal 1 — Lanzar la API

```bash
# Asegúrate de estar en la raíz del proyecto con el entorno activado
source .venv/bin/activate
uvicorn api.app:app --reload
```

La API estará disponible en: `http://localhost:8000`  
Documentación interactiva: `http://localhost:8000/docs`

### Terminal 2 — Lanzar el Bot

```bash
# En otra terminal, desde la raíz del proyecto
source .venv/bin/activate
python3 bot/telegram_bot.py
```

---

## Endpoints de la API

### `GET /`
Verifica que la API está corriendo.

```bash
curl http://localhost:8000/
```

**Respuesta:**
```json
{"message": "API running"}
```

---

### `GET /status`
Retorna el estado actual del modelo.

```bash
curl http://localhost:8000/status
```

**Respuesta:**
```json
{
  "status": "online",
  "mlp_model": "trained",
  "accuracy": 93.75
}
```

---

### `POST /train_complexity`
Entrena el MLP con el dataset de snippets de código. Debe ejecutarse al
menos una vez antes de usar `/analize`.

```bash
curl -X POST http://localhost:8000/train_complexity
```

**Respuesta:**
```json
{
  "status": "trained",
  "train_samples": 154,
  "test_samples": 39,
  "epochs": 140,
  "best_train_acc": 100.0,
  "test_accuracy": 93.75
}
```

---

### `POST /analize`
Recibe un snippet de código Python y retorna su complejidad algorítmica
predicha por el MLP.

```bash
curl -X POST http://localhost:8000/analize \
  -H "Content-Type: application/json" \
  -d '{"code": "for i in range(n):\n  for j in range(n):\n    pass"}'
```

**Respuesta:**
```json
{
  "complexity": "O(n²)",
  "confidence": 0.9823,
  "top3": [
    {"complexity": "O(n²)",      "probability": 0.9823},
    {"complexity": "O(n³)",      "probability": 0.0134},
    {"complexity": "O(n log n)", "probability": 0.0043}
  ]
}
```

---

### `GET /analize/plot`
Retorna una imagen PNG con la gráfica de complejidad espacio-temporal
del algoritmo analizado. El panel izquierdo muestra la curva destacada
con su rango real de operaciones, y el panel derecho compara todas las
complejidades resaltando la predicha.

```bash
curl "http://localhost:8000/analize/plot?complexity=O(n²)" \
  --output grafica.png
```

**Parámetros:**

| Parámetro | Tipo | Valores válidos |
|-----------|------|-----------------|
| `complexity` | string | `O(1)` `O(log n)` `O(n)` `O(n log n)` |
| | | `O(n²)` `O(n³)` `O(2^n)` |

**Respuesta:** imagen `image/png` (≈ 150 KB)

> El bot de Telegram llama a este endpoint automáticamente después de
> cada `/analize` y envía la imagen directamente en el chat.

---

### `GET /complexity_metrics`
Retorna el accuracy y loss por época del entrenamiento del clasificador.

```bash
curl http://localhost:8000/complexity_metrics
```

**Respuesta:**
```json
{
  "epoch_1":  {"accuracy": 42.14, "loss": 0.0996},
  "epoch_2":  {"accuracy": 66.43, "loss": 0.0727},
  "epoch_60": {"accuracy": 100.0, "loss": 0.0014}
}
```

---

### `GET /hard-examples`
Retorna los 5 ejemplos con mayor pérdida del entrenamiento
(hard mining con heap).

```bash
curl http://localhost:8000/hard-examples
```

**Respuesta:**
```json
{
  "hard_examples": [
    [0.1823, 142],
    [0.1654, 87],
    [0.1521, 203],
    [0.1398, 56],
    [0.1287, 178]
  ]
}
```

---

### `GET /benchmark`
Ejecuta el benchmark de Top-K comparando heap vs sort para diferentes
tamaños de entrada.

```bash
curl http://localhost:8000/benchmark
```

**Respuesta:**
```json
{
  "benchmark": [
    {"n": 1000,   "heap_time": 0.000312, "sort_time": 0.000891},
    {"n": 5000,   "heap_time": 0.000743, "sort_time": 0.004521},
    {"n": 10000,  "heap_time": 0.001234, "sort_time": 0.009876},
    {"n": 50000,  "heap_time": 0.005432, "sort_time": 0.051234},
    {"n": 100000, "heap_time": 0.009871, "sort_time": 0.108432}
  ]
}
```

---

### `GET /complexity`
Retorna las complejidades teóricas Big-O de los módulos implementados.

```bash
curl http://localhost:8000/complexity
```

**Respuesta:**
```json
{
  "top_k_heap":           "O(n log k)",
  "top_k_sort":           "O(n log n)",
  "quickselect_average":  "O(n)",
  "hash_table":           "O(1)",
  "queue":                "O(1)",
  "mlp_forward":          "O(B * h * output)",
  "mlp_backprop":         "O(B * h * output)"
}
```

---

## Comandos del Bot de Telegram

| Comando | Descripción |
|---------|-------------|
| `/start` | Inicializa el bot |
| `/help` | Muestra todos los comandos disponibles |
| `/train_complexity` | Entrena el MLP clasificador |
| `/analize <código>` | Clasifica la complejidad y muestra la gráfica |
| `/status` | Estado actual del modelo |
| `/complexity_metrics` | Resumen de accuracy y loss por época |
| `/hardexamples` | Ejemplos más difíciles del entrenamiento |
| `/benchmark` | Benchmark heap vs sort |
| `/complexity` | Complejidades teóricas de los módulos |

### Ejemplo de uso del bot

```
/train_complexity
```
> Entrena el MLP. Espera el mensaje de confirmación con el accuracy
> antes de continuar.

```
/analize def fib(n):\n  if n<=1: return n\n  return fib(n-1)+fib(n-2)
```
> Respuesta esperada: mensaje con `O(2^n)` y alta certeza, seguido de
> una imagen con la gráfica comparativa de complejidades.

También puedes **pegar código directamente** como mensaje de texto sin
usar el comando `/analize` — el bot lo detecta automáticamente si
contiene palabras clave como `def`, `for`, `while`, `return`.

---

## Ejecución de Tests

> Ejecución de todos los test
```bash
python3 -m pytest tests/ -v
```

> Ejecución individual de cada test
```bash
python3 -m pytest tests/test_hard_minig.py -v
python3 -m pytest tests/test_hash_table.py -v
python3 -m pytest tests/test_queue.py -v
python3 -m pytest tests/test_quickselect.py -v
```

---

## Notas técnicas

- El modelo se entrena **en memoria** — si reinicias la API debes
  ejecutar `/train_complexity` nuevamente.
- El entrenamiento usa **early stopping con patience=80** — para
  automáticamente si no mejora en 80 épocas consecutivas.
- El **learning rate** decae por un factor de 0.5 cada 150 épocas
  para afinar la convergencia.
- El dataset se **balancea automáticamente** con augmentation gaussiana
  (ruido σ=0.02) para igualar la cantidad de muestras por clase.
- Las gráficas se generan **en memoria** con Matplotlib usando un
  backend sin pantalla (`Agg`), sin escribir archivos temporales en
  disco.