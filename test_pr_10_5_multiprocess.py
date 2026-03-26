'''
Контекстные менеджеры в Python — это мощный механизм для управления ресурсами, который упрощает работу с ними,
обеспечивая правильное их закрытие и освобождение, даже если произошла ошибка. Наиболее распространенный способ
использования контекстных менеджеров — это оператор `with`.
Примеры использования ниже:
 Контекстный менеджер часто используется для работы с файлами, чтобы гарантировать их закрытие после завершения работы:
- with open(file, encoding='utf-8') as file:
Контекстный менеджер `multiprocessing.Pool` может быть использован для создания пула процессов. В этом случае блок
`with` гарантирует, что процессы обязательно будут завершены корректно после завершения работы. Когда вы используете
оператор `with` с `multiprocessing.Pool`, вам не нужно явно вызывать методы `close()` и `join()`. Контекстный менеджер
автоматически вызывается на выходе из блока `with`
- with multiprocessing.Pool(processes=pr) as pool:
и еще проходили:
Использование `threading.Lock`:
- with lock:
Контекстные менеджеры могут использоваться для управления сетевыми сокетами и соединениями
 with SocketContextManager('localhost', 8080) as s:
       # Использование сокета
       s.sendall(b'Hello, World!')

'''

from datetime import datetime
import multiprocessing

print('Не правильно в том, что каждый процесс перемалывает все 4 файла, а надо на каждый по файлу')

# Вы правы: проблема в том, что каждый процесс получает все четыре файла, так что каждый файл считывается четырежды,
# что приводит к значительным накладным расходам. Чтобы это исправить, мы можем передать каждый файл в отдельный
# процесс. Для этого нужно убрать перебор файлов внутри read_info и передавать каждый файл отдельно.
def read_info_(name):
    all_data = []
    for file in name:
        with open(file, encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                all_data.append(line.strip())
    return all_data


# filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

# if __name__ == '__main__':
    # Линейный вызов
    # start_time = datetime.now()
    # # read_info(filenames)
    # end_time = datetime.now()
    # elapse_time = end_time - start_time
    # print(elapse_time)

    # Многопроцессный
    # start_time = datetime.now()
    # with multiprocessing.Pool(processes=4) as pool:
    #     pool.map(read_info, (filenames,))
    # end_time = datetime.now()
    # elapse_time = end_time - start_time
    # print(elapse_time)

# Контекстный менеджер в Python позволяет оборачивать выполнение определенных операций и управлять ресурсами с
# использованием `with` для автоматического управления входом и выходом из контекста. Это обеспечивает более безопасное
# и читаемое управление ресурсами, такими как файлы, сетевые подключения или блокировки (lock).

print('Переносим перебор файлов в отдельный процесс')

# def read_info(name):
#     all_data = []
#     with open(name, encoding='utf-8') as file:
#         lines = file.readlines()
#         for line in lines:              #  можно альтернативно while line:
#             all_data.append(line.strip())
#     return all_data


# filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
#
# if __name__ == '__main__':
#     # Линейный вызов
#     start_time = datetime.now()
#     for file in filenames:
#         read_info(file)
#     end_time = datetime.now()
#     elapse_time = end_time - start_time
#     print(elapse_time)                  # 0:00:08.334102
#
#     # Многопроцессный
#     start_time = datetime.now()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     end_time = datetime.now()
#     elapse_time = end_time - start_time
#     print(elapse_time)                  # 0:00:18.329463
#
#     print(multiprocessing.cpu_count())  # 8


print('Все функции с коротким вызовом')

def read_info_00(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:              #  можно альтернативно while line:
            all_data.append(line.strip())
    return all_data

def main_line_():
    start_time = datetime.now()
    for file in filenames:
        read_info_00(file)
    print('main_line_:', datetime.now() - start_time)


def main_mult_(pr=2):
    start_time = datetime.now()
    with multiprocessing.Pool(processes=pr) as pool:
        pool.map(read_info_00, filenames)
    print(f'main_mult_{pr}', datetime.now() - start_time)

filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    main_line_()
    main_mult_(pr=2)
    main_mult_(pr=4)
    main_mult_(pr=8)

print('Чтобы быстро поменять readlines() на readline()')

def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data

def main_line():
    start_time = datetime.now()
    for file in filenames:
        read_info(file)
    print('main_line:', datetime.now() - start_time)


def main_mult(pr=2):
    start_time = datetime.now()
    with multiprocessing.Pool(processes=pr) as pool:
        pool.map(read_info, filenames)
    print(f'main_mult{pr}', datetime.now() - start_time)

filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    main_line()
    main_mult(pr=2)
    main_mult(pr=4)
    main_mult(pr=8)