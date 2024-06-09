import telebot
from telebot import types
from db import productRepository
from messaging.action import Action

def list_special_goods_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
  data = productRepository.fetchSpecialProducts(action.payload)
  if len(data) > 0:
      markup = types.InlineKeyboardMarkup()
      for row in data:
          btn = types.InlineKeyboardButton(row["name"], callback_data=Action('prod_details', row["product_id"]).to_json())
          markup.row(btn)
      bot.send_message(callback.message.chat.id, "Выбирайте продукты со скидкой", reply_markup=markup)
  else:
      bot.send_message(callback.message.chat.id, 'Извините, товары закончились')
