import threading
import requests
from datetime import datetime

print('Выполнение запроса долго - один бегунок')

start_time = datetime.now()
THE_URL = 'https://binaryjazz.com/wp-json/generator/v1/genre/'

res = []

for i in range(10):
    response = requests.get(THE_URL)
    page_response = response.json() # перевод формата интернета в формат Python
    res.append(page_response)

print(threading.enumerate())
print(threading.current_thread())

end_time = datetime.now()
elapse_time = end_time - start_time
print(elapse_time)  # 0:00:06.126190
print(res)

print('Выполнение запроса быстрее - с бегунками')

from threading import Thread, enumerate, current_thread
from datetime import datetime
import requests

THE_URL = 'https://binaryjazz.com/wp-json/generator/v1/genre/'

res = []
# Итак:
# - Изменение глобальной переменной (добавление элементов в список и т.д.) — можно без global, если мы меняем содержимое
# - Присвоение новой ссылки на переменную (перезапись) — требует использования global. См. закомментированный пример:
# res = []  # Глобальная переменная
#
# def func(url):
#     global res                        # Объявляем res как глобальную
#     response = requests.get(url)
#     page_response = response.json()
#     res = [page_response]
def func(url):
    response = requests.get(url)
    page_response = response.json()
    res.append(page_response)

start_time = datetime.now()

dwarf_01 = Thread(target=func, args=(THE_URL,))     # функция для выполнения и аргументы, который будут переданы
dwarf_02 = Thread(target=func, args=(THE_URL,))     # передавать надо кортеж
dwarf_03 = Thread(target=func, args=(THE_URL,))

dwarf_01.start()    # первый гномик побежал и так по каждому
dwarf_02.start()
dwarf_03.start()

print(threading.enumerate())
print(threading.current_thread())

dwarf_01.join()     # контроль того, что первый гномик прибежал и так по каждому
dwarf_02.join()
dwarf_03.join()

end_time = datetime.now()
elapse_time = end_time - start_time
print(elapse_time)  # 0:00:00.742800

print(res)

'''
поток есть общий MainThread(MainThread, started 13964), а может быть несколько MainThread(MainThread, started 13964)>,
<Thread(Thread-1 (func), started 2184)>, <Thread(Thread-2 (func), started 9744)>, <Thread(Thread-3 (func), started 6376)
- создание дополнительного потока: 
    - import threading
    - создание функции: def fun():
    - создание объекта класса Thread: object = threading.Thread(target=fun)
# Мы создаем объект класса Thread. Чтобы запускать поток, нужно вызвать метод start() этого объекта.
    - запуск потока: object.start()
    - если надо передать параметр: object = threading.Thread(target=fun, args=(x,))
    - если хотим, чтобы программа завершилась с завершением основного потока то: 
    object = threading.Thread(target=fun, args=(x,), deamon=True)
'''

