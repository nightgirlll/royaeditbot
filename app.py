from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)
bot = Bot(token=TOKEN)
application = Application.builder().token(TOKEN).build()

@app.route('/webhook', methods=['POST'])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    await application.process_update(update)
    return 'ok'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام، عکس رو بده 📸")

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دریافت شد (باید عملیات ادیت بشه)")

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.PHOTO, photo))
