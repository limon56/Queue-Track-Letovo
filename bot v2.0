import logging
import time

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import requests

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
callback_data = '0'

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboard = [[InlineKeyboardButton("Show queue", callback_data='1')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\!', reply_markup=reply_markup)

def button(update, _):
    query = update.callback_query
    variant = query.data
    query.answer()
    query.edit_message_text(text=f"Выбранный вариант: {variant}")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')

def authors(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("@FrostDeath, @mikhailandri, @chickysnail")

def donates(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Thanks fo understanding!")
    update.message.reply_text("https://www.donationalerts.com/r/feed_queue_creators")

def request_queue(update: Update, context: CallbackContext) -> None:
    url = open("D:/прога/BOT/BOT/kapkeiki.png", 'rb')
    time.sleep(0.1)
    update.message.reply_photo(url)

def main() -> None:
    updater = Updater("2129247987:AAHdzOCLztXr19IH_KKostgsQ8xZmdYxDCk") #Tocken of Bot

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("request_queue", request_queue))
    dispatcher.add_handler(CommandHandler("authors", authors))
    dispatcher.add_handler(CommandHandler("smth", donates))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
