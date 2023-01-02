from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

SUPERUSERS = [2007427, 32323412]
QORAROYXAT = [2121223, 3434343]

# @dp.message_handler(filters.IDFilter(chat_id=SUPERUSERS))
@dp.message_handler(chat_id=SUPERUSERS, text='secret')
async def id_filter_example(msg: types.Message):
    await msg.answer('Xush kelibsiz, SuperUSER!')