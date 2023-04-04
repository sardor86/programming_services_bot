from tgbot.config import gino_db
from .base import Base


class Users:
    class UsersTable(gino_db.Model):
        __tablename__ = 'users'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        user_id = gino_db.Column(gino_db.BigInteger(), unique=True, nullable=False)
        user_name = gino_db.Column(gino_db.String())
        user_full_name = gino_db.Column(gino_db.String())
        phone_number = gino_db.Column(gino_db.BigInteger(), unique=True, nullable=False)
        rights_admin = gino_db.Column(gino_db.Boolean, default=False)
        rights_programmer = gino_db.Column(gino_db.Boolean, default=False)
        rights_operator = gino_db.Column(gino_db.Boolean, default=False)

        def __str__(self) -> str:
            return f'<User {self.user_id}>'

        def __repr__(self) -> str:
            return f'<User {self.user_id}>'

    async def add_users(self, user_id: int,
                        user_name: str,
                        user_full_name: str,
                        phone_number: int, /,
                        right_admin: bool = False,
                        right_programmer: bool = False,
                        right_operator: bool = False) -> bool:
        if not await self.check_in_db_user(user_id):
            user = self.UsersTable(user_id=user_id,
                                   user_name=user_name,
                                   user_full_name=user_full_name,
                                   phone_number=phone_number,
                                   rights_admin=right_admin,
                                   rights_programmer=right_programmer,
                                   rights_operator=right_operator
                                   )
            await user.create()
            return True
        else:
            return False

    async def check_in_db_user(self, user_id: int) -> bool:
        return not await self.UsersTable.query().where(self.UsersTable.user_id == user_id).gino.first() is None

    async def check_phone_number_user_in_db(self, phone_number: int) -> bool:
        return not await self.UsersTable.query().where(self.UsersTable.phone_number == phone_number).gino.first() is None

    async def get_all_information_user_id(self, user_id: int) -> UsersTable:
        return await self.UsersTable.query().where(self.UsersTable.user_id == user_id).gino.first()

    async def get_all_information_user_phone_number(self, phone_number: int) -> UsersTable:
        return await self.UsersTable.query().filter(self.UsersTable.phone_number == phone_number).gino.first()

    async def up_admin_right(self, phone_number: int) -> bool:
        user = await self.get_all_information_user_phone_number(phone_number)
        if user is None:
            return False
        else:
            user.update(rights_admin=True).apply()
            return True

    async def up_programmer_right(self, phone_number: int) -> bool:
        user = await self.get_all_information_user_phone_number(phone_number)
        if user is None:
            return False
        else:
            user.update(rights_programmer=True).apply()
            return True

    async def up_operator_right(self, phone_number: int) -> bool:
        user = await self.get_all_information_user_phone_number(phone_number)
        if user is None:
            return False
        else:
            user.update(rights_operator=True).apply()
            return True

    async def down_admin_right(self, phone_number: int) -> bool:
        user = await self.get_all_information_user_phone_number(phone_number)
        if user is None:
            return False
        else:
            user.update(rights_admin=False).apply()
            return True

    async def down_programmer_right(self, phone_number: int) -> bool:
        user = await self.get_all_information_user_phone_number(phone_number)
        if user is None:
            return False
        else:
            user.update(rights_programmer=False).apply()
            return True

    async def down_operator_right(self, phone_number: int) -> bool:
        user = await self.get_all_information_user_phone_number(phone_number)
        if user is None:
            return False
        else:
            user.update(rights_operator=False).apply()
            return True

    async def get_all_admin(self) -> list:
        return await self.UsersTable.query().where(self.UsersTable.rights_admin == True).gino.all()

    async def get_all_programmer(self) -> list:
        return await self.UsersTable.query().where(self.UsersTable.rights_programmer == True).gino.all()

    async def get_all_operator(self) -> list:
        return await self.UsersTable.query().where(self.UsersTable.rights_operator == True).gino.all()

    async def get_all_users(self) -> list:
        return self.UsersTable.query().where(self.UsersTable.rights_admin == False and
                                             self.UsersTable.rights_programmer == False and
                                             self.UsersTable.rights_operator == False).gino.all()

    async def check_admin(self, user_id: int) -> bool:
        return not self.UsersTable.query().where(self.UsersTable.rights_admin == True and
                                                 self.UsersTable.user_id == user_id).gino.first() is None

    async def check_programmer(self, user_id: int) -> bool:
        return not self.UsersTable.query().filter(self.UsersTable.rights_programmer == True and
                                                  self.UsersTable.user_id == user_id).gino.first() is None

    async def check_operator(self, user_id: int) -> bool:
        return not self.UsersTable.query().filter(self.UsersTable.rights_operator == True and
                                                  self.UsersTable.user_id == user_id).gino.first() is None
