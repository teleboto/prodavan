
import telebot
import decimal
from telebot import types
from db import cartRepository
from db import orderRepository
from messaging.action import Action

def place_order_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
    user_id = callback.from_user.id
    data = cartRepository.get_cart_products(user_id)
    if len(data) > 0:
        total = 0
        for row in data:
          price = get_price(row)
          total += price * row["quantity"]
        order_id = orderRepository.add_order(user_id, total)
        for row in data:
          price = get_price(row)
          orderRepository.add_order_item(order_id, row["product_id"], price, row["quantity"])
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Посмотреть заказ", callback_data=Action('order_details', order_id).to_json())
        markup.row(btn)
        bot.send_message(callback.message.chat.id, f"Заказ создан, номер заказа: {order_id}", reply_markup=markup)
    else:
        bot.send_message(callback.message.chat.id, 'В вашей корзине пусто')

def get_price(row):
  price = row["price"]
  if row["special_name"]:
      price = get_discounted_price(row["price"], row["discount"])
  return price


def get_discounted_price(price, discount):
    price -= price * decimal.Decimal(discount / 100)
    return round(price, 2)