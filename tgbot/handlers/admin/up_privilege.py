from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext, Dispatcher

import logging

from tgbot.misc.states import UpPrivilegeUsers
from tgbot.models.users import Users


logger = logging.getLogger(__name__)


async def choice_tip_user_admin(callback: CallbackQuery, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    async with state.proxy() as data:
        data['tip_user'] = callback.data[7:][:-4]

    logging.info('save choice tip user in memory')

    await callback.message.edit_text('Введите id пользователя')

    logging.info('set choice_user_id state in UpPrivilegeUsers')
    await UpPrivilegeUsers.choice_user_id.set()


async def get_id_user_admin(message: Message, state: FSMContext) -> None:
    if not message.text.isdigit():
        await message.reply('Вы вели не число')
        return

    async with state.proxy() as data:
        user_tip = data['tip_user']

    user_data = Users(message.bot.get('config').db)
    if user_tip == 'admin':
        if user_data.up_admin_right(int(message.text)):
            await message.reply('Вы повысили права пользователя')
        else:
            await message.reply('Пользователь не нашлось')
    if user_tip == 'programmer':
        if user_data.up_programmer_right(int(message.text)):
            await message.reply('Вы повысили права пользователя')
        else:
            await message.reply('Пользователь не нашлось')
    if user_tip == 'operator':
        if user_data.up_operator_right(int(message.text)):
            await message.reply('Вы повысили права пользователя')
        else:
            await message.reply('Пользователь не нашлось')


def register_up_privilege_handler(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(choice_tip_user_admin,
                                       state=UpPrivilegeUsers.choice_tip_user)
    dp.register_message_handler(get_id_user_admin,
                                state=UpPrivilegeUsers.choice_user_id)
