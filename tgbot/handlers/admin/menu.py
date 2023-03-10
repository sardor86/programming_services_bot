from aiogram.types import CallbackQuery
from aiogram.dispatcher import Dispatcher
import logging

from tgbot.keyboards import admin_menu, admin_choice_tip_user
from tgbot.misc import UpPrivilegeUsers, DownPrivilegeUsers, \
                       AddEvent, DeleteEvent, \
                       AddService, DeleteService

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


async def add_new_event(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    await callback.message.edit_text('Отправьте нам фото')

    logger.info('Set get_phone in AddEvent')
    await AddEvent.get_photo.set()


async def delete_event(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    await callback.message.edit_text('Введите id события')

    logger.info('set get event id in DeleteEvent')
    await DeleteEvent.get_event_id.set()


async def add_new_service(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    await callback.message.edit_text('Отправьте нам фото')

    logger.info('set get photo in AddService')
    await AddService.get_photo.set()


async def delete_service(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    await callback.message.edit_text('Отправьте нам id услуги')

    logger.info('set get service id in DeleteService')
    await DeleteService.get_service_id.set()


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

    logger.info('register down user privilege for admin handler')
    dp.register_callback_query_handler(down_privilege_user,
                                       lambda callback: callback.data == 'down_user_admin',
                                       state='*',
                                       is_admin=True)

    logger.info('register add event for admin handler')
    dp.register_callback_query_handler(add_new_event,
                                       lambda callback: callback.data == 'add_event_admin',
                                       state='*',
                                       is_admin=True)

    logger.info('register delete event for admin handler')
    dp.register_callback_query_handler(delete_event,
                                       lambda callback: callback.data == 'delete_event_admin',
                                       state='*',
                                       is_admin=True)

    logger.info('register add service for admin handler')
    dp.register_callback_query_handler(add_new_service,
                                       lambda callback: callback.data == 'add_service_admin',
                                       state='*',
                                       is_admin=True)

    logger.info('register delete service for admin handler')
    dp.register_callback_query_handler(delete_service,
                                       lambda callback: callback.data == 'delete_service_admin',
                                       state='*',
                                       is_admin=True)
