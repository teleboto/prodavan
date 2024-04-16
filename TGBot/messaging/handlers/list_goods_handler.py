import telebot
from telebot import types

def list_goods_handler(bot: telebot.TeleBot, callback: types.CallbackQuery):
  bot.send_message(callback.message.chat.id, 'Тут будет список товаров')
