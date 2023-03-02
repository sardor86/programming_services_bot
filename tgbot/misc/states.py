from aiogram.dispatcher.filters.state import StatesGroup, State


class UpPrivilegeUsers(StatesGroup):
    choice_tip_user = State()
    choice_user_id = State()


class DownPrivilegeUsers(StatesGroup):
    choice_tip_user = State()
    choice_user_id = State()
