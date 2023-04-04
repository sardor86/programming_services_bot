from tgbot.config import gino_db


class Base:
    def __init__(self):
        self.db = gino_db

    async def __aexit__(self, *excinfo):
        await self.db.pop_bind()


async def create_all_db():
    await gino_db.gino.create_all()
