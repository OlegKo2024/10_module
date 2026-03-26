print('Многопроцессное программирование')
# Потоки существуют внутри одного процесса и работают с общими ресурсами этого процесса. Однако у процессов, по сути,
# своя область памяти и свой внутренний GIL (Global Interpreter Lock). То есть, когда мы говорим о потоках, мы говорим
# о конкурентном выполнении кода. Когда мы говорим о процессах, мы говорим о ПАРАЛЛЕЛЬНОМ выполнении на разных ядрах
# вашего процессора



# Создадим функцию «first_worker», которая будет принимать «n», то есть значение, на которое нужно увеличить наш счётчик.
# В функции будет цикл на «n» раз, который будет увеличивать этот счётчик каждую секунду. После выполнения работы мы
# выведем информацию о том, что "Первый рабочий изменил значение счётчика, и теперь он равен counter

import multiprocessing
import time
import threading

# counter = 0
# def first_worker(n):
#     global counter
#     for _ in range(n):
#         counter += 1
#         time.sleep(1)
#     print(f'Первый рабочий изменил значение счётчика, и теперь он равен {counter}')
#
# def second_worker(n):
#     global counter
#     for _ in range(n):
#         counter += 1
#         time.sleep(1)
#     print(f'Второй рабочий изменил значение счётчика, и теперь он равен {counter}')
#
# thread_1 = threading.Thread(target=first_worker, args=(10,))
# thread_2 = threading.Thread(target=second_worker, args=(5,))
#
# thread_1.start()
# thread_2.start()

print('Но что, если поменять threading на multiprocessing')
# Когда вы используете `multiprocessing`, каждый процесс получает свой собственный адресное пространство и не может
# напрямую разделять глобальные переменные. Это означает, что изменение глобальной переменной `counter` в одном процессе
# не будет затрагивать ее значение в другом процессе. Таким образом, при запуске `first_worker_` и `second_worker_`,
# каждый из них работает с отдельной копией `counter`, и любые изменения не будут видны другим процессам.

# Результат:
# Рабочий второй изменил значение счётчика, и теперь он равен 5
# Рабочий первый изменил значение счётчика, и теперь он равен 10

counter = 0
def first_worker_(n):
    global counter
    for _ in range(n):
        counter += 1
        time.sleep(1)
        print(f'Рабочий первый запустил счётчик, он равен {counter}')
    print(f'Рабочий первый изменил значение счётчика, и теперь он равен {counter}')

def second_worker_(n):
    global counter
    for _ in range(n):
        counter += 1
        time.sleep(1)
        print(f'Рабочий второй запустил счётчик, он равен {counter}')
    print(f'Рабочий второй изменил значение счётчика, и теперь он равен {counter}')


if __name__ == '__main__':
    pro_1 = multiprocessing.Process(target=first_worker_, args=(10,))
    pro_2 = multiprocessing.Process(target=second_worker_, args=(5,))

    pro_1.start()
    pro_2.start()
