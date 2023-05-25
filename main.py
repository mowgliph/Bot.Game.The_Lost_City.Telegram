# 5994663798:AAG71TpWfx-jM4aFTJG1U97rURALLNOrnDA

import telebot
import constants as keys

bot = telebot.TeleBot(keys.API_KEY)

print("Loading The Lost City...");

@bot.message_handler(commands=['start','START'])

def send_welcome(message):
    bot.reply_to(message, "Welcome to the Lost City adventure game! \n Type /help to see the available commands")

bot.polling()