from aiogram.dispatcher import Dispatcher

from .users import register_user
from .registrer_user import register_user_registration_handler


def register_all_user_handler(dp: Dispatcher) -> None:
    register_user(dp)
    register_user_registration_handler(dp)

