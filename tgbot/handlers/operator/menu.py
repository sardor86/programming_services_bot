from aiogram.types import CallbackQuery
from aiogram.dispatcher import Dispatcher
import logging

from tgbot.keyboards import operator_menu
from tgbot.misc import GetTZFile

logger = logging.getLogger(__name__)


async def operators_menu(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('operators_menu')
    await callback.message.edit_text('Выберите дйствие',
                                     reply_markup=operator_menu())


async def come_in_operators_group(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get operators group id')
    operator_group_id = callback.bot.get('config').id_group.operator_id
    logger.info('get operators group link')
    operator_group_link = await callback.bot.export_chat_invite_link(operator_group_id)
    await callback.message.edit_text(f'Зайдите в группу опараторов: {operator_group_link}')


async def create_new_works_for_programmer(callback: CallbackQuery) -> None:
    await GetTZFile.get_tz_file.set()

    await callback.message.edit_text('Отправте нам тз файл для программиста')


def register_operator_menu_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register operator menu')
    dp.register_callback_query_handler(operators_menu,
                                       lambda callback: callback.data == 'operator_menu',
                                       is_operator=True,
                                       state='*')

    logger.info('register handler for operator to create a new works for programmer')
    dp.register_callback_query_handler(create_new_works_for_programmer,
                                       lambda callback: callback.data == 'create_new_work_for_programmer',
                                       is_operator=True,
                                       state='*')

    logger.info('register come in operators group handler')
    dp.register_callback_query_handler(come_in_operators_group,
                                       lambda callback: callback.data == 'come_in_operators_group',
                                       is_operator=True,
                                       state='*')
