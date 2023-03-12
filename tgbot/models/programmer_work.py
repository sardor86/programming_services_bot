import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

from tgbot.config import DataBase

Base = declarative_base()


class ProgrammerWorkTable(Base):
    __tablename__ = 'programmer_works'

    id = Column(Integer(), primary_key=True)
    operator_id = Column(Integer(), nullable=False)
    programmer_id = Column(Integer())

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

    def create_work(self, operator_id: int, programmer_id: int) -> None:
        self.session.add(ProgrammerWorkTable(
            operator_id=operator_id,
            programmer_id=programmer_id
        ))
        self.session.commit()

    def check_work(self, operator_id: int, programmer_id: int) -> bool:
        return not self.session.query(ProgrammerWorkTable).filter(ProgrammerWorkTable.operator_id == operator_id,
                                                                  ProgrammerWorkTable.programmer_id == programmer_id) is None

    def delete_work(self, operator_id: int, programmer_id: int) -> bool:
        if self.check_work(operator_id, programmer_id):
            self.session.delete(self.session.query(ProgrammerWorkTable).filter(ProgrammerWorkTable.operator_id == operator_id,
                                                                               ProgrammerWorkTable.programmer_id == programmer_id).first())
            self.session.commit()
            return True
        return False

    def check_have_work(self, programmer_id) -> bool:
        return not self.session.query(ProgrammerWorkTable).filter(ProgrammerWorkTable.programmer_id == programmer_id).first() is None
