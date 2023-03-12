from aiogram.dispatcher import Dispatcher

from .users import register_all_user_handler
from .admin import register_admin
from .operator import register_operator
from .programmer import register_programmer


def register_all_handlers(dp: Dispatcher) -> None:
    register_all_user_handler(dp)
    register_admin(dp)
    register_operator(dp)
    register_programmer(dp)
