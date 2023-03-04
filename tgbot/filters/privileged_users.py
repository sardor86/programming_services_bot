import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import Config
from tgbot.models import Users


class PrivilegedUsersFilter(BoundFilter):
    key = 'privileged_users'

    def __init__(self, privileged_users: typing.Optional[bool] = None):
        self.privileged_users = privileged_users

    async def check(self, obj):
        if self.privileged_users is None:
            return False
        if not self.privileged_users:
            return True

        config: Config = obj.bot.get('config')
        user = Users(config.db).get_all_information_user(obj.from_user.id)

        if user.rights_admin or user.rights_programmer or user.rights_operator:
            return True
        return False
