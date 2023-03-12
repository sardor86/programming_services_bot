from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery

import logging

from tgbot.keyboards import choice_menu, user_menu, get_services_menu, get_event_menu, register_user_menu

from tgbot.models import Users, \
                         Services, ServicesTable, \
                         Events, EventsTable,\
                         ProgrammerWork

from tgbot.misc import RegisterUser

logger = logging.getLogger(__name__)


async def start_user(message: Message) -> None:

    user_info = Users(message.bot.get('config').db).get_all_information_user_id(message.from_user.id)

    if user_info is None:
        await RegisterUser.get_phone_number.set()

        await message.reply('Чтобы зарегестрироватся надо отправить свой номер телефона',
                            reply_markup=register_user_menu())
    else:
        await message.reply(f'Приветствуем {message.from_user.username}\n'
                            f'вы здесь можете купить услуги по программированию',
                            reply_markup=user_menu())


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


async def get_service(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('delete old service menu')
    await callback.message.delete()

    logger.info('get service number')
    service_number = int(callback.data.split('_')[-1])

    logger.info('get services list')
    services = Services(callback.bot.get('config').db).get_all_service()

    logger.info('get service')
    service: ServicesTable = services[service_number]

    logger.info('send service')
    await callback.bot.send_photo(callback.from_user.id,
                                  service.img,
                                  caption=service.text,
                                  reply_markup=get_services_menu(service_number, len(services) - 1))


async def get_event(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('delete old event')
    await callback.message.delete()

    logger.info('get event number')
    event_number = int(callback.data.split('_')[-1])

    logger.info('get events list')
    events = Events(callback.bot.get('config').db).get_all_event()

    logger.info('get event')
    event: EventsTable = events[event_number]

    logger.info('send event')
    await callback.bot.send_photo(callback.from_user.id,
                                  event.img,
                                  caption=event.text,
                                  reply_markup=get_event_menu(event_number, len(events) - 1))


async def complete_work(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get client phone number')
    client_phone_number = Users(callback.bot.get('config').db).get_all_information_user_id(callback.from_user.id).phone_number

    logger.info('delete work in db')
    ProgrammerWork(callback.bot.get('config').db).delete_work(client_phone_number, int(callback.data.split('_')[-1]))

    await callback.message.edit_text('Проект выполнен')
    await callback.bot.send_message(callback.data.split('_')[-1], 'Проект выполнен')


def register_user(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('Register user handler')

    logger.info('Register start function handler')
    dp.register_message_handler(start_user,
                                commands='start',
                                state='*',
                                privileged_users=False)

    logger.info('Register help function handler')
    dp.register_message_handler(help_user,
                                commands='help',
                                state='*',
                                privileged_users=False)

    logger.info('Register privileged user menu function handler')
    dp.register_message_handler(choice_privileged_user_menu,
                                commands='menu',
                                state='*',
                                privileged_users=True,
                                in_group=False)

    logger.info('register service menu handler')
    dp.register_callback_query_handler(get_service,
                                       lambda callback: callback.data[:13] == 'watch_service')

    logger.info('register event menu handler')
    dp.register_callback_query_handler(get_event,
                                       lambda callback: callback.data[:11] == 'watch_event')

    logger.info('register complete project handler')
    dp.register_callback_query_handler(complete_work,
                                       lambda callback: callback.data[:14] == 'completed_work',
                                       state='*')
