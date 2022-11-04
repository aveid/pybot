import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(config("TOKEN_BOT"))


@bot.message_handler(commands=["start", "hi"])
def get_start_message(message):
    full_name = f"{message.from_user.username}!!!"
    text = f"Welcome {full_name}"
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def get_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if message.text.lower() == "меню":
        text = "Выберите пожалуйста:"
        btn1 = types.InlineKeyboardButton("Чай", callback_data="tea")
        btn2 = types.InlineKeyboardButton("Кофе", callback_data="coffee")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def get_callback_data(call):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    text = ""
    if call.data == "tea":
        text = f"Выберите желаемы чай внизу:"
        btn1 = types.KeyboardButton("black")
        btn2 = types.KeyboardButton("blue")
        btn3 = types.KeyboardButton("green")
        murkup.add(btn1, btn2, btn3)

    if call.data == "coffee":
        text = f"Выберите желаемы coffee внизу:"
        btn1 = types.KeyboardButton("latte")
        btn2 = types.KeyboardButton("cappuchino")
        btn3 = types.KeyboardButton("espresso")
        btn4 = types.KeyboardButton("americano")
        murkup.add(btn1, btn2, btn3, btn4)
    bot.send_message(call.message.chat.id, text, reply_markup=murkup)



bot.polling()