from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterUser(StatesGroup):
    get_phone_number = State()


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


class DeleteService(StatesGroup):
    get_service_id = State()


class CreateNewWorkForProgrammer(StatesGroup):
    get_phone_number = State()
    get_tz_file = State()


class EndProject(StatesGroup):
    get_github_project_link = State()
