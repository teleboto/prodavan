
import telebot
from telebot import types
from db import orderRepository
from messaging.action import Action

def order_details_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
    user_id = callback.from_user.id
    order_data = orderRepository.fetch_order(user_id, action.payload)
    if len(order_data) > 0:
        order = order_data[0]
        order_items = orderRepository.fetch_order_items(user_id, action.payload)
        message = f"Заказ № {order['order_id']} от {order['date_ordered']}\n"
        for item in order_items:
            message += f"{item['name']} - {item['price']} x {item['quantity']} = {item['total_amount']}\n"
        message += f"Общая стоимость заказа: {order['total_amount']}\n"
        message += f"Статус заказа: {get_order_status(order['status'])}\n"

        bot.send_message(callback.message.chat.id, message)
    else:
        bot.send_message(callback.message.chat.id, 'Извините, мы потеряли ваш заказ (')


def get_order_status(status):
    if status == 'pending':
        return 'собирается'
    elif status == 'shipping':
        return 'передан в доставку'
    elif status == 'delivered':
        return 'доставлен'
    return 'какой заказ? небыло никакого заказа.'
