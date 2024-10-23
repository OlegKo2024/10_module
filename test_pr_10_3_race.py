print('Банковские операции')

print('Лучшее решение')

# import threading
# from random import randint
# from time import sleep
#
# class Bank:
#
#     def __init__(self):
#         self.balance = 0
#         self.lock = threading.Lock()
#
#     def deposit(self):
#         for i in range(100):
#             random_deposit = randint(50, 500)
#             if self.balance >= 500 and self.lock.locked():
#                 self.lock.release()                       # освобождаем только если денег > 500 и закрыт
#             self.balance += random_deposit
#             print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
#             sleep(0.001)

# Метод deposit:
    # Будет совершать 100 транзакций пополнения средств.
    # Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
    # Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
    # После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
    # Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.

    # def take(self):
    #     for i in range(100):
    #         random_withdrawal = randint(50, 500)
    #         print(f'Запрос на {random_withdrawal}')
    #         if random_withdrawal <= self.balance:
    #             self.balance -= random_withdrawal
    #             print(f'Снятие: {random_withdrawal}. Баланс: {self.balance}')
    #         else:
    #             print(f'Запрос отклонён, недостаточно средств')
    #             self.lock.acquire()
# Метод take:
    # Будет совершать 100 транзакций снятия.
    # Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
    # В начале должно выводится сообщение "Запрос на <случайное число>".
    # Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие,
    # уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
    # Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать поток методом acquire.

# bk = Bank()
#
# # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
# th1 = threading.Thread(target=Bank.deposit, args=(bk,))
# th2 = threading.Thread(target=Bank.take, args=(bk,))
#
# th1.start()
# th2.start()
# th1.join()
# th2.join()

# print(f'Итоговый баланс: {bk.balance}')


print('Вариант 1: lock.acquire - lock.release')

# import threading
# from random import randint
# from time import sleep
#
# class Bank:
#
#     def __init__(self):
#         self.balance = 0
#         self.lock = threading.Lock()
#
#     def deposit(self):
#         for i in range(100):
#             random_deposit = randint(50, 500)
#             self.lock.acquire()
#             self.balance += random_deposit
#             print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
#             # if self.balance >= 500 and self.lock.locked():
#             self.lock.release()
#             sleep(0.001)
#
#     def take(self):
#         for i in range(100):
#             random_withdrawal = randint(50, 500)
#             print(f'Запрос на {random_withdrawal}')
#             if random_withdrawal <= self.balance:
#                 self.lock.acquire()
#                 self.balance -= random_withdrawal
#                 print(f'Снятие: {random_withdrawal}. Баланс: {self.balance}')
#                 self.lock.release()
#             else:
#                 print(f'Запрос отклонён, недостаточно средств для поддержания минимального остатка')
#
#
# bk = Bank()
#
# # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
# th1 = threading.Thread(target=Bank.deposit, args=(bk,))
# th2 = threading.Thread(target=Bank.take, args=(bk,))
#
# th1.start()
# th2.start()
# th1.join()
# th2.join()

# print(f'Итоговый баланс: {bk.balance}')

print('Вариант 2: with lock')

import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            random_deposit = randint(50, 500)
            with self.lock:                             # Защита доступа к балансу
                self.balance += random_deposit          # if self.balance >= 500: # and self.lock.locked(): - not used
                print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_withdrawal = randint(50, 500)
            print(f'Запрос на {random_withdrawal}')
            if random_withdrawal <= self.balance:
                with self.lock:                             # Блокируем доступ к балансу
                    self.balance -= random_withdrawal
                    print(f'Снятие: {random_withdrawal}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
            sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

print('Вариант 3: try - finally')

# import threading
# from random import randint
# from time import sleep
#
# class Bank:
#
#     def __init__(self):
#         self.balance = 0
#         self.lock = threading.Lock()
#
#
#     def deposit(self):
#         for i in range(100):
#             random_deposit = randint(50, 500)
#             try:
#                 self.lock.acquire()
#                 self.balance += random_deposit
#                 print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
#                 # if self.balance >= 500 and self.lock.locked():
#             finally:
#                 self.lock.release()
#             sleep(0.001)
#
#     def take(self):
#         for i in range(100):
#             random_withdrawal = randint(50, 500)
#             print(f'Запрос на {random_withdrawal}')
#             if random_withdrawal <= self.balance:
#                 try:
#                     self.lock.acquire()
#                     self.balance -= random_withdrawal
#                     print(f'Снятие: {random_withdrawal}. Баланс: {self.balance}')
#                 finally:
#                     self.lock.release()
#             else:
#                 print(f'Запрос отклонён, недостаточно средств')
#
#
# bk = Bank()
#
# # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
# th1 = threading.Thread(target=Bank.deposit, args=(bk,))
# th2 = threading.Thread(target=Bank.take, args=(bk,))
#
# th1.start()
# th2.start()
# th1.join()
# th2.join()
#
# print(f'Итоговый баланс: {bk.balance}')