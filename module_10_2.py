import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def fighting(self, name, power, enemies):
        days = 0
        while enemies:
            days += 1
            enemies -= power
            sleep(1)
            print(f"{name} сражается {days} день(дня)..., осталось {enemies} воинов.")
        print(f"{name} одержал победу спустя {days} дней(дня)!")

    def run(self):
        print(f"{self.name}, на нас напали!")
        self.fighting(self.name, self.power, enemies=100)

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
# Вывод строки об окончании сражения
first_knight.join()
second_knight.join()
print("Все битвы закончились!")