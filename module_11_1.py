import requests

#1 получаем данные с сайта
response = requests.get('https://httpbin.org/get')
print(response.json())
#2 отправляем данные из payload на сервер, пост запросом
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.json())
#3 отправляем запрос на сайт с измененным юзер-агентом
headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json())
