from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import logging, os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
app = Flask(__name__)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

# Command handler: /start
def start(update, context):
    update.message.reply_text("سلام، عکس رو بفرست 📸")

# Message handler: Photo
def photo_handler(update, context):
    update.message.reply_text("عکس دریافت شد! (اینجا باید عملیات ادیت بشه)")

# Register handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
