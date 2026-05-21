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

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = os.getenv("API_URL")


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "MLP Algorithm Analysis System initialized."
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        """
Available commands:

/start
/status
/help
        """
    )


async def status(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    try:
        response = requests.get(
            f"{API_URL}/status"
        )

        data = response.json()

        message = (
            f"System Status\n\n"
            f"Status: {data['status']}\n"
            f"API: {data['api']}\n"
            f"MLP Model: {data['mlp_model']}"
        )

        await update.message.reply_text(
            message
        )

    except Exception as error:
        await update.message.reply_text(
            f"Error connecting to API: {error}"
        )


def main():
    app = ApplicationBuilder().token(
        TOKEN
    ).build()

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
            "status",
            status
        )
    )

    print(
        "Telegram bot running..."
    )

    app.run_polling()


if __name__ == "__main__":
    main()