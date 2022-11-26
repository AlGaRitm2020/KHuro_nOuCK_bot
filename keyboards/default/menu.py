from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
main_captions = ["Поиск по фотографии", "Поиск по названию", "Популярные в боте", "История поиска", "Сохранненные книги", ""]
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=main_captions[0]),
            KeyboardButton(text=main_captions[1]),
            KeyboardButton(text=main_captions[2]),
        ],
        [
            KeyboardButton(text=main_captions[3]),
            KeyboardButton(text=main_captions[4]),
            KeyboardButton(text=main_captions[5]),
        ],
    ],
    resize_keyboard=True
)
