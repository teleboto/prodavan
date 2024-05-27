import telebot
from telebot import types
from db import userRepository
from db import cartRepository
from messaging.action import Action

def add_to_cart_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
    user_id = callback.from_user.id
    user = userRepository.fetchUser(user_id)
    if len(user) == 0:
      userRepository.createUser(user_id, callback.from_user.first_name, callback.from_user.last_name)

    cart_add = cartRepository.add_to_cart(user_id, action.payload)

    if cart_add:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Показать корзину", callback_data=Action('show_cart', '').to_json())
        markup.row(btn)
        bot.send_message(callback.from_user.id, "Товар успешно добавлен в корзину!", reply_markup=markup)
    else:
        bot.send_message(callback.from_user.id, "Не удалось добавить товар в корзину. Пожалуйста, попробуйте еще раз.")
