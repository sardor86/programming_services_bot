import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

from tgbot.config import DataBase

Base = declarative_base()


class ServicesTable(Base):
    __tablename__ = 'services'

    id = Column(Integer(), primary_key=True)
    img = Column(String(255), nullable=False)
    text = Column(String(1024), default='')

    def __str__(self) -> str:
        return f'<Services {self.id}>'

    def __repr__(self) -> str:
        return f'<Services {self.id}>'


class Services:
    def __init__(self, data_base: DataBase) -> None:
        self.engine = db.create_engine(f'postgresql://{data_base.user}:'
                                       f'{data_base.password}@'
                                       f'{data_base.host}:5432/'
                                       f'{data_base.data_base}')
        self.conn = self.engine.connect()
        self.session = Session(bind=self.engine)

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def create_service(self, img: str, text: str) -> int:
        event = ServicesTable(img=img,
                              text=text)
        self.session.add(event)
        self.session.commit()
        return self.session.query(ServicesTable).all()[-1].id

    def check_service(self, service_id: int) -> bool:
        return not self.session.query(ServicesTable).filter(ServicesTable.id == service_id).first() is None

    def delete_service(self, service_id: int) -> bool:
        if self.check_service(service_id):
            self.session.delete(self.session.query(ServicesTable).filter(ServicesTable.id == service_id).first())
            self.session.commit()
            return True
        return False

    def get_all_service(self) -> list:
        return self.session.query(ServicesTable).all()

    def get_service(self, service_id: int) -> ServicesTable:
        return self.session.query(ServicesTable).filter(ServicesTable.id == service_id).first()
