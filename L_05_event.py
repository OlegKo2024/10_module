import time

print('Класс Event')

from threading import Thread, Event
from time import sleep


def worker01():
    print('Первый начал работу')
    event.wait()
    print('Первый продолжил работу')
    time.sleep(3)
    print('Первый закончил всю работу')

def worker02():
    print('Второй начал работу')
    time.sleep(5)
    print('Второй закончил всю работу')
    event.wait(timeout=5)
    event.set()

event = Event()

w01 = Thread(target=worker01)
w02 = Thread(target=worker02)

w01.start()
w02.start()

print('all methods')

event01 = Event()
event01.set()
print(event01.is_set())
event01.clear()
print(event01.is_set())

# Если мы обратим внимание, то у класса Event, как мы уже упоминали, есть флаг. Проверить состояние этого флага мы
# можем, вызвав метод «is_set()». Он вернёт значение флага, и при запуске кода мы увидим, что в результате работы
# «is_set()» наш флаг равен «False», то есть пока никакого события не произошло

# Если нам необходимо сбросить состояние флага, потому что эти состояния могут меняться в процессе выполнения программы,
# мы можем вызвать метод «clear()». Этот метод сбросит состояние события на «False». Если мы установим его через «set()»,
# а затем вызовем «clear()» и попробуем вывести значение нашего события, то в результате получим «False»
