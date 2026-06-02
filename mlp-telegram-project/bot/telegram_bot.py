import os
import requests

from dotenv import load_dotenv

from telegram import Update

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

import json

load_dotenv()

TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)

API_URL = os.getenv(
    "API_URL"
)


async def start(
    update: Update,
    context:
    ContextTypes.DEFAULT_TYPE
):

    await (
        update.message.reply_text(
            "MLP Algorithm "
            "System initialized."
        )
    )


async def help_command(
    update: Update,
    context:
    ContextTypes.DEFAULT_TYPE
):

    await (
        update.message.reply_text(
            """
Available commands:

/train
/status
/predict
/metrics
/hardexamples
/benchmark
/complexity
/help
"""
        )
    )


async def train(
    update: Update,
    context:
    ContextTypes.DEFAULT_TYPE
):

    await (
        update.message.reply_text(
            "Training started..."
        )
    )

    response = requests.post(
        f"{API_URL}/train"
    )

    data = response.json()

    await (
        update.message.reply_text(
            f"Training completed\n\n"
            f"Accuracy: "
            f"{data['accuracy']}%"
        )
    )


async def status(
    update: Update,
    context:
    ContextTypes.DEFAULT_TYPE
):

    response = requests.get(
        f"{API_URL}/status"
    )

    data = response.json()

    await (
        update.message.reply_text(
            f"System Status\n\n"
            f"Model: "
            f"{data['mlp_model']}\n"
            f"Accuracy: "
            f"{data['accuracy']}"
        )
    )


async def predict(
    update: Update,
    context:
    ContextTypes.DEFAULT_TYPE
):

    try:

        values = list(
            map(
                float,
                context.args
            )
        )

        if len(values) != 4:

            await (
                update.message.reply_text(
                    "Use:\n"
                    "/predict "
                    "5.1 3.5 "
                    "1.4 0.2"
                )
            )

            return

        response = requests.get(
            f"{API_URL}/predict",
            params={
                "sepal_length":
                values[0],

                "sepal_width":
                values[1],

                "petal_length":
                values[2],

                "petal_width":
                values[3]
            }
        )

        data = (
            response.json()
        )

        await (
            update.message.reply_text(
                f"Prediction:\n"
                f"{data['prediction']}"
            )
        )

    except Exception:

        await (
            update.message.reply_text(
                "Invalid input."
            )
        )


async def metrics(
    update: Update,
    context:
    ContextTypes.DEFAULT_TYPE
):

    response = requests.get(
        f"{API_URL}/metrics"
    )

    data = response.json()

    text = (
        "Training Metrics\n\n"
    )

    for key, value in (
        data.items()
    ):

        if value is not None:

            text += (
                f"{key}: "
                f"{value}%\n"
            )

    await (
        update.message.reply_text(
            text
        )
    )


async def hard_examples(
    update: Update,
    context:
    ContextTypes.DEFAULT_TYPE
):

    response = requests.get(
        f"{API_URL}/hard-examples"
    )

    data = response.json()

    text = (
        "Hard Examples\n\n"
    )

    for loss, idx in (
        data[
            "hard_examples"
        ]
    ):

        text += (
            f"Sample {idx}"
            f" → loss "
            f"{loss:.4f}\n"
        )

    await (
        update.message.reply_text(
            text
        )
    )


async def benchmark(
    update: Update,
    context:
    ContextTypes.DEFAULT_TYPE
):

    response = requests.get(
        f"{API_URL}/benchmark"
    )

    data = response.json()

    text = (
        "Benchmark Results\n\n"
    )

    for item in (
        data[
            "benchmark"
        ]
    ):

        text += (
            f"N={item['n']}\n"
            f"Heap: "
            f"{item['heap_time']:.6f}s\n"
            f"Sort: "
            f"{item['sort_time']:.6f}s\n\n"
        )

    await (
        update.message.reply_text(
            text
        )
    )


async def complexity(
    update: Update,
    context:
    ContextTypes.DEFAULT_TYPE
):

    response = requests.get(
        f"{API_URL}/complexity"
    )

    data = response.json()

    text = (
        "Algorithm Complexity\n\n"
    )

    for key, value in (
        data.items()
    ):

        text += (
            f"{key} "
            f"→ {value}\n"
        )

    await (
        update.message.reply_text(
            text
        )
    )

