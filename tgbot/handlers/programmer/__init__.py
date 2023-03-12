from aiogram.dispatcher import Dispatcher
from .get_work import register_get_work_handler


def register_programmer(dp: Dispatcher) -> None:
    register_get_work_handler(dp)
