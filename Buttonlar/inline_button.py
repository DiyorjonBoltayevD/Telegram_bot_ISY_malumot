from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kurslar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python Foundation', callback_data='py_found'),
            InlineKeyboardButton(text='Java Foundation', callback_data='jv_found'),
        ],
        [
            InlineKeyboardButton(text='Python Backend', callback_data='py_back'),
            InlineKeyboardButton(text='Java Backend', callback_data='jv_back'),
        ],
    ],
    row_width=3
)

python_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1-dars', callback_data='1'),
            InlineKeyboardButton(text='2-dars', callback_data='2'),
        ],
        [
            InlineKeyboardButton(text='3-dars', callback_data='3'),
            InlineKeyboardButton(text='4-dars', callback_data='4'),
        ],
        [
            InlineKeyboardButton(text='5-dars', callback_data='5'),
            InlineKeyboardButton(text='6-dars', callback_data='6'),
        ]
    ]
)