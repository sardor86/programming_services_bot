import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

from tgbot.config import DataBase

Base = declarative_base()


class EventsTable(Base):
    __tablename__ = 'events'

    id = Column(Integer(), primary_key=True)
    img = Column(String(255), nullable=False)
    text = Column(String(1024), default='')

    def __str__(self) -> str:
        return f'<Event {self.id}>'

    def __repr__(self) -> str:
        return f'<Event {self.id}>'


class Events:
    def __init__(self, data_base: DataBase) -> None:
        self.engine = db.create_engine(f'postgresql://{data_base.user}:'
                                       f'{data_base.password}@'
                                       f'{data_base.host}:5432/'
                                       f'{data_base.data_base}')
        self.conn = self.engine.connect()
        self.session = Session(bind=self.engine)

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def create_event(self, img: str, text: str) -> int:
        event = EventsTable(img=img,
                            text=text)
        self.session.add(event)
        self.session.commit()
        return self.session.query(EventsTable).all()[-1].id

    def check_event(self, event_id: int) -> bool:
        return not self.session.query(EventsTable).filter(EventsTable.id == event_id).first() is None

    def delete_event(self, event_id: int) -> bool:
        if self.check_event(event_id):
            self.session.delete(self.session.query(EventsTable).filter(EventsTable.id == event_id).first())
            self.session.commit()
            return True
        return False

    def get_all_event(self) -> list:
        return self.session.query(EventsTable).all()

    def get_event(self, event_id: int) -> EventsTable:
        return self.session.query(EventsTable).filter(EventsTable.id == event_id).first()
