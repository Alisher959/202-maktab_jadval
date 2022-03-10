from sre_parse import State
from states.sinf_state import sinf_state
from states.sinf_harf import sinf_harf
from states.end import end
from keyboards.default.end import end_orqaga
from keyboards.default.sinf import sinf, harf_sinf_3
from keyboards.default.hafta import hafta_5_11
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types

from loader import dp

@dp.message_handler(text = "5️⃣ 5-sinf 5️⃣")
async def bot_start(message: types.Message):
    await message.answer(f"Sinf qabul qilindi endi tugmalardan birini tanlang.", reply_markup=harf_sinf_3)
    await sinf_state.sinf_5.set()

@dp.message_handler(text = "A sinf", state=sinf_state.sinf_5)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_5_11)
    await sinf_harf.sinf_5_a.set()

@dp.message_handler(text = "B sinf", state=sinf_state.sinf_5)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_5_11)
    await sinf_harf.sinf_5_b.set()

@dp.message_handler(text = "V sinf", state=sinf_state.sinf_5)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_5_11)
    await sinf_harf.sinf_5_v.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_state.sinf_5)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_5_a)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf qabul qilindi endi tugmalardan birini tanlang.", reply_markup=harf_sinf_3)
    await sinf_state.sinf_5.set()


@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_5_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_a_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_a.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_5_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_a_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_a.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_5_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_a_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_a.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_5_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_a_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_a.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_5_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_a_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_a.set()

@dp.message_handler(text = "📅 Shanba 📅", state=sinf_harf.sinf_5_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_a_shanba.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_a.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_5_a)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_5_a)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_5_11)
    await sinf_harf.sinf_5_a.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_5_a)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_3)
    await sinf_state.sinf_5.set()



@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_5_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_b_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_b.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_5_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_b_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_b.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_5_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_b_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_b.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_5_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_b_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_b.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_5_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_b_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_b.set()

@dp.message_handler(text = "📅 Shanba 📅", state=sinf_harf.sinf_5_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_b_shanba.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_b.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_5_b)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_5_b)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_5_11)
    await sinf_harf.sinf_5_b.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_5_b)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_3)
    await sinf_state.sinf_5.set()



@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_5_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_v_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_v.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_5_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_v_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_v.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_5_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_v_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_v.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_5_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_v_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_v.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_5_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_v_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_v.set()

@dp.message_handler(text = "📅 Shanba 📅", state=sinf_harf.sinf_5_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_5_v_shanba.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_5_v.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_5_v)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_5_v)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_5_11)
    await sinf_harf.sinf_5_v.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_5_v)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_3)
    await sinf_state.sinf_5.set()

