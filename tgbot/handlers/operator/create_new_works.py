from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import Message

import logging

from tgbot.misc import GetTZFile
from tgbot.keyboards import get_work

logger = logging.getLogger(__name__)


async def get_file(message: Message, state: FSMContext):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    await state.finish()

    logger.info('send work to programmer group')
    await message.bot.send_document(message.bot.get('config').id_group.programmer_id,
                                    message.document.file_id,
                                    reply_markup=get_work(message.from_user.id))


def register_create_new_works_handler(dp: Dispatcher) -> None:
    dp.register_message_handler(get_file,
                                content_types=['document'],
                                state=GetTZFile)
