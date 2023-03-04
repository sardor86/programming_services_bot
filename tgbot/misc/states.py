from aiogram.dispatcher.filters.state import StatesGroup, State


class UpPrivilegeUsers(StatesGroup):
    choice_tip_user = State()
    choice_user_id = State()


class DownPrivilegeUsers(StatesGroup):
    choice_tip_user = State()
    choice_user_id = State()


class AddEvent(StatesGroup):
    get_photo = State()
    get_text = State()


class DeleteEvent(StatesGroup):
    get_event_id = State()


class AddService(StatesGroup):
    get_photo = State()
    get_text = State()
