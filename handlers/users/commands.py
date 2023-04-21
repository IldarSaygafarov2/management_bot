from telebot import types

from data.loader import bot


@bot.message_handler(commands=["start"])
def command_start(message: types.Message):
    chat_id = message.from_user.id
    bot.reply_to(message, "Hello")
