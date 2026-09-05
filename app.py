import telebot
from telebot import types
from telebot import util

bot = telebot.TeleBot('8233554934:AAH0KrK2lraaTi1JHm8-AdgMBcXP_UdCuKQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Hi":
#         bot.send_message(message.chat.id, "And for you HI") #, parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f'Your ID: {message.from_user.id} ') #, parse_mode='html')
#     elif message.text == "photo":
#         #photo = open('jiraf.jpg', 'rb')
#         with open('jiraf.jpg', 'rb') as file:
#             bot.send_document(message.chat.id, file)
        #bot.send_message(message.chat.id, photo)
    # else:
    #     bot.send_message(message.chat.id, f"I don't understand you") #, parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_phot(message):
    bot.send_message(message.chat.id, "WOW")


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('GO TO SITE', url = 'https://seasonvar.ru/'))
    bot.send_message(message.chat.id, 'GO', reply_markup = markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
    website = types.KeyboardButton('Вебсайт')
    start = types.KeyboardButton('START')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'GO', reply_markup = markup)




bot.polling(none_stop=True)