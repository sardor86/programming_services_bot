from .users import Users
from .events import Events
from tgbot.config import DataBase


def create_all_db(db: DataBase):
    Users(db).create_db()
    Events(db).create_db()
