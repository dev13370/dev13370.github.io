import telebot,requests,re

bot = telebot.TeleBot("1762957622:AAFuWwf1hvMHaCOiOZOz9zQGx5ga92eoj1E")
@bot.message_handler(commands=["start"])

def start(message):
    bot.send_message(message.chat_id,"hello")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat_id,"help")

@bot.message_handler(func=lambda m:True)
def get_message(message):
    msg = message.text

    req = requests.get("https")


bot.polling(True)