from tgbot.models.users import Users, UsersTable
from tgbot.config import DataBase


def create_all_db(db: DataBase):
    Users(db).create_db()
