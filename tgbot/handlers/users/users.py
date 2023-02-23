from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
import logging

logger = logging.getLogger(__name__)


async def start_user(message: Message) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Command start')

    await message.reply(f'Приветствуем {message.from_user.username}\n'
                        f'вы здесь можете купить услуги по программированию')


async def help_user(message: Message) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Command help')

    await message.reply('Вы в этом боте можете покупать услуги по программированию')


def register_user(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Register user handler')

    dp.register_message_handler(start_user, commands='start', state='*')
    dp.register_message_handler(help_user, commands='help', state='*')
