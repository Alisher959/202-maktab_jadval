import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    num=0
    for user in users:
        user_id = user[0]
        photo_id = 'AgACAgIAAxkBAAEOi6RiJ0lGDrssP9-VcqOJrEGSAjzJKAACyrkxGwGZOEm6mUr33hWgowEAAwIAA3kAAyME'
        await bot.send_photo(chat_id=user_id,photo=photo_id, caption='Mening portfoliom 👉 alisherjon.uz 👈')
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")


@dp.message_handler(text="/users", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    num1=0
    for user in users:
        user_id = user[0]
        num1=num1+1
        await asyncio.sleep(0.05)
    await bot.send_message(chat_id=ADMINS[0], text=f'foydalanuvchilar soni {num1}ta ') 