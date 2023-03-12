import sqlalchemy as db
from sqlalchemy import Column, Integer, BigInteger
from sqlalchemy.orm import declarative_base, Session

from tgbot.config import DataBase

Base = declarative_base()


class ProgrammerWorkTable(Base):
    __tablename__ = 'programmer_works'

    id = Column(Integer(), primary_key=True)
    programmer_id = Column(Integer())
    client_phone_number = Column(BigInteger())

    def __str__(self) -> str:
        return f'<Programmer_works {self.id}>'

    def __repr__(self) -> str:
        return f'<Programmer_works {self.id}>'


class ProgrammerWork:
    def __init__(self, data_base: DataBase) -> None:
        self.engine = db.create_engine(f'postgresql://{data_base.user}:'
                                       f'{data_base.password}@'
                                       f'{data_base.host}:5432/'
                                       f'{data_base.data_base}')
        self.conn = self.engine.connect()
        self.session = Session(bind=self.engine)

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def create_work(self, programmer_id: int, client_phone_number: int) -> None:
        self.session.add(ProgrammerWorkTable(
            programmer_id=programmer_id,
            client_phone_number=client_phone_number
        ))
        self.session.commit()

    def check_work(self, client_phone_number: int, programmer_id: int) -> bool:
        return not self.session.query(ProgrammerWorkTable).filter(ProgrammerWorkTable.client_phone_number == client_phone_number,
                                                                  ProgrammerWorkTable.programmer_id == programmer_id) is None

    def delete_work(self, client_phone_number: int, programmer_id: int) -> bool:
        if self.check_work(client_phone_number, programmer_id):
            self.session.delete(self.session.query(ProgrammerWorkTable).filter(ProgrammerWorkTable.client_phone_number == client_phone_number,
                                                                               ProgrammerWorkTable.programmer_id == programmer_id).first())
            self.session.commit()
            return True
        return False

    def check_have_work(self, programmer_id: int) -> bool:
        return not self.session.query(ProgrammerWorkTable).filter(ProgrammerWorkTable.programmer_id == programmer_id).first() is None

    def get_work(self, programmer_id) -> ProgrammerWorkTable:
        return self.session.query(ProgrammerWorkTable).filter(ProgrammerWorkTable.programmer_id == programmer_id).first()
