
import telebot
from telebot import types
from db import cartRepository
from messaging.action import Action

def show_cart_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
    user_id = callback.from_user.id
    data = cartRepository.get_cart_products(user_id)
    if len(data) > 0:
        markup = types.InlineKeyboardMarkup()
        for row in data:
            btn = types.InlineKeyboardButton(f"{row['name']} - {row['quantity']} шт.", callback_data=Action('prod_details', row["product_id"]).to_json())
            markup.row(btn)
        btn = types.InlineKeyboardButton("Создать заказ", callback_data=Action('place_order', '').to_json())
        markup.row(btn)
        btn = types.InlineKeyboardButton("Очистить корзину", callback_data=Action('clear_cart', '').to_json())
        markup.row(btn)
        bot.send_message(callback.message.chat.id, "Ваша корзина:\n", reply_markup=markup)
    else:
        bot.send_message(callback.message.chat.id, 'В вашей корзине пусто')
