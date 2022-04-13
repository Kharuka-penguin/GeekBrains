# 1. Посмотреть документацию к API GitHub, разобраться как вывести список наименований репозиториев для конкретного
# пользователя, сохранить JSON-вывод в файле *.json.

import requests
import json
url = "https://api.github.com"

username = 'Kharuka-penguin'
params = {'accept': "application/vnd.github.v3+json",
          'username': username}

response = requests.get(url+'/users/'+username+'/repos', params=params)
j_data = response.json()
with open(username+'.json', 'w') as file:
    json.dump(j_data, file, indent=4)
