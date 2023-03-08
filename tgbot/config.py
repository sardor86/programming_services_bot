from dataclasses import dataclass

from environs import Env

import logging

logger = logging.getLogger(__name__)


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


def load_config(path: str = None) -> Config:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Get config')

    env = Env()
    env.read_env(path)

    return Config(
        db=DataBase(
            host=env.str('DB_HOST'),
            user=env.str('DB_USER'),
            password=env.str('DB_PASSWORD'),
            data_base=env.str('DB_DATA_BASE')
        ),
        bot=TgBot(
            token=env.str('BOT_TOKEN')
        ),
        id_group=IdGroup(
            operator_id=int(env.str('OPERATORS_GROUP_ID')),
            programmer_id=int(env.str('PROGRAMMER_GROUP_ID'))
        )
    )
