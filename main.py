from telegram.ext import *
from constants import *

def start_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = """
    Welcome to the Lost City adventure game! \n
    Type /help to see the available commands. 
    """)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start_command)
dispatcher.add_handler(start_handler)

updater.start_polling()