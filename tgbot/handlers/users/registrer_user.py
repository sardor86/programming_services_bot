from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

import logging

from tgbot.misc import RegisterUser
from tgbot.models import Users

logger = logging.getLogger(__name__)


async def register_user(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('add user in db')

    await Users().add_users(message.from_user.id,
                            message.from_user.username,
                            message.from_user.full_name,
                            int(message.contact.phone_number[1:]))

    await message.reply('Вы зарегестрировались', reply_markup=ReplyKeyboardRemove())
    await state.finish()


def register_user_registration_handler(dp: Dispatcher):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('register user registration handler')
    dp.register_message_handler(register_user,
                                content_types=['contact'],
                                state=RegisterUser.get_phone_number)
