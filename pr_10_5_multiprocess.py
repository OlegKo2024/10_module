# print('Многопроцессное считывание')
import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            all_data.append(line.strip())
    return all_data


filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    # Линейный вызов
    start_time = datetime.now()
    for file in filenames:
        read_info(file)
    end_time = datetime.now()
    elapse_time = end_time - start_time
    print(elapse_time)                  # 0:00:08.334102

    # Многопроцессный
    start_time = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    elapse_time = end_time - start_time
    print(elapse_time)                  # 0:00:18.329463

    print(multiprocessing.cpu_count())  # 8
