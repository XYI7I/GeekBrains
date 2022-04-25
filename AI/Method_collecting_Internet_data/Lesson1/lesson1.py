'''  Урок 1. Основы клиент-серверного взаимодействия. Парсинг API¶
Задание

    Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json; написать функцию, возвращающую список репозиториев.
    П Зарегистрироваться на https://openweathermap.org/api и написать функцию, которая получает погоду в данный момент для города, название которого получается через input. https://openweathermap.org/current

Задание 1

Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json; написать функцию, возвращающую список репозиториев.
'''

import requests
import json

url = 'https://api.github.com'
user='XYI7I'

r = requests.get(f'{url}/users/{user}/repos')

with open('data.json', 'w') as f:
    json.dump(r.json(), f)

for i in r.json():
    print(i['name'])

'''  Задание 2

Зарегистрироваться на https://openweathermap.org/api и написать функцию, которая получает погоду в данный момент для города, название которого получается через input. https://openweathermap.org/current
'''

import requests
appid = '428a8740f92b5801ae78199236994a16'
service = 'https://api.openweathermap.org/data/2.5/weather'
req = requests.get(f'{service}?q=Moscow&appid={appid}')
print(req.text)

import requests
import json
appid = '428a8740f92b5801ae78199236994a16'
service = 'https://api.openweathermap.org/data/2.5/weather'
req = requests.get(f'{service}?q=Moscow&appid={appid}')
data = json.loads(req.text)

print(f"В городе {data['name']} {int(data['main']['temp']) - 273} градусов по Цельсию")