import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

WELCOME_MESSAGE = """👋 Salut !
Bienvenue chez Lucas Analyse 📊⚽️
Pour accéder au groupe privé et recevoir mes analyses exclusives, clique ci-dessous :
👉 Rejoindre le groupe privé :

https://t.me/+aZyjCO1v0yoxNWQ1

⚡️ Places limitées — ne tarde pas !"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

def main():
    token = os.environ["BOT_TOKEN"]
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
