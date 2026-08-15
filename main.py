import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Welcome message in French
WELCOME_MESSAGE = """👋 Salut !
Bienvenue chez Lucas Analyse 📊⚽️
Pour accéder au groupe privé et recevoir mes analyses exclusives, clique ci-dessous :
👉 Rejoindre le groupe privé :

https://t.me/+aZyjCO1v0yoxNWQ1

⚡️ Places limitées — ne tarde pas !"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responds to the /start command."""
    if update.message:
        await update.message.reply_text(WELCOME_MESSAGE)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responds to any text message sent by the user."""
    if not update.message or not update.message.text:
        return
        
    text = update.message.text.lower()
    
    # Check for goal / prediction keywords
    if any(word in text for word in ["but", "goal", "prédiction", "prediction", "pronostic", "prono"]):
        response = (
            "⚽️ **Analyse & Prédiction**\n\n"
            "Toutes nos prédictions de buts et analyses en direct sont publiées dans le groupe privé !\n"
            "Clique ici pour rejoindre : https://t.me/+aZyjCO1v0yoxNWQ1"
        )
    else:
        response = WELCOME_MESSAGE
        
    await update.message.reply_text(response, parse_mode="Markdown")

if __name__ == "__main__":
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        print("ERROR: BOT_TOKEN environment variable is missing!", file=sys.stderr)
        sys.exit(1)
        
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling(drop_pending_updates=True)
