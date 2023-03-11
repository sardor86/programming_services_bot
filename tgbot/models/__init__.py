from .users import Users, UsersTable
from .events import Events, EventsTable
from .services import Services, ServicesTable
from .programmer_work import ProgrammerWork, ProgrammerWorkTable

from tgbot.config import DataBase


def create_all_db(db: DataBase):
    Users(db).create_db()
    Events(db).create_db()
    Services(db).create_db()
