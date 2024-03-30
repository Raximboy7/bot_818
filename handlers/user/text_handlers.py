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
        if re.match(r"""(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})""",message.text):
            data['birthdate'] = '.'.join(message.text.split('.')[::-1])
            fullname = data['fullname']
            contact = data['contact']
            bot.set_state(user_id,RegisterState.submit,chat_id)
            bot.send_message(chat_id,f"""Ma'lumotingizni tekshiring!!!
Ism Familyangiz: <b>{fullname}</b>
Kontakt: <b>{contact}</b>
Tug'ilgan kun: <b>{message.text}</b>""", reply_markup=yes_no(), parse_mode='HTML')

        else:
            bot.set_state(user_id,RegisterState.birthdate,chat_id)
            bot.send_message(chat_id,"Tug'ilgan kuningizni qaytadan kiriting!:dd.mm.yyyy 📆",
                             reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'],state=RegisterState.submit)
def reaction_submit(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if message.text == 'Ha':
        with bot.retrieve_data(user_id, chat_id) as data:
            fullname = data['fullname']
            birthdate = data['birthdate']
            contact = data['contact']
        db.save_user(fullname, birthdate, contact, user_id)
        bot.send_message(chat_id, "Malumotlaringiz Saqlandi! ", reply_markup=vidio_btn(db.get_all_curses()))
        bot.delete_state(user_id, chat_id)
    else:
        bot.delete_state(user_id, chat_id)
        bot.set_state(user_id, RegisterState.fullname, chat_id)
        bot.send_message(chat_id, 'Ismingizni qaytadan kriting: ✍️',
                             reply_markup=ReplyKeyboardRemove() )


@bot.message_handler(func=lambda message: message.text == 'Asosiy Menyu 🔙')
def reaction_menyu(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Asosiy Menyu 🏠', reply_markup=main_menyu())

@bot.message_handler(func=lambda message: message.text == 'About 🤖')
def reaction_aloqa(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Bu bot youtubedan vidyo yuklashga yordam beradi')