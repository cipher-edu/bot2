from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandPrivacy, CommandSettings

from loader import dp

@dp.message_handler(CommandSettings())
async def bot_help(message: types.Message):
    text = ("Bot sozlamalari")
    await message.answer(text)

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
