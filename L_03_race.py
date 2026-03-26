'''
print('Проблемы многопоточного программирования, блокировки и обработка ошибок')

import threading

x = 0
def thread_task():
    global x
    for i in range(1_000_000):
        x = x + 1

def fun():
    global x
    x = 0
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    fun()
    print(x, end=' ')   # 2000000 2000000 2000000 2000000 2000000 2000000 2000000 2000000 2000000 2000000

# у меня получились 20 000 000, но у тех у кого более ранняя версия не получается из-за проблемы, что оба потока берут
# одну и туже цифру одновременно и теряют единицу на потере последовательности. Обходят эту проблему атомарной (в одно
# действие) операцией, если не возможно, то проблема решается блокировкой - узким горлышком, когда только один поток
# может получить доступ к действию
'''
# Последовательность:
# - for - fun
# - fun - х=0 - создание и запуск потоков по целевой функции - thread_task
# - thread_task - х+1 по двум потокам 1 млн. раз - конечное значение
# - печать конечного значения и новый цикл
# - и так 10 раз
'''

print('Блокировка - реализация этого решений через lock')


from threading import Thread, Lock


lock = Lock()
x = 0
def thread_task():
    global x
    for i in range(1000000):
        lock.acquire()      # когда зашел один, второй не может зайти - закрыто
        x = x + 1
        lock.release()      # когда один, вышел второй может войти - открыто

def main():
    global x
    x = 0
    t1 = Thread(target=thread_task)
    t2 = Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main()
    print(x, end=' ')   # 2000000 2000000 2000000 2000000 2000000 2000000 2000000 2000000 2000000 2000000 - о работает
                        # чуть дольше, так как два потока одновременно не работают, а по одному получают доступ к x
                        # но тогда и смысла в двух потоках нет, еще и медленнее, чем даже работает один поток.

print('Блокировка - реализация этого решений через WITH lock')

from threading import Thread, Lock


lock = Lock()
x = 0
def thread_task():
    global x
    for i in range(1000000):
        with lock:
            x = x + 1

def main():
    global x
    x = 0
    t1 = Thread(target=thread_task)
    t2 = Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main()
    print(x, end=' ')   # 2000000 2000000 2000000 2000000 2000000 2000000 2000000 2000000 2000000 2000000

print('Взаимоблокировка - проблема, когда два потока заблокировали друг друга')

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def threading_task1():
    lock1.acquire()
    print('Thread 1 lock1 acquired')
    time.sleep(1)
    lock2.acquire()
    print('Thread 1 lock2 acquired')
    lock2.release()
    lock1.release()

def threading_task2():
    lock2.acquire()
    print('Thread 2 lock2 acquired')
    time.sleep(1)
    lock1.acquire()
    print('Thread 2 lock1 acquired')
    lock1.release()
    lock2.release()

t1 = threading.Thread(target=threading_task1())
t2 = threading.Thread(target=threading_task2())

# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


print('Решение с try and finally')

from threading import Thread, Lock

lock = Lock()
x = 0

# def thread_task():
#     global x
#     for i in range(1000000):
#         with lock:
#             x = x + 1
def thread_task():          # альтернатива для WITH
    global x
    for i in range(1000000):
        try:
            lock.acquire()
            x = x + 1
        finally:
            lock.release()

def main():
    global x
    x = 0
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main()
    print(x, end=' ')
'''
print('Новая лекция')

import threading

counter = 0
lock = threading.Lock()
print(lock.locked())

def plus(name):
    global counter
    lock.acquire()
    for _ in range(1000):
        counter += 1
        print(name, counter, lock.locked())
    lock.release()

def minus(name):
    global counter
    with lock:
        for _ in range(1000):
            counter -= 1
            print(name, counter, lock.locked())

def try_me(name):
    counter = 0
    try:
        lock.acquire()
        for i in range(1000):
            counter += i
            print(name, counter, lock.locked())
    except Exception as ex:
        print(f"Произошла ошибка в потоке {name}: {ex}")
    finally:
        lock.release()



plus_01 = threading.Thread(target=plus, args=('p01',))
minus_01 = threading.Thread(target=minus, args=('m01',))
plus_02 = threading.Thread(target=plus, args=('p02',))
minus_02 = threading.Thread(target=minus, args=('m02',))
try_me_00 = threading.Thread(target=try_me, args=('tm',))

plus_01.start()
minus_01.start()
plus_02.start()
minus_02.start()
try_me_00.start()

# plus_01.join()
# minus_01.join()
# plus_02.join()
# minus_02.join()

'''
Ключевые моменты:
первое - создаем объект lock = threading.Lock()
три варианта, постановки замка:
    - первый lock.acquire() / lock.release() ставим перед циклом / после цикла
    - второй with lock: - опять перед циклом, не требует снятия - сам снимает
    - третий try: - lock.acquire() - цикл finally: lock.release()
но смотри вариант и описание практики:
    - lock.release(), если deposit выполнил условия достаточности денег
    - lock.acquire(), если денег не хватает для снятия
'''