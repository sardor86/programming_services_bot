from aiogram.dispatcher import Dispatcher

from tgbot.handlers.users import register_user
from tgbot.handlers.admin import register_admin


def register_all_handlers(dp: Dispatcher) -> None:
    register_user(dp)
    register_admin(dp)
