import os
import requests

from dotenv import load_dotenv

from telegram import Update

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

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
        ("complexity", complexity)
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

    app.run_polling()


if __name__ == "__main__":
    main()