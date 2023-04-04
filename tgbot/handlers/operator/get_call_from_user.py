from aiogram.types import CallbackQuery
from aiogram.dispatcher import Dispatcher

from tgbot.models import Services, Users

import logging

logger = logging.getLogger(__name__)


async def get_call_from_user(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get service')
    service = await Services().get_all_service()[int(callback.data.split('_')[-1])]

    logger.info('get information user')
    user = await Users().get_all_information_user_id(callback.from_user.id)

    logger.info('send call from operators group')
    await callback.bot.send_photo(callback.bot.get('config').id_group.operator_id,
                                  photo=service.img,
                                  caption=service.text + '\n========================\n'
                                                         f'имя пользователя: {callback.from_user.full_name}\n'
                                                         f'Телефонный номер: +{user.phone_number}\n')


def register_get_call_from_user_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register get call from user handler')
    dp.register_callback_query_handler(get_call_from_user,
                                       lambda callback: callback.data[:24] == 'call_with_operator_about')
