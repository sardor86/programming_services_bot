from aiogram.types import CallbackQuery
from aiogram.dispatcher import Dispatcher
import logging

logger = logging.getLogger(__name__)


async def operator_menu(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get operators group id')
    operator_group_id = callback.bot.get('config').id_group.operator_id

    logger.info('get operators group link')
    operator_group_link = await callback.bot.export_chat_invite_link(operator_group_id)
    await callback.message.edit_text(f'Зайдите в группу опараторов: {operator_group_link}')


def register_operator_menu_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register operator menu')
    dp.register_callback_query_handler(operator_menu,
                                       lambda callback: callback.data == 'operator_menu',
                                       is_operator=True,
                                       state='*')
