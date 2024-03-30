from telebot.types import Message, ReplyKeyboardRemove

from loader import bot, db

from keyboards.inlane import *
from keyboards.default import *

@bot.message_handler(chat_types='private', commands=['start'])
def reacton_start(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    db.insert_user_id(user_id)
    bot.send_message(chat_id, f"Assalomu alaykum Shoping botga hush kelibsiz  {message.from_user.first_name}", reply_markup=(main_menyu))


@bot.message_handler(commands=['help'])
def reaction_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu alekom, botni qayeri yaxshi ishlamayotgan bo'lsa @Developer_power Shu manzilga yozing !")