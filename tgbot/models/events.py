from tgbot.config import gino_db
from .base import Base


class Events(Base):
    class EventsTable(gino_db.Model):
        __tablename__ = 'events'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        img = gino_db.Column(gino_db.String(255), nullable=False)
        text = gino_db.Column(gino_db.String(1024), default='')

        def __str__(self) -> str:
            return f'<Event {self.id}>'

        def __repr__(self) -> str:
            return f'<Event {self.id}>'

    async def create_event(self, img: str, text: str) -> int:
        event = self.EventsTable(img=img,
                                 text=text)
        await event.create()

        return event.id

    async def check_event(self, event_id: int) -> bool:
        return not await self.EventsTable.query.where(self.EventsTable.id == event_id).gino.first() is None

    async def delete_event(self, event_id: int) -> bool:
        if await self.check_event(event_id):
            event = await self.EventsTable.query.where(self.EventsTable.id == event_id).gino.first()
            await event.delete()
            return True
        return False

    async def get_all_event(self) -> list:
        return await self.EventsTable.query.gino.all()

    async def get_event(self, event_id: int) -> EventsTable:
        return self.EventsTable.query.where(self.EventsTable.id == event_id).gino.first()
