from pickle import TRUE
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

hafta_1_4 = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="📅 Dushanba 📅"),
                KeyboardButton(text="📅 Seshanba 📅"),
            ],
            [
                KeyboardButton(text="📅 Chorshanba 📅"),
                KeyboardButton(text="📅 Payshanba 📅"),
            ],   
            [
                KeyboardButton(text="📅 Juma 📅"),
                KeyboardButton(text="🔙 Назад 🔙"),
            ],
            [
                KeyboardButton(text="🔙 Bosh sahifa 🔙"),
            ],
        ],
        resize_keyboard=True
)
hafta_5_11 = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="📅 Dushanba 📅"),
                KeyboardButton(text="📅 Seshanba 📅"),
            ],
            [
                KeyboardButton(text="📅 Chorshanba 📅"),
                KeyboardButton(text="📅 Payshanba 📅"),
            ],
            [
                KeyboardButton(text="📅 Juma 📅"),
                KeyboardButton(text="📅 Shanba 📅"),
            ],
            [
                KeyboardButton(text="🔙 Назад 🔙"),
                KeyboardButton(text="🔙 Bosh sahifa 🔙"),
            ],
            
        ],
        resize_keyboard=True
)

hafta_1_4_ru = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="📅 Понедельник 📅"),
                KeyboardButton(text="📅 Вторник 📅"),
            ],
            [
                KeyboardButton(text="📅 Среда 📅"),
                KeyboardButton(text="📅 Четверг 📅"),
            ],   
            [
                KeyboardButton(text="📅 Пятница 📅"),
                KeyboardButton(text="🔙 Назад 🔙"),
            ],
            [
                KeyboardButton(text="🔙 Bosh sahifa 🔙"),
            ],
        ],
        resize_keyboard=True
)
hafta_5_11_ru = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="📅 Понедельник 📅"),
                KeyboardButton(text="📅 Вторник 📅"),
            ],
            [
                KeyboardButton(text="📅 Среда 📅"),
                KeyboardButton(text="📅 Четверг 📅"),
            ],
            [
                KeyboardButton(text="📅 Пятница 📅"),
                KeyboardButton(text="📅 Суббота 📅"),
            ],
            [
                KeyboardButton(text="🔙 Назад 🔙"),
                KeyboardButton(text="🔙 Bosh sahifa 🔙"),
            ],
            
        ],
        resize_keyboard=True
)
