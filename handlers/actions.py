import os

history = []


def handle_action(bot, message):
    """Обработка кнопки 'Погладить кота'"""
    text = message.text

    if "Погладить" in text:
        history.append("Погладить кота")
        photo_path = os.path.join("media", "cat2.jpg")
        if os.path.exists(photo_path):
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo, caption="Кот счастлив")
    elif "Обнять" in text:
        history.append("Обнять кота")
        photo_path = os.path.join("media", "cat3.jpg")
        if os.path.exists(photo_path):
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo, caption="Обнять кота")
