import telebot
from telebot import types
from db import productRepository
from messaging.action import Action

def product_details_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
    data = productRepository.fetchProduct(action.payload)
    if len(data) > 0:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Добавить в корзину", callback_data=Action('add_to_cart', action.payload).to_json())
        row = data[0]
        markup.row(btn)
        message = f"""
{row["name"]}\n
{row["description"]}\n
Цена: {row["price"]}"""
        bot.send_message(callback.message.chat.id, message, reply_markup=markup)
    else:
        bot.send_message(callback.message.chat.id, 'Извините, воры его украли')
