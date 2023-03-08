from aiogram.types import Message
from aiogram.dispatcher import FSMContext, Dispatcher

import logging

from tgbot.misc import DeleteEvent
from tgbot.models import Events


logger = logging.getLogger(__name__)


async def get_id_event(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.warning('This is not number')
    if not message.text.isdigit():
        await message.reply('Это не id')
        return None

    logger.info('delete event')
    if not Events(message.bot.get('config').db).delete_event(int(message.text)):
        logger.info('dont find event in db')
        await message.reply('Мы не смогли найти это событье')
        return None

    await message.reply('Событие удалено')

    logger.info('finish delete event state')
    await state.finish()


def register_delete_event_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register get event id function handler for events')
    dp.register_message_handler(get_id_event,
                                content_types=['text'],
                                state=DeleteEvent.get_event_id,
                                is_admin=True)
