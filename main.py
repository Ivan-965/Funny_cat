import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

from handlers.start import start

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()