import os
from keyboards.menu import main_menu

def start(bot, message):
    """Команда приветствия"""
    photo_path = os.path.join("media", "cat.jpg")

    if os.path.exists(photo_path):
        with open(photo_path, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="Привет! Я твой кот 🐾")
    else:
        bot.send_message(message.chat.id, "Привет! Я твой кот 🐾")

    bot.send_message(message.chat.id, "Выбери, что сделать:", reply_markup=main_menu)