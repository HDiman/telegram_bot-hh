import requests
from datetime import datetime
import telebot
from auth_data import token


today_day = datetime.now().strftime('%Y-%m-%d %H:%M')


def get_data():
    req = requests.get("https://")
    response = req.json()
    result = response[]

    print()
    return


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend!")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                bot.send_message(message.chat.id, get_data())
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Disconnection!!!")
        else:
            bot.send_message(message.chat.id, "Wrong command")

    bot.polling()


if __name__ == "__main__":
    get_data()
    # telegram_bot(token)

