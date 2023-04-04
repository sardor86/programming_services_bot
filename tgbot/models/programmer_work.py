from tgbot.config import gino_db
from .base import Base


class ProgrammerWork(Base):
    class ProgrammerWorkTable(gino_db.Model):
        __tablename__ = 'programmer_works'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        programmer_id = gino_db.Column(gino_db.Integer())
        client_phone_number = gino_db.Column(gino_db.BigInteger())

        def __str__(self) -> str:
            return f'<Programmer_works {self.id}>'

        def __repr__(self) -> str:
            return f'<Programmer_works {self.id}>'

    async def create_work(self, programmer_id: int, client_phone_number: int) -> None:
        programmer_work = self.ProgrammerWorkTable(programmer_id=programmer_id,
                                                   client_phone_number=client_phone_number)
        await programmer_work.create()

    async def check_work(self, client_phone_number: int, programmer_id: int) -> bool:
        return not await self.ProgrammerWorkTable.query().where(self.ProgrammerWorkTable.client_phone_number == client_phone_number,
                                                                self.ProgrammerWorkTable.programmer_id == programmer_id).gino.firts() is None

    async def delete_work(self, client_phone_number: int, programmer_id: int) -> bool:
        if await self.check_work(client_phone_number, programmer_id):
            programmer_work = await self.ProgrammerWorkTable.query().where(self.ProgrammerWorkTable.client_phone_number == client_phone_number,
                                                                           self.ProgrammerWorkTable.programmer_id == programmer_id).gino.first()
            await programmer_work.delete()
            return True
        return False

    async def check_have_work(self, programmer_id: int) -> bool:
        return not await self.ProgrammerWorkTable.query().where(self.ProgrammerWorkTable.programmer_id == programmer_id).gino.first() is None

    async def get_work(self, programmer_id) -> ProgrammerWorkTable:
        return await self.ProgrammerWorkTable.query().where(self.ProgrammerWorkTable.programmer_id == programmer_id).gino.first()
