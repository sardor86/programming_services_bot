import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import Config
from tgbot.models.users import Users


class OperatorFilter(BoundFilter):
    key = 'is_operator'

    def __init__(self, is_operator: typing.Optional[bool] = None):
        self.is_operator = is_operator

    async def check(self, obj):
        if self.is_operator is None:
            return False
        config: Config = obj.bot.get('config')
        users = Users(config.db)

        return users.check_programmer(obj.bot.from_user.id) == self.is_operator
