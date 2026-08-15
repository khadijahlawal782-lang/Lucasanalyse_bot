import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Votre message de bienvenue
WELCOME_MESSAGE = """👋 Salut !
Bienvenue chez Lucas Analyse 📊⚽️
Pour accéder au groupe privé et recevoir mes analyses exclusives, clique ci-dessous :
👉 Rejoindre le groupe privé :

https://t.me/+aZyjCO1v0yoxNWQ1

⚡️ Places limitées — ne tarde pas !"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
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
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot en cours d'exécution...")
    app.run_polling()
