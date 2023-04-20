
import logging
import datetime
from aiogram import Bot, Dispatcher, executor, types
from tugma import keyboard, ramadan
from aiogram.types import CallbackQuery

API_TOKEN = "5963546190:AAE9QKJfOptxxSnpRZqhRecwp4pfd8J2Nhw"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
 await bot.send_photo(chat_id=message.from_user.id,photo="https://dqliving.com/wp-content/uploads/2020/04/6-RAM-MSG-first.jpg", caption="Assalomu aleykum botga xush kelibsiz! Ushbu botdan foydalanib Ramazon taqvimini bilib olishingiz mumkun.", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == "kecha")
async def kecha_taqvim(callback: CallbackQuery):
   x=datetime.datetime.now()
   day = x.strftime('%d')
   last_day = int(day)-1
   for i in ramadan:
      if int(i["kun"]) == last_day:
         await bot.send_photo(chat_id=callback.from_user.id, photo="https://ih1.redbubble.net/image.1124494602.7480/farp,small,wall_texture,product,750x1000.jpg", caption=f"<b>kechagi taqvim</b>\nSaharlik vaqti : {i['Saharlik']}\nIftorlik vaqti:{i['Iftorlik']}", reply_markup=keyboard,parse_mode="HTML")


@dp.callback_query_handler(lambda c: c.data == "bugun")
async def kecha_taqvim(callback: CallbackQuery):
   x = datetime.datetime.now()
   day = x.strftime('%d')
   last_day = int(day)
   for i in ramadan:
      if int(i["kun"]) == last_day:
         await bot.send_photo(chat_id=callback.from_user.id, photo="https://ih1.redbubble.net/image.1124494602.7480/farp,small,wall_texture,product,750x1000.jpg", caption=f"<b>bugungi taqvim</b>\nSaharlik vaqti : {i['Saharlik']}\nIftorlik vaqti:{i['Iftorlik']}", reply_markup=keyboard, parse_mode="HTML")


@dp.callback_query_handler(lambda c: c.data == "ertaga")
async def kecha_taqvim(callback: CallbackQuery):
   x = datetime.datetime.now()
   day = x.strftime('%d')
   last_day = int(day)+1
   for i in ramadan:
      if int(i["kun"]) == last_day:
         await bot.send_photo(chat_id=callback.from_user.id, photo="https://ih1.redbubble.net/image.1124494602.7480/farp,small,wall_texture,product,750x1000.jpg", caption=f"<b>ertangi taqvim</b>\nSaharlik vaqti : {i['Saharlik']}\nIftorlik vaqti:{i['Iftorlik']}", reply_markup=keyboard, parse_mode="HTML")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)