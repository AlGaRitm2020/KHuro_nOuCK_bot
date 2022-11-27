from aiogram.dispatcher import FSMContext

import os
import parsing.get_book

from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove, ParseMode
import keyboards
import states
import utils
from aiogram.dispatcher.filters import Command

from uuid import uuid4


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

    await message.answer(f"Парсинг занимает несколько секунд", reply_markup=keyboards.default.back_menu)

    try:    
        name, author, byte_img, pages, genre, description, link = await parsing.get_book.parse_book(query)

        caption = f'<b>{name}\n</b>' \
              f'<i>Автор:</i> {author}\n' \
              f'<i>Жанр:</i> {genre}\n' \
              f'<i>Количество страниц:</i> {pages}\n' \
              f'<i>Описание:</i> {description}\n' \
              f'<a href = "{link}">Ссылка для прочтения</a>'
    
#    await message.answer(caption, parse_mode="html", reply_markup=keyboards.default.book_menu)
#    await state.BookMenu.base_state.set()
    
        await message.answer_photo(byte_img, caption, parse_mode="html", reply_markup=keyboards.default.book_menu)
 
        await state.update_data(book_name=name)
        await states.BookMenu.save.set()     
    except: 
        await message.answer('По данному запросу ничего не найдено')
        await state.finish()

@dp.message_handler(state=states.SearchByPhoto.recive_photo, content_types=['photo'])
async def recive_photo(message: Message, state: FSMContext):
    chat_id = message.from_user.id
    await message.photo[-1].download(f'user_folders/user_{chat_id}/{str(uuid4())[-11::]}.jpg')
    await message.answer(f"Парсинг занимает несколько секунд", reply_markup=keyboards.default.back_menu)


    # === starting text recognition
    def get_book_name():
        return "Война и мир" 

    book_name = get_book_name()
    # === end
    
    
    query = "Кострикин введение в алгебру"
    try:
        name, author, byte_img, pages, genre, description, link = await parsing.get_book.parse_book(query)

        caption = f'<b>{name}\n</b>' \
              f'<i>Автор:</i> {author}\n' \
              f'<i>Жанр:</i> {genre}\n' \
              f'<i>Количество страниц:</i> {pages}\n' \
              f'<i>Описание:</i> {description}\n' \
              f'<a href = "{link}">Ссылка для прочтения</a>'
    
    

        await message.answer_photo(byte_img, caption, parse_mode="html", reply_markup=keyboards.default.book_menu)

        await state.update_data(book_name=name)
        await states.BookMenu.save.set()  

    except:
        await message.answer("По данному запросу ничего не найдено")
        await state.finish()

@dp.message_handler(state=states.SearchByPhoto.recive_photo)
async def recive_photo_eroor(message: Message, state: FSMContext):
    """
    if (message == "/start"):
        await state.finish()
        return 
    """


    await message.answer("Ошибка! Отправьте одну картинку", reply_markup=keyboards.default.back_menu)     
    await states.SearchByPhoto.recive_photo.set()



@dp.message_handler(text=keyboards.default.main_captions[3])
async def history(message: Message):
    chat_id = message.from_user.id
    
    await message.answer(f'История отправлений пользователя {chat_id}' ,reply_markup=keyboards.default.back_menu)
    
    # import required module
# assign directory
    directory = f'user_folders/user_{chat_id}'

# iterate over files in
# that directory
    for filename in os.listdir(directory):
        image_bytes = open(directory + '/' +  filename, 'rb') 
        await message.answer_photo(image_bytes, '', parse_mode="html")
 


    await states.SearchByPhoto.recive_photo.set()

@dp.message_handler(text=keyboards.default.main_captions[4])
async def favorites(message: Message):
    chat_id = message.from_user.id
   

    favorites_books = await utils.db_api.repo.get_favorites(chat_id)

    await message.answer(f'Ваши Сохранненые книги:' )

    i = 1
    if len(favorites_books) == 0:
        await message.answer("У вас нет сохранных книг")
    for book_name, is_read, rate, feedback in favorites_books:
        
        if is_read:
            msg =  f'{i} "{book_name}" <b>ПРОЧИТАНА</b>\n'
        else:
            msg =  f'{i} "{book_name}" <b>НЕ ПРОЧИТАНА</b>\n'

        if rate == 0:
            msg += "Еще не оценена"
        else:
            msg += f"Оценка: {rate}/10"

        if feedback == '':
            msg += ", без отзыва"
        else:
            msg += f"\nОтзыв: {feedback}"

        await message.answer(msg, parse_mode='html')
        i = i + 1 