async def analize(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    """
    Uso:
        /analize <código Python>

    Ejemplo:
        /analize for i in range(n):\n  for j in range(n):\n    pass

    También acepta código multilínea si el usuario lo escribe
    en el mismo mensaje después del comando.
    """
    # Tomar todo el texto después de /analize
    if not context.args:
        await update.message.reply_text(
            "⚠️ Uso: /analize <código Python>\n\n"
            "Ejemplo:\n"
            "`/analize for i in range(n):\\n  for j in range(n):\\n    pass`\n\n"
            "💡 También puedes pegar código multilínea directamente "
            "como mensaje de texto.",
            parse_mode="Markdown"
        )
        return

    # Reconstruir el código desde los args (preserva espacios)
    raw_text = update.message.text
    # Remover "/analize " del inicio
    code = raw_text[len("/analize "):].strip()
    # Reemplazar \n literales por saltos de línea reales
    code = code.replace("\\n", "\n").replace("\\t", "\t")

    await _call_analize_api(update, code)

async def analize_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    """
    Detecta si un mensaje de texto plano parece código Python
    y lo analiza automáticamente.
    Heurística: contiene "def ", "for ", "while " o "return ".
    """
    text = update.message.text.strip()
    code_keywords = ("def ", "for ", "while ", "return ", "if ", "class ")

    if any(kw in text for kw in code_keywords):
        await update.message.reply_text(
            "🔎 Parece código Python. Analizando complejidad...",
            parse_mode="Markdown"
        )
        await _call_analize_api(update, text)

async def _call_analize_api(update: Update, code: str):
    try:
        response = requests.post(
            f"{API_URL}/analize",
            json={"code": code},
            timeout=10
        )
        data = response.json()

        complexity = data.get("complexity", "?")
        reason     = data.get("reason", "")
        confidence = data.get("confidence", "")
        details    = data.get("details", [])

        # Emoji por complejidad
        emoji_map = {
            "O(1)":      "🟢",
            "O(log n)":  "🟡",
            "O(n)":      "🟡",
            "O(n log n)":"🟠",
            "O(n²)":     "🔴",
            "O(n³)":     "🔴",
            "O(2^n)":    "💀",
            "O(n!)":     "💀",
        }
        emoji = emoji_map.get(complexity, "🔵")

        text = (
            f"🔍 *Análisis de Complejidad*\n\n"
            f"{emoji} *Complejidad:* `{complexity}`\n"
            f"💡 *Razón:* {reason}\n"
            f"🎯 *Confianza:* {confidence}\n"
        )

        if details:
            text += "\n📝 *Observaciones:*\n"
            for d in details:
                text += f"  • {d}\n"

        await update.message.reply_text(
            text,
            parse_mode="Markdown"
        )

    except Exception as e:
        await update.message.reply_text(
            f"❌ Error al analizar: {str(e)}"
        )


async def train_complexity(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "⏳ Entrenando MLP clasificador de complejidad...\n"
        "Esto puede tardar unos segundos."
    )

    try:
        response = requests.post(
            f"{API_URL}/train_complexity",
            timeout=120  # ← el entrenamiento puede tardar
        )
        data = response.json()

        if "error" in data:
            await update.message.reply_text(f"❌ Error: {data['error']}")
            return

        await update.message.reply_text(
            f"✅ *Entrenamiento completo*\n\n"
            f"🎯 Test accuracy: `{data.get('test_accuracy')}%`\n"
            f"🏆 Best train acc: `{data.get('best_train_acc')}%`\n"
            f"📊 Train samples: `{data.get('train_samples')}`\n"
            f"🧪 Test samples: `{data.get('test_samples')}`\n"
            f"🔁 Épocas: `{data.get('epochs')}`",
            parse_mode="Markdown"
        )

    except requests.exceptions.Timeout:
        await update.message.reply_text(
            "⚠️ El entrenamiento está tomando más de lo esperado.\n"
            "Intenta /status para ver si el modelo ya está listo."
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

def main():

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )

    commands = [
        ("start", start),
        ("help", help_command),
        ("train", train),
        ("status", status),
        ("predict", predict),
        ("metrics", metrics),
        ("hardexamples", hard_examples),
        ("benchmark", benchmark),
        ("complexity", complexity),
        ("train_complexity", train_complexity), 
        ("analize", analize)

    ]

    for name, fn in commands:

        app.add_handler(
            CommandHandler(
                name,
                fn
            )
        )

    print(
        "Bot running..."
    )

    from telegram.ext import MessageHandler, filters
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analize_message))

    app.run_polling()


if __name__ == "__main__":
    main()