import telebot
from telebot import types
from db import userRepository
from db import OrderRepository

def fetch_main_products_handler(bot: telebot.TeleBot, callback: types.CallbackQuery):
    user_id = callback.from_user.id
    
    user = userRepository.fetchUser(user_id)
    if not user:
        userRepository.createUser(user_id, callback.from_user.first_name, callback.from_user.last_name)
    
    main_products = OrderRepository(user_id)
    
    if main_products:
        response = "Ваша корзина:\n" + "\n".join([product['name'] for product in main_products])
    else:
        response = "Ваша корзина пуста."
    
    bot.send_message(callback.from_user.id, response)