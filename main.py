import requests
from bs4 import BeautifulSoup
import telebot
from auth_data import token


url_1 = "https://hh.ru/search/vacancy?text=&fromSearchLine=true&area=1"
url_2 = "https://hh.ru/search/vacancy?text=&fromSearchLine=true&area=1&page=1&hhtmFrom=vacancy_search_list"
url_3 = "https://hh.ru/search/vacancy?text=&fromSearchLine=true&area=1&page=2&hhtmFrom=vacancy_search_list"
url_4 = "https://hh.ru/search/vacancy?text=parsing&from=suggest_post&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true"
url_parsing = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&ored_clusters=true&text=парсинг&search_period=7&hhtmFrom=vacancy_search_list"

headers = {
    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}

# --- Block for use only ones ---
# req = requests.get(url=url_parsing, headers=headers)
# response = req.text
# # print(response)
#
# with open("index.html", "w") as file:
#     file.write(response)




