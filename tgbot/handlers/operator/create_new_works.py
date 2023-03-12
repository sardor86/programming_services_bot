from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import Message

import logging

from tgbot.misc import CreateNewWorkForProgrammer
from tgbot.keyboards import get_work
from tgbot.models import Users

logger = logging.getLogger(__name__)


async def get_phone_number(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('check phone number')
    if not message.text.isdigit():
        await message.reply('Это не телефонный номер')
        await state.finish()
        return None

    logger.info('check phone number in db')
    if not Users(message.bot.get('config').db).check_phone_number_user_in_db(int(message.text)):
        await message.reply('Этого номера не существует в базе данных')

    logger.info('save phone number to member')
    async with state.proxy() as data:
        data['phone_number'] = int(message.text)

    await message.reply('А теперь отправте нам тз файл')

    logger.info('next step to create new work for programmer')
    await CreateNewWorkForProgrammer.get_tz_file.set()


async def get_file(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get phone number in member')
    async with state.proxy() as data:
        phone_number = data['phone_number']

    logger.info('send work to programmer group')
    await message.bot.send_document(message.bot.get('config').id_group.programmer_id,
                                    message.document.file_id,
                                    caption=f'Телефон покупателя: {phone_number}',
                                    reply_markup=get_work(phone_number))

    logger.info('end create a new work for programmer')
    await state.finish()


async def get_not_file(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get not file for tz')
    await message.reply('Это не тз файл')

    logger.info('end create new work for programmer')
    await state.finish()


def register_create_new_works_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register message handler to get client phone number to create a new work for programmer')
    dp.register_message_handler(get_phone_number,
                                state=CreateNewWorkForProgrammer.get_phone_number)

    logger.info('register message handler to get file to create a new work for programmer')
    dp.register_message_handler(get_file,
                                content_types=['document'],
                                state=CreateNewWorkForProgrammer.get_tz_file)

    logger.info('register message handler to get not file to create a new work for programmer')
    dp.register_message_handler(get_not_file,
                                state=CreateNewWorkForProgrammer.get_tz_file)
