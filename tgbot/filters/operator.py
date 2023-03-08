import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.models import Users


class OperatorFilter(BoundFilter):
    key = 'is_operator'

    def __init__(self, is_operator: typing.Optional[bool] = None):
        self.is_operator = is_operator

    async def check(self, obj):
        if self.is_operator is None:
            return False
        
        users = Users(obj.bot.get('config').db)

        return users.check_operator(obj.from_user.id) == self.is_operator


class OperatorGroupFilter(BoundFilter):
    key = 'in_operators_group'

    def __init__(self, in_group: typing.Optional[bool] = None):
        self.in_group = in_group

    async def check(self, obj) -> bool:
        if not self.in_group:
            return True

        users = Users(obj.bot.get('config').db)

        if users.check_operator(obj.from_user.id) is False:
            operator_group_id = obj.bot.get('config').id_group.operator_id
            await obj.bot.kick_chat_member(operator_group_id, obj.from_user.id)
            return False

        if obj.message.chat.id == obj.bot.get('config').id_group.operator_id:
            return True
