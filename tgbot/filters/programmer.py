import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import Config
from tgbot.models import Users


class ProgrammerFilter(BoundFilter):
    key = 'is_programmer'

    def __init__(self, is_programmer: typing.Optional[bool] = None):
        self.is_programmer = is_programmer

    async def check(self, obj):
        if self.is_programmer is None:
            return False

        users = Users()

        return await users.check_programmer(obj.bot.from_user.id) == self.is_programmer
