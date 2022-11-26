from aiogram.dispatcher.filters.state import StatesGroup, State


class BookMenu(StatesGroup):

    save= State()
    put_rate = State() 
    show_rates = State()
    leave_review = State()
