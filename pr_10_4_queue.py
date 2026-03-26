print('Потоки гостей в кафе')

from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def __str__(self):
        return str(self.number)

class Guest(Thread):
    def __init__(self, name, ):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
# Каждый раз, когда вам необходимо использовать очередь для передачи данных между потоками, вы должны создать экземпляр
# `Queue`. Эта очередь будет управлять элементами, которые потоки могут добавлять (положить в очередь) и забирать
# (взять из очереди).
# Здесь вы создаете объект очереди `self.queue` в методе `__init__` класса `Cafe`. Этот объект используется в методах
#`guest_arrival` и `discuss_guests` для хранения гостей, которые ожидают своего стола. Очередь создается один раз, и
# эта же очередь используется в нескольких методах класса, что позволяет централизиовать управление потоком гостей.

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):  # хотя бы один не None
            for table in self.tables:  # проходим по столам
                if table.guest is not None and not table.guest.is_alive():  # если типа сидят и не заказывают
                    print(f'{table.guest.name} покушал(а) и ушел')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:  # если очередь не пуста и стол свободен
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(а) из очереди и сел(а) за стол номер {table.number}')
                    table.guest.start()


# Создание объектов столов
tables = [Table(number) for number in range(1, 6)]
print(tables)
result = (", ".join(str(table) for table in tables))
print(result)
print(type(result))
# Метод join() вызывается на строке ", " (которая является строкой-разделителем). Он объединяет строки, возвращенные
# генератором, в одну строку, вставляя между ними запятую и пробел. В результате вы получаете одну строку: 1, 2, 3, 4, 5
# Хотя join() используется в обоих контекстах (строки и потоки), важно различать их по назначению:
# str.join() — помогает склеить строки, чтобы получить удобный для чтения вывод.
# Thread.join() — используется, чтобы сделать основной поток программы «пауза», пока дочерний поток выполняет свою
# работу, обеспечивая синхронизацию.

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
