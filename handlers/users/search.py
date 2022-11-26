from aiogram.dispatcher import FSMContext

import parsing.get_books
import parsing.get_books1
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove, ParseMode
import keyboards
import states
from aiogram.dispatcher.filters import Command

# --- Main Menu Handlers
@dp.message_handler(text=keyboards.default.menu.main_captions[5])
async def solve_task(message: Message):
    books = await parsing.get_books.get_books(keyboards.default.menu.main_captions[2])
    while not books:
        books = await parsing.get_books.get_books(keyboards.default.menu.main_captions[2])
    caption = f'<b>{books[0]["name"]}\n</b>' \
              f'<i>Оценка:</i> {books[0]["rate"]}\n' \
              f'<i>Автор:</i> {books[0]["author"]}\n' \
              f'<i>Жанр:</i> {books[0]["genre"]}\n' \
              f'<i>Количество страниц:</i> {books[0]["pages"]}\n' \
              f'<i>Описание:</i> {books[0]["about"]}\n' \
              f'<a href = "{books[0]["link"]}">Ссылка для прочтения</a>'
    await message.answer_photo(books[0]["img"], caption, parse_mode="html")


@dp.message_handler(text=keyboards.default.menu.main_captions[0])
async def theory(message: Message):
    await message.answer(f'Отправьте картинку с книгой')
