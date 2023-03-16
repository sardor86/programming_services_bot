import sqlalchemy as db
from sqlalchemy import Column, Integer, BigInteger
from sqlalchemy.orm import declarative_base, Session

from tgbot.models import Services
from tgbot.config import DataBase

Base = declarative_base()


class BasketTable(Base):
    __tablename__ = 'baskets'

    id = Column(Integer(), primary_key=True)
    user_id = Column(BigInteger())
    service_id = Column(Integer())

    def __str__(self) -> str:
        return f'<User {self.user_id}>'

    def __repr__(self) -> str:
        return f'<User {self.user_id}>'


class Baskets:
    def __init__(self, data_base: DataBase) -> None:
        self.data_base = data_base
        self.engine = db.create_engine(f'postgresql://{data_base.user}:'
                                       f'{data_base.password}@'
                                       f'{data_base.host}:5432/'
                                       f'{data_base.data_base}')
        self.conn = self.engine.connect()
        self.session = Session(bind=self.engine)

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def check_service_in_basket(self, user_id: int, service_id: int) -> bool:
        all_service_in_basket = self.session.query(BasketTable).filter(BasketTable.user_id == user_id).all()

        for service in all_service_in_basket:
            return service.id == service_id
        return False

    def create_service_in_basket(self, user_id: int, service_id: int) -> bool:
        self.session.add(BasketTable(user_id=user_id,
                                     service_id=service_id))
        self.session.commit()
        return True

    def check_service(self, service_id: int) -> bool:
        if not Services(self.data_base).check_service(service_id):
            self.session.delete(self.session.query(BasketTable).filter(BasketTable.service_id == service_id).all)
            return False
        return True

    def get_all_service_in_basket(self, user_id: int) -> list:
        all_services = self.session.query(BasketTable).filter(BasketTable.user_id == user_id).all()

        services = []
        for service in all_services:
            self.check_service(service.service_id)
            services.append(service)
        return services

    def delete_service_in_basket(self, user_id: int, service_id) -> bool:
        if self.check_service_in_basket(user_id, service_id):
            self.session.delete(self.session.query(BasketTable).filter(BasketTable.user_id == user_id,
                                                                       BasketTable.service_id == service_id).first())
            return True
        return False
