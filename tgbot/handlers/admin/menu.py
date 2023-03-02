from aiogram.types import CallbackQuery
from aiogram.dispatcher import Dispatcher
import logging

from tgbot.keyboards.inline import admin_menu, admin_choice_tip_user
from tgbot.misc.states import UpPrivilegeUsers, DownPrivilegeUsers

logger = logging.getLogger(__name__)


async def menu_admin(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Admin menu')

    await callback.message.edit_text('Выберите действие', reply_markup=admin_menu())


async def up_privilege_user(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('set choice_tip_user in UpPrivilegeUsers')
    await UpPrivilegeUsers.choice_tip_user.set()

    await callback.message.edit_text('Выберите тип пользователя', reply_markup=admin_choice_tip_user())


async def down_privilege_user(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('set choice_tip_user in DownPrivilegeUsers')
    await DownPrivilegeUsers.choice_tip_user.set()

    await callback.message.edit_text('Выберите тип пользователя', reply_markup=admin_choice_tip_user())


def register_menu_handlers(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register admin menu handler')
    dp.register_callback_query_handler(menu_admin,
                                       lambda callback: callback.data == 'admin_menu',
                                       state='*',
                                       is_admin=True)

    logger.info('register up user privilege for admin handler')
    dp.register_callback_query_handler(up_privilege_user,
                                       lambda callback: callback.data == 'up_user_admin',
                                       state='*',
                                       is_admin=True)

    logger.info('register DOWN user privilege for admin handler')
    dp.register_callback_query_handler(down_privilege_user,
                                       lambda callback: callback.data == 'down_user_admin',
                                       state='*',
                                       is_admin=True)
