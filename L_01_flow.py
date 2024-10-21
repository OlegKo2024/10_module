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

end_time = datetime.now()
elapse_time = end_time - start_time
print(elapse_time)  # 0:00:06.126190
print(res)

print('Выполнение запроса быстрее - с бегунками')

from threading import Thread
from datetime import datetime
import requests

THE_URL = 'https://binaryjazz.com/wp-json/generator/v1/genre/'

res = []
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

dwarf_01.join()     # контроль того, что первый гномик прибежал и так по каждому
dwarf_02.join()
dwarf_03.join()

end_time = datetime.now()
elapse_time = end_time - start_time
print(elapse_time)  # 0:00:00.742800

print(res)



