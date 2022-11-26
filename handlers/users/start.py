from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import menu
import utils
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await utils.db_api.repo.register(message.from_user.username, message.chat.id)
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=menu)
