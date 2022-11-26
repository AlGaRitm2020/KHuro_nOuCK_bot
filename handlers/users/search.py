from aiogram.dispatcher import FSMContext

import parsing.get_book

from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove, ParseMode
import keyboards
import states
from aiogram.dispatcher.filters import Command


@dp.message_handler(text=keyboards.default.main_captions[0])
async def send_image(message: Message):
    await message.answer(f'Отправьте картинку с книгой')
    await states.SearchByPhoto.recive_photo.set()

@dp.message_handler(text=keyboards.default.main_captions[1])
async def send_query(message: Message):
    await message.answer(f'Введите название книги \n Укажите автора если такое название не уникально')
    await states.SearchByPhoto.recive_text.set()


@dp.message_handler(state=states.SearchByPhoto.recive_text)
async def recive_text(message: Message, state: FSMContext):
    query = message.text

    await message.answer(f"Парсинг занимает несколько секунд")

    name, author, byte_img, pages, genre, description, link = await parsing.get_book.parse_book(query)

    caption = f'<b>{name}\n</b>' \
              f'<i>Автор:</i> {author}\n' \
              f'<i>Жанр:</i> {genre}\n' \
              f'<i>Количество страниц:</i> {pages}\n' \
              f'<i>Описание:</i> {description}\n' \
              f'<a href = "{link}">Ссылка для прочтения</a>'
    
#    await message.answer(caption, parse_mode="html", reply_markup=keyboards.default.book_menu)
    await state.finish()
#    await state.BookMenu.base_state.set()
    
    await message.answer_photo(byte_img, caption, parse_mode="html")

    await state.finish()

@dp.message_handler(state=states.SearchByPhoto.recive_photo, content_types=['photo'])
async def recive_photo(message: Message, state: FSMContext):
    await message.photo[-1].download('data/user_book_image/book_photo.jpg')
    await message.answer(f"Парсинг занимает несколько секунд")


    # === starting text recognition
    def get_book_name():
        return "Война и мир" 

    book_name = get_book_name()
    # === end
    
    
    query = "Кострикин введение в алгебру"
    name, author, byte_img, pages, genre, description, link = await parsing.get_book.parse_book(query)

    caption = f'<b>{name}\n</b>' \
              f'<i>Автор:</i> {author}\n' \
              f'<i>Жанр:</i> {genre}\n' \
              f'<i>Количество страниц:</i> {pages}\n' \
              f'<i>Описание:</i> {description}\n' \
              f'<a href = "{link}">Ссылка для прочтения</a>'
    
#    await message.answer(caption, parse_mode="html", reply_markup=keyboards.default.book_menu)
    await state.finish()
#    await state.BookMenu.base_state.set()
    
    await message.answer_photo(byte_img, caption, parse_mode="html")



    await state.finish()


@dp.message_handler(state=states.SearchByPhoto.recive_photo)
async def recive_photo_eroor(message: Message, state: FSMContext):
    """
    if (message == "/start"):
        await state.finish()
        return 
    """
    await message.answer("Ошибка! Отправьте одну картинку")     
    await states.SearchByPhoto.recive_photo.set()




