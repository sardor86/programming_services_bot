from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext, Dispatcher

import logging

from tgbot.misc import UpPrivilegeUsers
from tgbot.models import Users


logger = logging.getLogger(__name__)


async def choice_tip_user_admin(callback: CallbackQuery, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    async with state.proxy() as data:
        data['tip_user'] = callback.data[7:][:-4]

    logging.info('save choice tip user in memory')

    await callback.message.edit_text('Введите номер телефона пользователя без + например:\n'
                                     '998777777777')

    logging.info('set choice_user_id state in UpPrivilegeUsers')
    await UpPrivilegeUsers.choice_user_id.set()


async def get_id_user_admin(message: Message, state: FSMContext) -> None:
    logger.info('check phone number')
    if not message.text.isdigit():
        await message.reply('Вы вели не номер')
        return

    logger.info('get tip user')
    async with state.proxy() as data:
        user_tip = data['tip_user']

    logger.info('get user db')
    user_data = Users()
    if user_tip == 'admin':
        if await user_data.up_admin_right(int(message.text)):
            logger.info('up user admin privilege')
            await message.reply('Вы повысили права пользователя')
        else:
            logger.warning('error up privilege user')
            await message.reply('Пользователь не нашлось')
    if user_tip == 'programmer':
        if await user_data.up_programmer_right(int(message.text)):
            logger.info('up user programmer privilege')
            await message.reply('Вы повысили права пользователя')
        else:
            logger.warning('error up privilege user')
            await message.reply('Пользователь не нашлось')
    if user_tip == 'operator':
        if await user_data.up_operator_right(int(message.text)):
            logger.info('up user operator privilege')
            await message.reply('Вы повысили права пользователя')
        else:
            logger.warning('error up privilege user')
            await message.reply('Пользователь не найден')

    logger.info('finish up privilege state')
    await state.finish()


def register_up_privilege_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register up privilege user function choice tip user')
    dp.register_callback_query_handler(choice_tip_user_admin,
                                       state=UpPrivilegeUsers.choice_tip_user,
                                       is_admin=True)

    logger.info('register up privilege user function choice user id')
    dp.register_message_handler(get_id_user_admin,
                                state=UpPrivilegeUsers.choice_user_id,
                                is_admin=True)
