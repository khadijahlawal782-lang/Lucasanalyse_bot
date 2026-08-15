import os
import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

GROUP_LINK = "https://t.me/+aZyjCO1v0yoxNWQ1"

WELCOME_TEXT = (
    "👋 Salut !\n"
    "Bienvenue chez Lucas Analyse 📊⚽️\n\n"
    "Pour accéder au groupe privé et recevoir mes analyses exclusives, clique ci-dessous :\n\n"
    "👉 Rejoindre le groupe privé :\n"
    f"{GROUP_LINK}\n\n"
    "⚡️ Places limitées — ne tarde pas !"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        keyboard = [
            [InlineKeyboardButton("🚀 Rejoindre le Groupe Privé", url=GROUP_LINK)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            WELCOME_TEXT,
            reply_markup=reply_markup
        )
        logger.info(f"Sent welcome message to user {update.effective_user.id}")
    except Exception as e:
        logger.error(f"Error in start handler: {e}")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Update {update} caused error: {context.error}")


def main() -> None:
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN environment variable is not set.")
        raise SystemExit(1)

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_error_handler(error_handler)

    logger.info("Bot starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
