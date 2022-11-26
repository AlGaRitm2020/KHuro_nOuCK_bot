from aiogram.dispatcher import FSMContext


from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove, ParseMode
import keyboards
import states
from aiogram.dispatcher.filters import Command


@dp.message_handler(text=keyboards.default.main_captions[4])
async def history(message: Message):

    await message.answer(f'История отправлений')
    await states.SearchByPhoto.recive_photo.set()




