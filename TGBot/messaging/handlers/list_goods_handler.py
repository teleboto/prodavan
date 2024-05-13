import telebot
from telebot import types
from db import productRepository
from messaging.action import Action

def list_goods_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
  data = productRepository.fetchProductID(action.payload)
  if len(data) > 0:
      markup = types.InlineKeyboardMarkup()
      for row in data:
          btn = types.InlineKeyboardButton(row["name"], callback_data=Action('prod_details', row["product_id"]).to_json())
          markup.row(btn)
      bot.send_message(callback.message.chat.id, "Вот что есть у меня,\nвыбирай чего нада", reply_markup=markup)
  else:
      bot.send_message(callback.message.chat.id, 'Прастити, но они раскупили все ваши товары (')