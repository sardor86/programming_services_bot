from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.models import Users
from tgbot.config import DataBase


def user_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.insert(InlineKeyboardButton('Посмотреть услуги', callback_data='watch_service_0'))
    keyboard.insert(InlineKeyboardButton('Посмотреть событья', callback_data='watch_event_0'))
    keyboard.insert(InlineKeyboardButton('Связатся с оператором', callback_data='call_with_operator_about_0'))
    keyboard.insert(InlineKeyboardButton('Корзинка', callback_data='basket'))
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
    user = Users(db).get_all_information_user_id(user_id)

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


def get_services_menu(service_number: int, max_service_number: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)

    if not service_number == 0:
        keyboard.insert(InlineKeyboardButton('<', callback_data=f'watch_service_{service_number - 1}'))

    keyboard.insert(InlineKeyboardButton('связатся с оператором', callback_data=f'call_with_operator_about_{service_number}'))

    if not service_number == max_service_number:
        keyboard.insert(InlineKeyboardButton('>', callback_data=f'watch_service_{service_number + 1}'))

    keyboard.add(InlineKeyboardButton('Добавить в корзину', callback_data='add_to_basket_service'))

    return keyboard


def get_event_menu(event_number: int, max_event_number: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)

    if not event_number == 0:
        keyboard.insert(InlineKeyboardButton('<', callback_data=f'watch_event_{event_number - 1}'))

    if not event_number == max_event_number:
        keyboard.insert(InlineKeyboardButton('>', callback_data=f'watch_event_{event_number + 1}'))

    return keyboard
