from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


FORBIDDEN_PHRASE = [
    'ahmoq',
    'telba',
]


@dp.message_handler(text_contains='ahmoq')
async def text_example(msg: types.Message):
    await msg.reply("So'kish mumkin emas!")

@dp.message_handler(filters.Text(equals='assalom alaykum', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Waalaykum assalom')

@dp.message_handler(filters.Text(contains='assalom', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Waalaykum assalom')

# boshqa parametrlar
# startswith
# endswith