from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.models import Users
from tgbot.config import DataBase


def user_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.insert(InlineKeyboardButton('something', callback_data='something'))
    return keyboard


def admin_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.insert(InlineKeyboardButton('Повысить права пользователя', callback_data='up_user_admin'))
    keyboard.insert(InlineKeyboardButton('Понизить права пользователя', callback_data='down_user_admin'))
    keyboard.insert(InlineKeyboardButton('Добавить событие', callback_data='add_event_admin'))
    keyboard.insert(InlineKeyboardButton('Удалить событие', callback_data='delete_event_admin'))
    keyboard.insert(InlineKeyboardButton('Добавить услуги', callback_data='add_service_admin'))
    keyboard.insert(InlineKeyboardButton('Удалить услуги', callback_data='delete_service_admin'))
    return keyboard


def admin_choice_tip_user() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.insert(InlineKeyboardButton('Админ', callback_data='choice_admin_tip'))
    keyboard.insert(InlineKeyboardButton('Программист', callback_data='choice_programmer_tip'))
    keyboard.insert(InlineKeyboardButton('Оператор', callback_data='choice_operator_tip'))
    return keyboard


def programmer_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.insert(InlineKeyboardButton('something', callback_data='something'))
    return keyboard


def operator_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.insert(InlineKeyboardButton('something', callback_data='something'))
    return keyboard


def choice_menu(db: DataBase, user_id: int) -> InlineKeyboardMarkup:
    user = Users(db).get_all_information_user(user_id)

    keyboard = InlineKeyboardMarkup(row_width=1)

    if user.rights_admin or user.rights_programmer or user.rights_operator:
        if user.rights_admin:
            keyboard.insert(InlineKeyboardButton('Админ', callback_data='admin_menu'))
        if user.rights_programmer:
            keyboard.insert(InlineKeyboardButton('Программист', callback_data='programmer_menu'))
        if user.rights_operator:
            keyboard.insert(InlineKeyboardButton('Оператор', callback_data='operator_menu'))
    else:
        return user_menu()

    return keyboard

