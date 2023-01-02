from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
COMMAND_EMAIL_REGEX = r"/email:" + EMAIL_REGEX


@dp.message_handler(filters.Regexp(EMAIL_REGEX))
async def regexp_email(msg: types.Message):
    await msg.answer('Email qabul qilindi')

@dp.message_handler(filters.Regexp(PHONE_NUM))
async def regexp_phone(msg: types.Message):
    await msg.answer('Telefon raqam qabul qilindi')

@dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGEX])
async def command_regexp_example(msg: types.Message):
    await msg.answer('Email qabul qilindi')