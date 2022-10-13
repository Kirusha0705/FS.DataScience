# Поиск данных на страницы. Позволяет по названию тегов и их атрибутов получать содержащийся в них текст
from bs4 import BeautifulSoup
# Позволяет получить инфу от сервиса. Отправляем запрос к сервису с помощью метода GET.
import requests
# Позволяет найти на HTML странице таблицу и возвратить её списком из датафреймов
import pandas as pd

# Отправляем запрос к сервису с помощью метода GET
response = requests.get('https://mfd.ru/centrobank/preciousmetals/')

page = BeautifulSoup(response.text, 'html.parser')
url = 'https://mfd.ru/centrobank/preciousmetals/'

df = pd.read_html(url)
df = df[1]
min_gold = df['Золото руб./грамм'].min()
max_gold = df['Золото руб./грамм'].max()

count_gold = 100000 / min_gold
money_gold = count_gold * max_gold
money = money_gold - 100000

print(money)


