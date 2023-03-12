from aiogram.types import CallbackQuery
from aiogram.dispatcher import Dispatcher

from tgbot.models import ProgrammerWork
from tgbot.keyboards import programmer_menu
from tgbot.misc import EndProject

import logging

logger = logging.getLogger(__name__)


async def programmers_menu(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get programmer menu')
    await callback.message.edit_text('Выберите действие',
                                     reply_markup=programmer_menu(ProgrammerWork(callback.bot.get('config').db),
                                                                  callback.from_user.id))


async def come_in_programmers_group(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get programmers group id')
    programmers_group_id = callback.bot.get('config').id_group.programmer_id

    logger.info('get programmers group link')
    programmers_group_link = await callback.bot.export_chat_invite_link(programmers_group_id)

    await callback.message.edit_text(f'Зайдите в группу программистов: {programmers_group_link}')


async def end_project(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get github project links')
    await callback.message.edit_text('Отправте github сылку')

    await EndProject.get_github_project_link.set()


def register_programmer_menu_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register programmer menu handler')
    dp.register_callback_query_handler(programmers_menu,
                                       lambda callback: callback.data == 'programmer_menu',
                                       state='*')

    logger.info('register handler to come in programmers group')
    dp.register_callback_query_handler(come_in_programmers_group,
                                       lambda callback: callback.data == 'come_in_programmers_group',
                                       state='*')

    logger.info('register end project handler for programmer')
    dp.register_callback_query_handler(end_project,
                                       lambda callback: callback.data == 'end_project')
