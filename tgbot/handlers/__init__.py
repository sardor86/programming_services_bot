from aiogram.dispatcher import Dispatcher

from tgbot.handlers.users import register_user


def register_all_handlers(dp: Dispatcher) -> None:
    register_user(dp)
