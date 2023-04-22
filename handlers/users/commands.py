from telebot import types

import messages
from data.loader import bot
from keyboards import default as kb


@bot.message_handler(commands=["start"])
def command_start(message: types.Message):
    chat_id = message.from_user.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id,
                     text=messages.USER_GREETING_MESSAGE.format(first_name=first_name),
                     parse_mode="HTML",
                     reply_markup=kb.show_registration_menu())
