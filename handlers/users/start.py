import sqlite3
from aiogram import types
from keyboards.default.sinf import sinf
from aiogram.dispatcher.filters.builtin import CommandStart
from states.sinf_harf import sinf_harf
from keyboards.inline.subscription import check_button
from data.config import ADMINS, CHANNELS
from utils.misc import subscription
from loader import dp, db, bot

@dp.message_handler(commands=['start'])
async def show_channel(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        #logging.info(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"
    
    await message.answer(f"Botdan foydalanish uchun, quyidagi kanallarga obuna bo`ling: \n"
                        f"{channels_format}",
                        reply_markup=check_button,
                        disable_web_page_preview=True
    )
    await message.answer(f"Salom, {message.from_user.first_name}! Botimizga xush kelibsiz", reply_markup=sinf)

@dp.callback_query_handler(text="alisher")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> kanaliga obuna bo`lgansiz\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanalga obuna bo`lmagansiz"
                        f"<a href='{invite_link}'>Obuna bo`ling</a>\n\n"
            )
    await call.message.answer(result, disable_web_page_preview=False)
    


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
