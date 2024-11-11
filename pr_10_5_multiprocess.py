# print('Многопроцессное считывание')
import multiprocessing
from datetime import datetime


def read_info_(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            all_data.append(line.strip())
    return all_data

# В функции read_info вы используете readlines() для считывания всех строк сразу, а по условиям задачи требуется
# считать файл построчно с помощью readline() в цикле. Это может повлиять на производительность.

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


def main_mult(pr):
    start_time = datetime.now()
    with multiprocessing.Pool(processes=pr) as pool:
        pool.map(read_info, filenames)
    print(f'main_mult{pr}', datetime.now() - start_time)


filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    main_line() # 6
    main_mult(2)    # 14
    main_mult(4)    # 12
    main_mult(8)    # 13
    print(multiprocessing.cpu_count())  # 8
