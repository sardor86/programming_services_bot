from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery

from tgbot.models import ProgrammerWork

import logging

logger = logging.getLogger(__name__)


async def get_work(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('delete old message')
    await callback.message.delete()

    logger.info('check programmer have work')
    if ProgrammerWork(callback.bot.get('config').db).check_have_work(callback.from_user.id):
        await callback.bot.send_message(callback.from_user.id, 'Вы имеете работу')
        return None

    logger.info('programmer get a new work')
    ProgrammerWork(callback.bot.get('config').db).create_work(callback.from_user.id,
                                                              int(callback.data.split('_')[-1]))
    await callback.bot.send_message(callback.from_user.id, 'Вы получили новую работу')


def register_get_work_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register get work handler')
    dp.register_callback_query_handler(get_work,
                                       lambda callback: callback.data[:13] == 'get_work_from')
