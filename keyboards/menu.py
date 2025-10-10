from telegram import ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    [
        ["Погладить кота 🐱", "Обнять кота 🤗"],
        ["История выбора 📜"]
    ],
    resize_keyboard=True
)
