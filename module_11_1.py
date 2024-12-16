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

#---------------------------------------------------------------------------
import numpy as np

# создание массива матрицы
matrix = np.array([[1, 1, 1], [2, 2 ,2], [3, 3, 3]])
print(matrix)

# созданный массив можно изменять и так же можно "мутировать"
a_array = np.array([321, 210, 987, 65, 43, 0])
print(a_array)
a_array[2] = 999
print(a_array)
b_array = a_array[3:]
print(b_array)
b_array[2] = 123
print(a_array)

# генерация рандомного массива чисел
r_array = np.random.random((3, 3))
print(r_array)

#---------------------------------------------------------------------
import matplotlib.pyplot as plt

# Линейный график
xline = np.linspace(0, 10, 100)
plt.plot(xline, np.sin(xline)) # синус x линии
plt.title('Линейный')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Гистограмма
hist = np.random.randn(1000)
plt.hist(hist, bins=30, alpha=0.3, color='r')
plt.title('Гистограмма')
plt.show()

# Столбчатая таблица
cbar = ['X', 'Y', 'Z']
cval = [9, 3, 7]
plt.bar(cbar, cval)
plt.title('Столбцы')
plt.show()
