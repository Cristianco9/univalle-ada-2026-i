import os
import requests

from dotenv import load_dotenv

from telegram import (
    Update
)

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


def main():

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CommandHandler(
            "help",
            help_command
        )
    )

    app.add_handler(
        CommandHandler(
            "train",
            train
        )
    )

    app.add_handler(
        CommandHandler(
            "status",
            status
        )
    )

    app.add_handler(
        CommandHandler(
            "predict",
            predict
        )
    )

    print(
        "Bot running..."
    )

    app.run_polling()


if __name__ == "__main__":
    main()