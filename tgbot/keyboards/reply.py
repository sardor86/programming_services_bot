from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def register_user_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(KeyboardButton('Отправить свой номер для регистрации', request_contact=True))

    return keyboard
