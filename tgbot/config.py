from dataclasses import dataclass

from environs import Env


@dataclass
class DataBase:
    host: str
    user: str
    password: str


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    db: DataBase
    bot: TgBot


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        db=DataBase(
            host=env.str('DB_HOST'),
            user=env.str('DB_USER'),
            password=env.str('DB_PASSWORD')
        ),
        bot=TgBot(
            token=env.str('BOT_TOKEN')
        )
    )


print(load_config('.env').bot.token)
