print('Банковские операции')

import threading
from random import randint
from time import sleep

class Bank:

    def __init__(self):
        self.balance = 0    # инициализируем - присваиваем значение переданного параметра - инициализация атрибута balance
# self.balance = 0`: создается атрибут `balance` экземпляра `Bank`, будет использоваться для хранения текущего баланса
        self.lock = threading.Lock()    # Инициализация атрибута lock, который является экземпляром Lock

# self.lock = threading.Lock()`: создается объект блокировки (lock), который будет использоваться для синхронизации
# доступа к общему ресурсу, в данном случае к `self.balance`
# `Lock`:
#- `self.lock = threading.Lock()` создаёт экземпляр класса `Lock`. Этот экземпляр (например, `self.lock`) предназначен
    # для управления доступом к общему ресурсу (в вашем случае — переменной `self.balance`).
#- `Lock()` предоставляет методы для захвата и освобождения блокировки, которые гарантируют, что только один поток может
    # изменять `self.balance` в данный момент времени.

# 1. Переменная `self.lock`
# `self.lock` указывает на объект
# - Когда вы создаёте объект блокировки с помощью `self.lock = threading.Lock()`, переменная `self.lock` действительно
# становится ссылкой на созданный объект блокировки.
# - Этот объект предоставляет методы, такие как `acquire()` и `release()`, которые позволяют управлять доступом к
# общим ресурсам в многопоточном окружении.
# Таким образом, когда вы выполняете, например, `self.lock.acquire()`, вы вызываете метод `acquire()` на объекте, на
# который ссылается `self.lock`. Это означает, что `self.lock` контролирует доступ к критическим секциям кода, где
# происходят изменения `self.balance`.
# 2. "Присваивается результат создания объекта Lock"
# Когда мы говорим, что "присваивается результат создания объекта `Lock`", мы имеем в виду следующее:
# - Создание объекта: Когда вы вызываете `threading.Lock()`, это приводит к созданию нового экземпляра класса `Lock`.
# - Возврат объекта: Конструктор `Lock` возвращает ссылку на созданный объект. Это означает, что теперь у нас есть
# доступ к методу и атрибутам этого объекта.
# - Присвоение ссылке: Вы присваиваете возвращаемое значение (ссылку на объект `Lock`) атрибуту `self.lock`.
# Теперь `self.lock` ссылается на этот объект.
    def deposit(self):
        for i in range(100):
            random_deposit = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()  # освобождаем только если денег > 500 и закрыт
            self.balance += random_deposit
            print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_withdrawal = randint(50, 500)
            print(f'Запрос на {random_withdrawal}')
            if random_withdrawal <= self.balance:
                self.balance -= random_withdrawal
                print(f'Снятие: {random_withdrawal}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()     # Создаётся экземпляр класса Bank

# Основной поток выполняет действия по изменению банковского счёта (добавление и снятие средств) не напрямую, а через
# потоки, которые работают с одним и тем же объектом `bk`. То есть операции `deposit` и `take` выполняются в потоках,
# управляемых основным потоком - то есть опосредованно. Основной поток:
# - создает экземпляр класса `Bank` - с переменной bk, которая ссылается на данный объект. В этом шаге вызывается
# метод `__init__`, который инициализирует атрибуты объекта переменной `bk` (включая `self.balance` и `self.lock`)
# - создал и запустил два потока - start()
# - Ожидает завершения потоков - join()
# - Вывел итоговый результат - print()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

print(threading.enumerate())
print(threading.current_thread())

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

print('Вариант 2: with lock')


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            random_deposit = randint(50, 500)
            with self.lock:  # Защита доступа к балансу
                self.balance += random_deposit  # if self.balance >= 500: # and self.lock.locked(): - not used
                print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_withdrawal = randint(50, 500)
            print(f'Запрос на {random_withdrawal}')
            if random_withdrawal <= self.balance:
                with self.lock:  # Блокируем доступ к балансу
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


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    # def deposit(self):
    #     for i in range(100):
    #         random_deposit = randint(50, 500)
    #         try:
    #             self.lock.acquire()
    #             self.balance += random_deposit
    #             print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
    #             # if self.balance >= 500 and self.lock.locked():
    #         finally:
    #             self.lock.release()
    #         sleep(0.001)

    def deposit(self):
        try:
            self.lock.acquire()
            for i in range(100):
                random_deposit = randint(50, 500)
                self.balance += random_deposit
                print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
            # if self.balance >= 500 and self.lock.locked():
        finally:
            self.lock.release()
        sleep(0.001)

    def take(self):
        for i in range(100):
            random_withdrawal = randint(50, 500)
            print(f'Запрос на {random_withdrawal}')
            if random_withdrawal <= self.balance:
                try:
                    self.lock.acquire()
                    self.balance -= random_withdrawal
                    print(f'Снятие: {random_withdrawal}. Баланс: {self.balance}')
                finally:
                    self.lock.release()
            else:
                print(f'Запрос отклонён, недостаточно средств')
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
