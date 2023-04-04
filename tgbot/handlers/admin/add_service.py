from aiogram.types import Message
from aiogram.dispatcher import FSMContext, Dispatcher

import logging

from tgbot.misc import AddService
from tgbot.models import Services


logger = logging.getLogger(__name__)


async def get_photo(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    logger.info('save photo id in memory')

    await message.reply('Введите текст')

    logger.info('set get_text state in AddService')
    await AddService.get_text.set()


async def get_not_photo(message: Message) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.warning('This is not photo')
    await message.reply('Это не фото')


async def get_text(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    async with state.proxy() as data:
        photo = data['photo']

    logger.info('get photo')

    text = message.text
    logger.info('get text')

    services_id = await Services().create_service(photo, text)
    logger.info('create event')

    await message.reply(f'Создана новая услуга id: {services_id}')

    logger.info('finish add services state')
    await state.finish()


async def get_not_text(message: Message) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.warning('This is not text')
    await message.reply('Это не текст')


def register_add_service_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register get photo function handler for events')
    dp.register_message_handler(get_photo,
                                content_types=['photo'],
                                state=AddService.get_photo,
                                is_admin=True)

    logger.info('register get not photo function handler for events')
    dp.register_message_handler(get_not_photo,
                                lambda message: not message.photo,
                                state=AddService.get_photo,
                                is_admin=True)

    logger.info('register get text function handler for events')
    dp.register_message_handler(get_text,
                                content_types=['text'],
                                state=AddService.get_text,
                                is_admin=True)

    logger.info('register get not text function handler for events')
    dp.register_message_handler(get_text,
                                lambda message: not message.text,
                                state=AddService.get_text,
                                is_admin=True)
