from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
import re

@dp.message_handler(CommandStart(deep_link='kunuz'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salom,{message.from_user.full_name}!\n"
    text += f"Sizni {args} tavsiya qildi"
    await message.answer(text)

@dp.message_handler(CommandStart(deep_link='foydaliLink'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salom,{message.from_user.full_name}!\n"
    text += f"Sizni {args} tavsiya qildi"
    await message.answer(text)

@dp.message_handler(CommandStart(deep_link=re.compile("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salom,{message.from_user.full_name}!\n"
    text += f"Siz {args} saytidan keldingiz"
    await message.answer(text)


@dp.message_handler(commands='start')
@dp.message_handler(text="/start")
@dp.message_handler(CommandStart())
@dp.edited_message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")


