import sqlite3
from aiogram import types
from keyboards.default.sinf import sinf
from aiogram.dispatcher.filters.builtin import CommandStart
from states.sinf_harf import sinf_harf
from data.config import ADMINS
from loader import dp, db, bot




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        pass
    await message.answer(f"Salom, {message.from_user.first_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    # Adminga xabar beramiz

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def bot_start(message: types.Message):    
    await message.reply(f"{message.photo[-1].file_id}")
