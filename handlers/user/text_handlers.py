from telebot.types import Message,ReplyKeyboardRemove,ReplyKeyboardMarkup,CallbackQuery
import psycopg2
from loader import *

from keyboards.default import *
from keyboards.inlane import *
from state import *
import re

@bot.message_handler(func=lambda message: message.text =='Asosiy Menyu 🏠')
def reaction_register(message:Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    check = db.check_user(user_id)
    if None in check:
        text = "Ro'yxatdan o'tmagansiz, Iltmos ro'yxatdan o'ting!"
        markup = register_btn()
    else:
        text = 'Asosiy Menyu 🏠'
        markup = vidio_btn()
    bot.send_message(chat_id,text,reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Ro\'yxattan o\'tish 👨‍💻")
def reaction_regidter(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.set_state(user_id, RegisterState.fullname,chat_id)
    bot.send_message(chat_id, "Ismingiz va Familyangizni kriting: ✍️", reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'], state=RegisterState.fullname)
def reaction_fullname(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        data['fullname'] = message.text.title()

    bot.set_state(user_id, RegisterState.contact, chat_id)
    bot.send_message(chat_id, "Kontaktingizni kriting:📱", reply_markup=sent_contact())

@bot.message_handler(content_types=['text'],state=RegisterState.birthdate)
def reaction_birthdate(message:Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id,chat_id) as data:
        if re.match

