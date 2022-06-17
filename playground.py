def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    today_day = datetime.now().strftime('%Y-%m-%d %H:%M')
    print(f"{today_day}\n Sell BTC price: {sell_price}\n")
    return f"{today_day}\n Sell BTC price: {round(sell_price)}\n"



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


# --- Block -- last code
import requests
from bs4 import BeautifulSoup
import telebot
from auth_data import token


# url_1 = "https://hh.ru/search/vacancy?text=&fromSearchLine=true&area=1" #area=1 - Moscow
# url_2 = "https://hh.ru/search/vacancy?text=&fromSearchLine=true&area=1&page=1&hhtmFrom=vacancy_search_list"
# url_3 = "https://hh.ru/search/vacancy?text=&fromSearchLine=true&area=1&page=2&hhtmFrom=vacancy_search_list"
# url_4 = "https://hh.ru/search/vacancy?text=parsing&from=suggest_post&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true"
# url_parsing = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&ored_clusters=true&text=парсинг&search_period=7&hhtmFrom=vacancy_search_list"
#
# headers = {
#     "Accept": "*/*",
#     "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
# }

# --- Block for use only ones ---
# req = requests.get(url=url_parsing, headers=headers)
# response = req.text
# # print(response)
#
# with open("index.html", "w") as file:
#     file.write(response)

with open("index.html", "r") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_title = soup.find_all(class_="g-user-content")
for title in all_title:
    print(title.text)

