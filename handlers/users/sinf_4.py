from sre_parse import State
from states.sinf_state import sinf_state
from states.sinf_harf import sinf_harf
from states.end import end
from keyboards.default.end import end_orqaga
from keyboards.default.sinf import sinf, harf_sinf_4
from keyboards.default.hafta import hafta_1_4
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types

from loader import dp

@dp.message_handler(text = "4️⃣ 4-sinf 4️⃣")
async def bot_start(message: types.Message):
    await message.answer(f"Sinf qabul qilindi endi tugmalardan birini tanlang.", reply_markup=harf_sinf_4)
    await sinf_state.sinf_4.set()

@dp.message_handler(text = "A sinf", state=sinf_state.sinf_4)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_4_a.set()

@dp.message_handler(text = "B sinf", state=sinf_state.sinf_4)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_4_b.set()

@dp.message_handler(text = "V sinf", state=sinf_state.sinf_4)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_4_v.set()

@dp.message_handler(text = "G sinf", state=sinf_state.sinf_4)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_4_g.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_state.sinf_4)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_4_a)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf qabul qilindi endi tugmalardan birini tanlang.", reply_markup=harf_sinf_4)
    await sinf_state.sinf_4.set()


@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_4_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_a_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_a.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_4_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_a_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_a.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_4_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_a_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_a.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_4_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_a_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_a.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_4_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_a_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_a.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_4_a)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_4_a)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_4_a.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_4_a)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_4)
    await sinf_state.sinf_4.set()



@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_4_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_b_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_b.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_4_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_b_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_b.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_4_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_b_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_b.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_4_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_b_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_b.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_4_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_b_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_b.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_4_b)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_4_b)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_4_b.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_4_b)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_4)
    await sinf_state.sinf_4.set()

@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_4_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_v_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_v.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_4_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_v_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_v.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_4_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_v_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_v.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_4_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_v_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_v.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_4_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_v_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_v.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_4_v)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_4_v)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_4_v.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_4_v)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_4)
    await sinf_state.sinf_4.set()


@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_4_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_g_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_g.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_4_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_g_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_g.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_4_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_g_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_g.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_4_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_g_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_g.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_4_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_4_g_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n \n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_4_g.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_4_g)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_4_g)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_4_g.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_4_g)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_4)
    await sinf_state.sinf_4.set()