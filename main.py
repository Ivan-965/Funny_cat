import os
from dotenv import load_dotenv
import telebot

from handlers.start import start
from handlers.actions import handle_action

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    start(bot, message)


@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    handle_action(bot, message)


if __name__ == "__main__":
    print("наш бот запущен... ")
    bot.infinity_polling()
