from aiogram.dispatcher import Dispatcher

from .get_work import register_get_work_handler
from .menu import register_programmer_menu_handler


def register_programmer(dp: Dispatcher) -> None:
    register_get_work_handler(dp)
    register_programmer_menu_handler(dp)
