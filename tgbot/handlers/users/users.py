from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

import logging

from tgbot.keyboards import choice_menu, user_menu

from tgbot.models.users import Users

logger = logging.getLogger(__name__)


async def start_user(message: Message) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Command start')

    await message.reply(f'Приветствуем {message.from_user.username}\n'
                        f'вы здесь можете купить услуги по программированию',
                        reply_markup=user_menu())

    logger.info('Register new user')
    Users(message.bot.get('config').db).add_users(message.from_user.id,
                                                  message.from_user.username,
                                                  message.from_user.full_name)


async def help_user(message: Message) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Command help')

    await message.reply('Вы в этом боте можете покупать услуги по программированию')


async def choice_privileged_user_menu(message: Message) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('get menu')

    await message.reply(f'Выберите пользователя',
                        reply_markup=choice_menu(message.bot.get('config').db, message.from_user.id))


def register_user(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Register user handler')

    logger.info('Register start function handler')
    dp.register_message_handler(start_user, commands='start', state='*', privileged_users=False)

    logger.info('Register help function handler')
    dp.register_message_handler(help_user, commands='help', state='*', privileged_users=False)

    logger.info('Register privileged user menu function handler')
    dp.register_message_handler(choice_privileged_user_menu, commands='menu', state='*', privileged_users=True)
