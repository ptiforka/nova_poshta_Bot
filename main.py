from consts import *

import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands='start')
def send_welcome(message):
    bot.reply_to(message, "Yeah! basic setup completed!")


if __name__ == '__main__':
    bot.polling()
