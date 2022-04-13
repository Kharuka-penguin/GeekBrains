# 2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое,
# требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
# Если нет желания заморачиваться с поиском, возьмите API вконтакте (https://vk.com/dev/first_guide). Сделайте
# запрос, чтобы получить список всех сообществ на которые вы подписаны.

import webbrowser
import time
import requests

webbrowser.open('https://vk.com/apps?act=manage', new=2)
time.sleep(2)
client_id = input('Создайте Standalone-приложение и скопируйте сюда номер id приложения из адресной строки браузера: ')
webbrowser.open('https://oauth.vk.com/authorize?client_id='+client_id+'&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.131', new=2)
time.sleep(2)
access_token = input('Скопируйте сюда access_token из адреса появившийся в строке браузера: ')

url = 'https://api.vk.com/method/'
method = 'groups.get'
params = {'access_token': access_token,
          'extended': '1',
          'v': '5.131'}

response = requests.get(url+method, params=params)
j_data = response.json()

with open('My_groups.txt', 'w') as file:
    i = 1
    for group in j_data['response']['items']:
        file.write(str(i)+'\t'+group['name']+'\n')
        i += 1
