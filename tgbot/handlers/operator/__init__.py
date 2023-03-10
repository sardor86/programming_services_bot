from aiogram.dispatcher import Dispatcher

from .menu import register_operator_menu_handler
from .get_call_from_user import register_get_call_from_user_handler


def register_operator(dp: Dispatcher) -> None:
    register_operator_menu_handler(dp)
    register_get_call_from_user_handler(dp)
