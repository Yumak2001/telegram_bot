"""
Этот файл содержит слушатели на текстовые сообщения в боте
"""
import asyncio

from aiogram import types

from app.misc import dp, bot, i18n
from app.utils.message import msgToLog

_ = i18n.gettext


@dp.message_handler()
async def echo_message(msg: types.Message):
    msgToLog(msg)
    await bot.send_message(msg.from_user.id, msg.text)
