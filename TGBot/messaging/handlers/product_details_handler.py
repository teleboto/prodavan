import telebot
import decimal
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
        if row["special_name"]:
            price = f"""Цена по акции: <s>{row["price"]}</s> {get_discounted_price(row["price"], row["discount"])}"""
        else:
            price = f"""Цена: {row["price"]}"""
        message = f"""
{row["category_name"]}: {row["name"]}\n
{row["description"]}\n
{price}"""
        bot.send_message(callback.message.chat.id, message, reply_markup=markup, parse_mode="HTML")
    else:
        bot.send_message(callback.message.chat.id, 'Извините, воры его украли')


def get_discounted_price(price, discount):
    price -= price * decimal.Decimal(discount / 100)
    return round(price, 2)