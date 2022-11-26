from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
book_captions= ["Сохранить в избранное", "Поставить оценку", "Посмотреть отзывы", "Изменить статус прочтения", "", ""]
book_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=book_captions[0]),
            KeyboardButton(text=book_captions[1]),
        ],
        [
            KeyboardButton(text=book_captions[2]),
            KeyboardButton(text=book_captions[3]),
        ],
    ],
    resize_keyboard=True
)
