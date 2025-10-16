import os
from dotenv import load_dotenv
import telebot

from handlers.start import start


load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    start(bot, message)



if __name__ == "__main__":
    print("наш бот запущен... ")
    bot.infinity_polling()