from aiogram.types import Message
from aiogram.dispatcher import FSMContext, Dispatcher

import logging

from tgbot.misc import DeleteService
from tgbot.models import Services


logger = logging.getLogger(__name__)


async def get_id_service(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.warning('This is not number')
    if not message.text.isdigit():
        await message.reply('Это не id')
        return None

    logger.info('delete service')
    if not Services(message.bot.get('config').db).delete_service(int(message.text)):
        logger.info('dont find service in db')
        await message.reply('Мы не смогли найти эту услугу')
        return None

    await message.reply('Услуга удалено')

    logger.info('finish delete service state')
    await state.finish()


def register_delete_service_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register get event id function handler for events')
    dp.register_message_handler(get_id_service,
                                content_types=['text'],
                                state=DeleteService.get_service_id)
