from aiogram.dispatcher import Dispatcher

from .menu import register_menu_handlers
from .up_privilege import register_up_privilege_handler


def register_admin(dp: Dispatcher) -> None:
    register_menu_handlers(dp)
    register_up_privilege_handler(dp)
