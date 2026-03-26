print('Очереди в потоках')

from threading import Thread
from time import sleep
import queue

def producer(que):
    c = 0
    while c < 5:
        c += 1
        message = f'ping - {c}'
        que.put(message)

def consumer(que):
    while not que.empty():
        message = que.get()
        print(message)
        sleep(1)

q = queue.Queue()

tr1 = Thread(target=producer, args=(q,))
tr2 = Thread(target=consumer, args=(q,))

tr1.start()
tr2.start()
tr1.join()
tr2.join()

print('New school')

from threading import Thread, current_thread
from queue import Queue
from time import sleep

print('Идея')

q = Queue()
q.put('Nikita')
print(q.get(timeout=2))
print('Конец')

print('Реализация')
def getter(queue):
    while True:         # или можно задать while not queue.empty()
        sleep(5)
        item = queue.get()
        print(current_thread(), 'взял элемент ', item)

q = Queue(maxsize=3)   # параметр maxsize - if hit, то не сможем ничего положить, пока место в очереди не освободится

thread = Thread(target=getter, args=(q,), daemon=True)  # так как while True, чтобы программа могла завершиться, добавим
# daemon=True, который завершит программу ДОПОЛНИТЕЛЬНОГО потока, если завершится основной поток
thread.start()

for i in range(10): # ОСНОВНОЙ ПОТОК
    sleep(2)
    q.put(i)
    print(current_thread(), 'положил в очередь', i)
# Очередь `q` создается в начале программы, и она передается в поток, который выполняет функцию `getter`. Здесь
# очередь служит для синхронизации данных между потоками.
# - В этой структуре:
#   - Поток `getter` извлекает элементы из очереди.
#   - Основной поток добавляет числа в очередь (через `q.put(i)`).
# По сути, создание объекта `Queue` необходимо, когда вы хотите, чтобы потоки могли взаимодействовать. Очередь позволяет
# потокам передавать данные и синхронизировать свое выполнение. Ваши примеры показывают, как можно использовать один и
# тот же объект очереди для разных потоков, а также как реализуется взаимодействие между потоками через одну и ту же
# очередь, что особенно удобно для синхронизации работы.

print('делаем поток daemon')
# Что такое демон-поток?
# Демон-поток (или поток-демон) — это специальный тип потока в Python, который работает в фоновом режиме и не блокирует
# завершение программы.

# from threading import Thread
# import time
#
# def background_task():
#     while True:
#         print("Демон-поток работает...")
#         time.sleep(1)
#
# # Создаем и запускаем демон-поток
# daemon_thread = Thread(target=background_task, daemon=True)
# daemon_thread.start()
#
# # Основной поток
# for i in range(5):
#     print("Главный поток работает...")
#     time.sleep(2)
#
# print("Главный поток завершен.")
