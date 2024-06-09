import telebot
from telebot import types
from db import specialRepository
from messaging.action import Action

def list_special_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
  data = specialRepository.fetchActiveSpecial()
  if len(data) > 0:
      markup = types.InlineKeyboardMarkup()
      for row in data:
          btn = types.InlineKeyboardButton(row["name"], callback_data=Action('list_special_goods', row["special_id"]).to_json())
          markup.row(btn)
      bot.send_message(callback.message.chat.id, "Доступные специальные предложения\nВыберете предложение для просмотра товаров", reply_markup=markup)
  else:
      bot.send_message(callback.message.chat.id, 'На данный момент специальные предложения отсутствуют')