from aiogram import executor
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from config import dp
from Buttonlar.reply_button import start_button
from Buttonlar.inline_button import kurslar_button, python_button

################################################################################
@dp.message_handler(commands='start')
async def start(message: Message):
    photo = open('images\photo_2022-11-05_21-28-22.jpg', 'rb')
    text = f'Assalomu aleykum {message.from_user.full_name},Boltayev Diyorbek yaratgan Botga xush kelibsiz👋'
    await message.answer_photo(photo, caption=text, reply_markup=start_button)

@dp.message_handler(commands='help')
async def help(message: Message):
    await message.answer('Yordam uchun +99888 792-20-02 ga murojaat qiling.')
###################################################################################

@dp.message_handler(text='Kurslar')
async def kurslar(message: Message):
    image= open('images\photo_2023-07-21_18-13-45.jpg', 'rb')
    text = 'Kerakli kursni tanlang!'
    await message.answer_photo(image, caption=text, reply_markup=kurslar_button)
########################################################################################
@dp.message_handler(text='Biz Haqimizda')
async def malumot(message:Message):
    image=open('images\photo_2023-07-21_18-13-45.jpg','rb')
    text='iSystem IT Academy - texnologik ta\'lim yetakchisi\n🌐 isystem.uz\nManzil: Mirzo Ulug\'bek ko\'chasi 54A \nMo\'ljal: Buyuk ipak yo\'li metrosi\n📞 +99899 882- 60-60 \n💻  Admin: @isystemadmin\n💬 Savollar uchun: @isystemgroupuz'
    await message.answer_photo(image,caption=text)

@dp.callback_query_handler(text='py_found')
async def pyt_found(call: CallbackQuery):
    image = open('images/photo_2023-05-26_16-56-24.jpg', 'rb')
    text = 'Bu kurs 4 oy davom etadi va quyidagilar o\'rgatiladi\n' \
           '1.Python Basic\n2.Python Packages\n3.OOP\n4.Data Structura'
    await call.message.answer_photo(image, caption=text, reply_markup=python_button)
    await call.answer(cache_time=10)

@dp.callback_query_handler(text='1')
async def py1(call: CallbackQuery):
    async def malumot(call: CallbackQuery):
        await call.message.answer_video(open('tg.mp4', 'rb'))
@dp.callback_query_handler(text='2')
async def py1(call: CallbackQuery):
    await call.message.answer('Ikkinchi darsga xush kelipsiz')
    await call.answer(cache_time=10)

@dp.callback_query_handler(text='3')
async def py1(call: CallbackQuery):
    await call.message.answer('Uchincchi darsga xush kelipsiz')
    await call.answer(cache_time=10)

@dp.callback_query_handler(text='4')
async def py1(call: CallbackQuery):
    await call.message.answer('To\'rtichi darsga xush kelipsiz')
    await call.answer(cache_time=10)

@dp.callback_query_handler(text='5')
async def py1(call: CallbackQuery):
    await call.message.answer('Beshinchi darsga xush kelipsiz')
    await call.answer(cache_time=10)

@dp.callback_query_handler(text='6')
async def py1(call: CallbackQuery):
    await call.message.answer('Oltinchi darsga xush kelipsiz')
    await call.answer(cache_time=10)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
