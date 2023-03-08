from aiogram.dispatcher import Dispatcher
from .menu import register_operator_menu_handler


def register_operator(dp: Dispatcher) -> None:
    register_operator_menu_handler(dp)
