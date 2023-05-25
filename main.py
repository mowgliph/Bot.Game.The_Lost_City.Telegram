import keep_alive as alive
import constants as key
from telebot import *


alive.keep_alive()

bot = telebot.TeleBot(key.API_KEY)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.reply_to(message, "Welcome to the Lost City adventure game! \n Type /help to see the available commands.")

if __name__ == __main__:
    print("Loading The Lost City")
    bot.infinity_polling()
    print('fin')

