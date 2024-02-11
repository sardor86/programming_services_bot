from dataclasses import dataclass
from environs import Env
import logging
from gino import Gino

logger = logging.getLogger(__name__)
gino_db = Gino()


@dataclass
class DataBase:
    host: str
    user: str
    password: str
    data_base: str


@dataclass
class TgBot:
    token: str


@dataclass
class IdGroup:
    operator_id: int
    programmer_id: int


@dataclass
class Config:
    db: DataBase
    bot: TgBot
    id_group: IdGroup


async def set_gino(data_base: DataBase) -> None:
    await gino_db.set_bind(f'postgresql://{data_base.user}:'
                           f'{data_base.password}@'
                           f'{data_base.host}:5432/'
                           f'{data_base.data_base}')


async def load_config(path: str = None) -> Config:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Get config')

    env = Env()
    env.read_env(path)

    config = Config(
        db=DataBase(
            host=env.str('DB_HOST'),
            user=env.str('POSTGRES_USER'),
            password=env.str('POSTGRES_PASSWORD'),
            data_base=env.str('POSTGRES_DB'),
        ),
        bot=TgBot(
            token=env.str('BOT_TOKEN')
        ),
        id_group=IdGroup(
            operator_id=int(env.str('OPERATORS_GROUP_ID')),
            programmer_id=int(env.str('PROGRAMMER_GROUP_ID'))
        )
    )

    await set_gino(config.db)
    return config
