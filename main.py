import keep_alive as alive
import constants as key
from telebot import *

bot = telebot.TeleBot(key.API_KEY)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.reply_to(message, "Welcome to the Lost City adventure game! \n Type /help to see the available commands.")

@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.reply_to(message, """
    A continuacion todos los comandos disponibles en el Juego: \n     
    /start - Inicia el Juego 
    /help - Muestra lista de los comandos 
    /look - Explora tu entorno 
    /go - Muevete a una nueva ubicacion 
    /inventory - Abre el Inventario 
    /take - Recoger articulos 
    /use - Usar articulos del inventario    
    """)


if __name__ == '__main__':
    print("Loading The Lost City")
    bot.infinity_polling()
    print('fin')

