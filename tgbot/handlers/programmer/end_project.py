from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import Message

from tgbot.models import ProgrammerWork, Users
from tgbot.keyboards import completed_work
from tgbot.misc import EndProject

import logging

logger = logging.getLogger(__name__)


async def get_github_project_links(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('check github link')
    if not message.text[:19] == 'https://github.com/':
        await message.reply('Это не github сылка')
        await state.finish()
        return None

    logger.info('get client phone number')
    phone_number_client = (await ProgrammerWork().get_work(message.from_user.id)).client_phone_number

    logger.info('get client id')
    client_id = (await Users().get_all_information_user_phone_number(phone_number_client)).user_id

    await message.bot.send_message(client_id,
                                   'Подтвердите пожалуйста что проект выполнен',
                                   reply_markup=completed_work(message.from_user.id))

    await state.finish()


def register_end_project_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register get github project link handler')
    dp.register_message_handler(get_github_project_links,
                                state=EndProject.get_github_project_link)
