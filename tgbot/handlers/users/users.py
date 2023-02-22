from aiogram.dispatcher import Dispatcher
from aiogram.types import Message


async def start_user(message: Message) -> None:
    await message.reply(f'Приветствуем {message.from_user.username}\n'
                        f'вы здесь можете купить услуги по программированию')


async def help_user(message: Message) -> None:
    await message.reply('Вы в этом боте можете покупать услуги по программированию')


def register_user(dp: Dispatcher) -> None:
    dp.register_message_handler(start_user, commands='start', state='*')
    dp.register_message_handler(help_user, commands='help', state='*')
