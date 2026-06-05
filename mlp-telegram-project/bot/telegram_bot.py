import os
import requests

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()

TOKEN   = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = os.getenv("API_URL")


# ── /start ────────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "MLP Algorithm Complexity Classifier\n"
        "Escribe /help para ver los comandos disponibles."
    )


# ── /help ─────────────────────────────────────────────────────────────────────

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos disponibles:\n\n"
        "/train_complexity  - Entrena el MLP clasificador\n"
        "/analize <codigo>  - Clasifica la complejidad de un algoritmo\n"
        "/status            - Estado del modelo\n"
        "/complexity_metrics- Accuracy y loss por epoca\n"
        "/hardexamples      - Ejemplos mas dificiles del entrenamiento\n"
        "/benchmark         - Benchmark heap vs sort\n"
        "/complexity        - Complejidades teoricas de los modulos\n"
        "/help              - Muestra este mensaje\n\n"
        "Tambien puedes pegar codigo directamente como mensaje de texto."
    )


# ── /status ───────────────────────────────────────────────────────────────────

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(f"{API_URL}/status")
    data     = response.json()
    await update.message.reply_text(
        f"Estado del sistema\n\n"
        f"Modelo: {data['mlp_model']}\n"
        f"Accuracy: {data['accuracy']}"
    )


# ── /train_complexity ─────────────────────────────────────────────────────────

async def train_complexity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Entrenando MLP clasificador de complejidad...\n"
        "Esto puede tardar unos segundos."
    )
    try:
        response = requests.post(
            f"{API_URL}/train_complexity",
            timeout=120
        )
        data = response.json()

        if "error" in data:
            await update.message.reply_text(f"Error: {data['error']}")
            return

        await update.message.reply_text(
            f"Entrenamiento completo\n\n"
            f"Test accuracy:  {data.get('test_accuracy')}%\n"
            f"Best train acc: {data.get('best_train_acc')}%\n"
            f"Train samples:  {data.get('train_samples')}\n"
            f"Test samples:   {data.get('test_samples')}\n"
            f"Epocas:         {data.get('epochs')}"
        )
    except requests.exceptions.Timeout:
        await update.message.reply_text(
            "El entrenamiento esta tomando mas tiempo del esperado. "
            "Intenta /status para verificar si ya termino."
        )
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")


# ── /complexity_metrics ───────────────────────────────────────────────────────

async def complexity_metrics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(f"{API_URL}/complexity_metrics")
    data     = response.json()

    if not data:
        await update.message.reply_text(
            "No hay metricas disponibles.\n"
            "Ejecuta /train_complexity primero."
        )
        return

    items = list(data.items())
    total = len(items)

    # Mejor epoca
    best = max(items, key=lambda x: x[1].get('accuracy', 0))
    best_epoch = best[0]
    best_acc   = best[1]['accuracy']
    best_loss  = best[1]['loss']

    # Primera y ultima epoca
    first_key, first_val = items[0]
    last_key,  last_val  = items[-1]

    # Resumen compacto — nunca supera el limite de Telegram
    text = (
        f"Metricas de entrenamiento\n\n"
        f"Total de epocas: {total}\n\n"
        f"Epoca inicial\n"
        f"  {first_key}: acc={first_val['accuracy']}%  loss={first_val['loss']}\n\n"
        f"Mejor epoca\n"
        f"  {best_epoch}: acc={best_acc}%  loss={best_loss}\n\n"
        f"Ultima epoca\n"
        f"  {last_key}: acc={last_val['accuracy']}%  loss={last_val['loss']}\n\n"
        f"Ultimas 5 epocas:\n"
    )

    for key, val in items[-5:]:
        text += f"  {key}: acc={val['accuracy']}%  loss={val['loss']}\n"

    await update.message.reply_text(text)


# ── /hardexamples ─────────────────────────────────────────────────────────────

