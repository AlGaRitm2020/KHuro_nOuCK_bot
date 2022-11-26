from aiogram.dispatcher import FSMContext

import parsing.get_books
import parsing.get_books1
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove, ParseMode
import keyboards
import states
from aiogram.dispatcher.filters import Command

@dp.message_handler(text=keyboards.default.book_captions[0])
async def save_book(message: Message):
    await message.answer("Книга сохранена в избранное", reply_markup=keyboards.default.book_menu)

@dp.message_handler(text=keyboards.default.book_captions[1])
async def put_rate(message: Message):
    await message.answer("Поставьте оценку от 1 до 10", reply_markup=keyboards.default.book_menu)

@dp.message_handler(text=keyboards.default.book_captions[2])
async def show_rates(message: Message):
    await message.answer("Отзывы пользователей о книге", reply_markup=keyboards.default.book_menu)

@dp.message_handler(text=keyboards.default.book_captions[3])
async def change_status(message: Message):
    await message.answer("Статус прочтения изменен", reply_markup=keyboards.default.book_menu)



