from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Biz Haqimizda'),
            KeyboardButton('Kurslar'),
        ],
        [
            KeyboardButton('Orqaga'),
            KeyboardButton('Keyingi')
        ]
    ],
    resize_keyboard=True
)