async def hard_examples(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(f"{API_URL}/hard-examples")
    data     = response.json()

    text = "Ejemplos mas dificiles (hard mining)\n\n"
    for loss, idx in data["hard_examples"]:
        text += f"Sample {idx} -> loss {loss:.4f}\n"

    await update.message.reply_text(text)


# ── /benchmark ────────────────────────────────────────────────────────────────

async def benchmark(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(f"{API_URL}/benchmark")
    data     = response.json()

    text = "Benchmark Heap vs Sort (Top-K)\n\n"
    for item in data["benchmark"]:
        text += (
            f"N={item['n']}\n"
            f"  Heap: {item['heap_time']:.6f}s\n"
            f"  Sort: {item['sort_time']:.6f}s\n\n"
        )

    await update.message.reply_text(text)


# ── /complexity ───────────────────────────────────────────────────────────────

async def complexity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(f"{API_URL}/complexity")
    data     = response.json()

    text = "Complejidades teoricas\n\n"
    for key, value in data.items():
        text += f"{key} -> {value}\n"

    await update.message.reply_text(text)


# ── /analize ──────────────────────────────────────────────────────────────────

async def analize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Uso: /analize <codigo Python>\n\n"
            "Ejemplo:\n"
            "/analize for i in range(n):\\n  for j in range(n):\\n    pass\n\n"
            "Tambien puedes pegar el codigo directamente como mensaje."
        )
        return

    raw_text = update.message.text
    code     = raw_text[len("/analize "):].strip()
    code     = code.replace("\\n", "\n").replace("\\t", "\t")

    await _call_analize_api(update, code)


# ── Mensaje de texto plano (codigo pegado directamente) ───────────────────────

async def analize_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text         = update.message.text.strip()
    code_keywords = ("def ", "for ", "while ", "return ", "if ", "class ")

    if any(kw in text for kw in code_keywords):
        await update.message.reply_text("Analizando complejidad...")
        await _call_analize_api(update, text)


# ── Helper: llamar API y formatear respuesta ──────────────────────────────────

async def _call_analize_api(update: Update, code: str):
    try:
        response = requests.post(
            f"{API_URL}/analize",
            json={"code": code},
            timeout=10
        )
        data = response.json()

        if "error" in data:
            await update.message.reply_text(f"Error: {data['error']}")
            return

        complexity = data.get("complexity", "?")
        confidence = data.get("confidence", 0)
        top3       = data.get("top3", [])

        emoji_map = {
            "O(1)":       "🟢",
            "O(log n)":   "🟡",
            "O(n)":       "🟡",
            "O(n log n)": "🟠",
            "O(n²)":      "🔴",
            "O(n³)":      "🔴",
            "O(2^n)":     "💀",
            "O(n!)":      "💀",
        }

        reason_map = {
            "O(1)":       "Operaciones constantes: acceso directo, sin bucles ni recursion.",
            "O(log n)":   "Reduccion logaritmica: division del problema a la mitad en cada paso.",
            "O(n)":       "Recorrido lineal: el tiempo crece proporcional al tamano de entrada.",
            "O(n log n)": "Ordenamiento eficiente: divide y combina linealmente en cada nivel.",
            "O(n²)":      "Doble iteracion: bucles anidados que comparan o procesan todos los pares.",
            "O(n³)":      "Triple iteracion: tres bucles anidados sobre la misma entrada.",
            "O(2^n)":     "Explosion exponencial: recursion que se ramifica en dos llamadas por nivel.",
            "O(n!)":      "Complejidad factorial: genera todas las permutaciones posibles.",
        }

        emoji    = emoji_map.get(complexity, "🔵")
        reason   = reason_map.get(complexity, "Patron no identificado.")
        conf_pct = round(confidence * 100, 1)

        if conf_pct >= 90:
            certeza = "Alta certeza"
        elif conf_pct >= 70:
            certeza = "Certeza moderada"
        else:
            certeza = "Baja certeza — revisa el codigo manualmente"

        top3_text = "\nDistribucion de probabilidades:\n"
        for item in top3:
            pct    = round(item['probability'] * 100, 1)
            icon   = "🟢" if pct >= 70 else "🟡" if pct >= 40 else "🔴"
            marker = " <- elegida" if item['complexity'] == complexity else ""
            top3_text += f"  {icon} {item['complexity']:10s} {pct:5.1f}%{marker}\n"

        text = (
            f"Analisis de Complejidad\n\n"
            f"{emoji} Complejidad: {complexity}\n"
            f"Razon: {reason}\n"
            f"Confianza: {conf_pct}% ({certeza})"
            f"{top3_text}"
        )

        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text(f"Error al analizar: {str(e)}")


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    commands = [
        ("start",             start),
        ("help",              help_command),
        ("status",            status),
        ("train_complexity",  train_complexity),
        ("analize",           analize),
        ("complexity_metrics",complexity_metrics),
        ("hardexamples",      hard_examples),
        ("benchmark",         benchmark),
        ("complexity",        complexity),
    ]

    for name, fn in commands:
        app.add_handler(CommandHandler(name, fn))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, analize_message)
    )

    print("Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()