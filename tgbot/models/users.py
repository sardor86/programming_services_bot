import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, Session

from tgbot.config import DataBase

Base = declarative_base()


class UsersTable(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), unique=True, nullable=False)
    user_name = Column(String())
    user_full_name = Column(String())
    rights_admin = Column(Boolean, default=False)
    rights_programmer = Column(Boolean, default=False)
    rights_operator = Column(Boolean, default=False)

    def __str__(self) -> str:
        return f'<User {self.user_id}>'

    def __repr__(self) -> str:
        return f'<User {self.user_id}>'


class Users:
    def __init__(self, data_base: DataBase) -> None:
        self.engine = db.create_engine(f'postgresql://{data_base.user}:'
                                       f'{data_base.password}@'
                                       f'{data_base.host}:5432/'
                                       f'{data_base.data_base}')
        self.conn = self.engine.connect()
        self.session = Session(bind=self.engine)

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def add_users(self, user_id: int,
                  user_name: str,
                  user_full_name: str, /,
                  right_admin: bool = False,
                  right_programmer: bool = False,
                  right_operator: bool = False) -> bool:
        if not self.check_in_db_user(user_id):
            self.session.add(UsersTable(user_id=user_id,
                                        user_name=user_name,
                                        user_full_name=user_full_name,
                                        rights_admin=right_admin,
                                        rights_programmer=right_programmer,
                                        rights_operator=right_operator
                                        ))
            self.session.commit()
            return True
        else:
            return False

    def check_in_db_user(self, user_id: int) -> bool:
        return not self.session.query(UsersTable).filter(UsersTable.user_id == user_id).first() is None

    def get_all_information_user(self, user_id: int) -> UsersTable:
        return self.session.query(UsersTable).filter(UsersTable.user_id == user_id).first()

    def up_admin_right(self, user_id: int) -> bool:
        user = self.get_all_information_user(user_id)
        if user is None:
            return False
        else:
            user.rights_admin = True
            self.session.commit()
            return True

    def up_programmer_right(self, user_id: int) -> bool:
        user = self.get_all_information_user(user_id)
        if user is None:
            return False
        else:
            user.rights_programmer = True
            self.session.commit()
            return True

    def up_operator_right(self, user_id: int) -> bool:
        user = self.get_all_information_user(user_id)
        if user is None:
            return False
        else:
            user.rights_operator = True
            self.session.commit()
            return True

    def down_admin_right(self, user_id: int) -> bool:
        user = self.get_all_information_user(user_id)
        if user is None:
            return False
        else:
            user.rights_admin = False
            self.session.commit()
            return True

    def down_programmer_right(self, user_id: int) -> bool:
        user = self.get_all_information_user(user_id)
        if user is None:
            return False
        else:
            user.rights_programmer = False
            self.session.commit()
            return True

    def down_operator_right(self, user_id: int) -> bool:
        user = self.get_all_information_user(user_id)
        if user is None:
            return False
        else:
            user.rights_operator = False
            self.session.commit()
            return True

    def get_all_admin(self) -> list:
        return self.session.query(UsersTable).filter(UsersTable.rights_admin == True).all()

    def get_all_programmer(self) -> list:
        return self.session.query(UsersTable).filter(UsersTable.rights_programmer == True).all()

    def get_all_operator(self) -> list:
        return self.session.query(UsersTable).filter(UsersTable.rights_operator == True).all()

    def get_all_users(self) -> list:
        return self.session.query(UsersTable).filter(UsersTable.rights_admin == False and
                                                     UsersTable.rights_programmer == False and
                                                     UsersTable.rights_operator == False).all()
