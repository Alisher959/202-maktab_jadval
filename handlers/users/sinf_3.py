from sre_parse import State
from states.sinf_state import sinf_state
from states.sinf_harf import sinf_harf
from states.end import end
from keyboards.default.end import end_orqaga
from keyboards.default.sinf import sinf, harf_sinf_5
from keyboards.default.hafta import hafta_1_4
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types

from loader import dp

@dp.message_handler(text = "3️⃣ 3-sinf 3️⃣")
async def bot_start(message: types.Message):
    await message.answer(f"Sinf qabul qilindi endi tugmalardan birini tanlang.", reply_markup=harf_sinf_5)
    await sinf_state.sinf_3.set()

@dp.message_handler(text = "A sinf", state=sinf_state.sinf_3)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_a.set()

@dp.message_handler(text = "B sinf", state=sinf_state.sinf_3)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_b.set()

@dp.message_handler(text = "V sinf", state=sinf_state.sinf_3)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_v.set()

@dp.message_handler(text = "G sinf", state=sinf_state.sinf_3)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_g.set()

@dp.message_handler(text = "D sinf", state=sinf_state.sinf_3)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_d.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_state.sinf_3)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_3_a)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf qabul qilindi endi tugmalardan birini tanlang.", reply_markup=harf_sinf_5)
    await sinf_state.sinf_3.set()


@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_3_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_a_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_a.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_3_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_a_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_a.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_3_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_a_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_a.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_3_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_a_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_a.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_3_a)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_a_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_a.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_3_a)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_3_a)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_a.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_3_a)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_5)
    await sinf_state.sinf_3.set()



@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_3_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_b_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_b.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_3_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_b_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_b.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_3_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_b_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_b.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_3_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_b_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_b.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_3_b)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_b_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_b.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_3_b)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_3_b)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_b.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_3_b)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_5)
    await sinf_state.sinf_3.set()


@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_3_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_v_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_v.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_3_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_v_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_v.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_3_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_v_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_v.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_3_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_v_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_v.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_3_v)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_v_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_v.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_3_v)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_3_v)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_v.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_3_v)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_5)
    await sinf_state.sinf_3.set()


@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_3_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_g_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_g.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_3_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_g_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_g.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_3_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_g_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_g.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_3_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_g_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_g.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_3_g)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_g_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_g.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_3_g)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_3_g)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_g.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_3_g)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_5)
    await sinf_state.sinf_3.set()


@dp.message_handler(text = "📅 Dushanba 📅", state=sinf_harf.sinf_3_d)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_d_du.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_d.set()

@dp.message_handler(text = "📅 Seshanba 📅", state=sinf_harf.sinf_3_d)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_d_se.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_d.set()

@dp.message_handler(text = "📅 Chorshanba 📅", state=sinf_harf.sinf_3_d)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_d_chor.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_d.set()

@dp.message_handler(text = "📅 Payshanba 📅", state=sinf_harf.sinf_3_d)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_d_pay.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_d.set()

@dp.message_handler(text = "📅 Juma 📅", state=sinf_harf.sinf_3_d)
async def bot_start(message: types.Message, state: FSMContext):
    f = open("documents/sinf.sinf_3_d_juma.txt", "r")
    text = f.read()
    f.close()
    await message.answer(f"Dars jadval\n{text}\n\n\n Maktab rasmiy kanali 👉 <a href='https://t.me/Shodiyeva_202'>202-maktab</a>", reply_markup=end_orqaga, disable_web_page_preview=True)
    await end.end_back_3_d.set()

@dp.message_handler(text = "🔙 Bosh sahifa 🔙", state=sinf_harf.sinf_3_d)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! Botimizga xush kelibsiz", reply_markup=sinf)
    await state.finish()

@dp.message_handler(text = "🔙 Назад 🔙", state=end.end_back_3_d)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍.  Endi hafta kunini tanlang👌.", reply_markup=hafta_1_4)
    await sinf_harf.sinf_3_d.set()

@dp.message_handler(text = "🔙 Назад 🔙", state=sinf_harf.sinf_3_d)
async def bot_start(message: types.Message):
    await message.answer(f"Sinf tanlandi👍. Tugmalardan birini tanlang👌.", reply_markup=harf_sinf_5)
    await sinf_state.sinf_3.set()