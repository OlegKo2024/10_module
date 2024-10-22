print('За честь и отвагу!')

from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        foes_number = 100
        days_fought = 0
        print(f'{self.name} на нас напали!')
        while foes_number > 0:
            foes_number -= self.power
            sleep(1)
            days_fought += 1
            print(f'{self.name} сражается {days_fought}..., осталось {foes_number} воинов')
        print(f'{self.name} одержал победу спустя {days_fought} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
# Вывод строки об окончании сражения
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
