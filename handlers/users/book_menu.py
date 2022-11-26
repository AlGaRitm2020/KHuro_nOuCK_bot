from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove, ParseMode
import keyboards
import states
from aiogram.dispatcher.filters import Command

import utils

@dp.message_handler(text=keyboards.default.book_captions[0], state=states.BookMenu.save)
async def save_book(message: Message, state=FSMContext):
    
    data = await state.get_data() 
    book_name = data.get('book_name') 

    await utils.db_api.repo.add_to_favorites(book_name, message.chat.id)
    await message.answer("Книга сохранена в избранное", reply_markup=keyboards.default.book_menu)


@dp.message_handler(text=keyboards.default.book_captions[1], state=states.BookMenu.save)
async def put_rate(message: Message):
    await message.answer("Поставьте оценку от 1 до 10", reply_markup=keyboards.default.book_menu)

    await states.BookMenu.put_rate.set()

@dp.message_handler(text=keyboards.default.book_captions[2], state=states.BookMenu.save)
async def show_rates(message: Message, state=FSMContext):
    data = await state.get_data() 
    book_name = data.get('book_name') 
    
    avg_rate = await utils.db_api.get_average_rate(book_name)
    feedbacks = await utils.db_api.get_feedbacks(book_name)
    
    msg = f"Книга '{book_name}' \nСредняя оценка {avg_rate}/10\n"
    
    if len(feedbacks )!= 0: 
        msg += 'Отзывы пользователей\n'
        for feedback, rate, chat_id in feedbacks:
            msg += f"<b>user_{chat_id} </b>: {feedback}, <b>{rate}/10</b>\n"

    

    await message.answer(msg, reply_markup=keyboards.default.book_menu, parse_mode="html")
    

@dp.message_handler(text=keyboards.default.book_captions[3], state=states.BookMenu.save)
async def change_status(message: Message, state: FSMContext):
    data = await state.get_data() 
    book_name = data.get('book_name') 

    await utils.db_api.repo.change_is_read(book_name, message.from_user.id)
    await message.answer("Статус прочтения изменен", reply_markup=keyboards.default.book_menu)
    

@dp.message_handler(text=keyboards.default.book_captions[4], state=states.BookMenu.save)
async def leave_review(message: Message, state=FSMContext):
    data = await state.get_data() 
    book_name = data.get('book_name') 
    
    

    await message.answer("Напишите короткий отзыв о книге", reply_markup=keyboards.default.book_menu)
    await states.BookMenu.leave_review.set()
 

@dp.message_handler(state=states.BookMenu.put_rate)
async def get_rate(message: Message, state=FSMContext):
    rate = int(message.text)
    if 10 < rate < 1:
        await states.BookMenu.put_rate.set()
        return 
    
    data = await state.get_data() 
    book_name = data.get("book_name")

    await utils.db_api.repo.make_rate(message.from_user.id, book_name, rate) 
     
    await message.answer("Оценка о книге сохранена")
    await states.BookMenu.save.set()

@dp.message_handler(state=states.BookMenu.leave_review)
async def get_feedback(message: Message, state=FSMContext):
    feedback = message.text
    
    data = await state.get_data() 
    book_name = data.get("book_name")

    await utils.db_api.repo.make_feedback(message.from_user.id, book_name, feedback) 
    await message.answer("Отзыв о книге сохранен")
    await states.BookMenu.save.set()

@dp.message_handler(state="*", text=keyboards.default.book_captions[5])
async def back(message: Message, state=FSMContext):
    
    await state.finish()
    
    await message.answer("Вы вернулись в главное меню", reply_markup=keyboards.default.menu)

