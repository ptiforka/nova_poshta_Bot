from consts import TELEGRAM_TOKEN
import telebot
from np import NP
from validation import *

bot = telebot.TeleBot(TELEGRAM_TOKEN)
np = NP()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Всем привет. Этот бот написан для экспресс-лекци по ботоводству которую мы проведем в СумГу")
    send_available_commands(message)


@bot.message_handler(commands=['help'])
def send_available_commands(message):
    bot.send_message(
        message.chat.id, 'Для получения информации по ТТН просто отправьте нам её.'
        ' Добавьте телефон для более подробной по посылке. Пример использования - ТТН НОМЕР_ТЕЛЕФОНА')


@bot.message_handler()
def find_ttn(message):
    ttn, phone = unpack(message)
    if ttn_validation(ttn) and phone_validation(phone):
        bot.send_message(
            message.chat.id,
            serialize_message(
                np.tracking(
                    ttn,
                    phone),
                phone))
    else:
        bot.send_message(
            message.chat.id,
            'Неправильный ТТН или номер телефона')


def serialize_message(np_response, phone):
    message = f"""
Ваша стоимость доставки - {np_response['delivery_cost']} гривны
Вес посылки - {np_response['weight']} кг
               """
    if phone is not None:
        message = f"{message} \nДоставка оформлена на имя - {np_response['recipient_name']}"
    else:
        message = f"{message} \nДля более подробный информации введите свой номер)"

    return message


if __name__ == '__main__':
    bot.polling()
