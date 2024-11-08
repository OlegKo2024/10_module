print('Многопроцессное считывание')
from datetime import datetime
import multiprocessing
def read_info(name):
    all_data = []
    for file in name:
        with open(file, encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                all_data.append(line.strip())
    return all_data


filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]


if __name__ == '__main__':
    # Линейный вызов
    start_time = datetime.now()
    read_info(filenames)
    end_time = datetime.now()
    elapse_time = end_time - start_time
    print(elapse_time)

    # Многопроцессный
    start_time = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(read_info, filenames)
    end_time = datetime.now()
    elapse_time = end_time - start_time
    print(elapse_time)
