# Импорты необходимых модулей и функций
import threading
from time import sleep
import time

# Объявление функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for times in range(1, word_count+1):
            file.write(f"Какое-то слово №{times}\n")
            sleep(0.1)
    return print(f"Завершилась запись в файл {file_name}")

# Пример результата выполнения программы:

start_time = time.time() # Взятие текущего времени

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time() # Взятие текущего времени
print(f"Работа потоков: 0:00:{end_time - start_time:.6f}") # Вывод разницы начала и конца работы функций

#----------------------
start_time = time.time() # Взятие текущего времени

# Создание и запуск потоков с аргументами из задачи
examples = [threading.Thread(target=write_words(10, 'example5.txt')),
            threading.Thread(target=write_words(30, 'example6.txt')),
            threading.Thread(target=write_words(200, 'example7.txt')),
            threading.Thread(target=write_words(100, 'example8.txt'))]

for example in examples:
    example.start()

for example in examples:
    example.join()
#---------------------------------------------------------------
end_time = time.time() # Взятие текущего времени
print(f"Работа потоков: 0:00:{end_time - start_time:.6f}") # Вывод разницы начала и конца работы потоков
