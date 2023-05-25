# 5994663798:AAG71TpWfx-jM4aFTJG1U97rURALLNOrnDA

from constants import API_KEY
from telegram.ext import Updater, CommandHandler


print("Loading The Lost City...");

def start(update, context):
    update.message.reply_tex("""
    Welcome to the Lost City adventure game! \n
    Type /help to see the available commands. 
    """)

def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    #commands area
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

main()