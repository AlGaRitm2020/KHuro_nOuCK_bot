from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchByPhoto(StatesGroup):
    recive_photo = State()
    recive_text = State()
