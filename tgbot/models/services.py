from tgbot.config import gino_db
from .base import Base


class Services:
    class ServicesTable(gino_db.Model):
        __tablename__ = 'services'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        img = gino_db.Column(gino_db.String(255), nullable=False)
        text = gino_db.Column(gino_db.String(1024), default='')

        def __str__(self) -> str:
            return f'<Services {self.id}>'

        def __repr__(self) -> str:
            return f'<Services {self.id}>'

    async def create_service(self, img: str, text: str) -> int:
        event = self.ServicesTable(img=img,
                                   text=text)
        await event.create()
        return event.id

    async def check_service(self, service_id: int) -> bool:
        return not await self.ServicesTable.query().where(self.ServicesTable.id == service_id).gino.first() is None

    async def delete_service(self, service_id: int) -> bool:
        if await self.check_service(service_id):
            service = await self.ServicesTable.query().where(self.ServicesTable.id == service_id).gino.first()
            await service.delete()
            return True
        return False

    async def get_all_service(self) -> list:
        return await self.ServicesTable.query().gino.all()

    async def get_service(self, service_id: int) -> ServicesTable:
        return await self.ServicesTable.query().where(self.ServicesTable.id == service_id).gino.first()
