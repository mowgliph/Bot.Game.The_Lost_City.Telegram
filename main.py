# 5994663798:AAG71TpWfx-jM4aFTJG1U97rURALLNOrnDA

from constants import API_KEY
from telegram.ext import Updater, CommandHandler


print("Loading The Lost City...");

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = """
    Welcome to the Lost City adventure game! \n
    Type /help to see the available commands. 
    """)

updater = Updater(API_KEY, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()