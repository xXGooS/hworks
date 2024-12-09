import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rand_deposit = randint(50, 500)
            self.balance += rand_deposit
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {rand_deposit}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            rand_take = randint(50, 500)
            print(f"Проверка на {rand_take}")
            if rand_take <= self.balance:
                self.balance -= rand_take
                print(f"Снятие {rand_take}. Баланс: {self.balance}")
            else:
                print("Запрос отклонен, недостаточно средств")
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')