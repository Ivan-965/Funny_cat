from telebot import types

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row("Погладить кота 🐱", "Обнять кота 🤗")
main_menu.add("История выбора 📜")