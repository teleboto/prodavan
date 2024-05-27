import telebot
from telebot import types
from db import orderRepository
from messaging.action import Action

def list_orders_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
    user_id = callback.from_user.id
    orders = orderRepository.fetch_all_orders(user_id)
    if len(orders) > 0:
        markup = types.InlineKeyboardMarkup()
        for order_row in orders:
            btn = types.InlineKeyboardButton(f"Заказ № {order_row['order_id']} от {order_row['date_ordered']}", callback_data=Action('order_details', order_row["order_id"]).to_json())
            markup.row(btn)
        bot.send_message(callback.message.chat.id, "Ваши заказы:\n", reply_markup=markup)
    else:
        bot.send_message(callback.message.chat.id, 'У вас пока еще нет заказов')
