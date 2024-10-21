print('Потоковая запись в файлы')
print('Вызовем 4 раза функцию')
from time import sleep
from datetime import datetime
from threading import Thread

start_time = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = datetime.now()
elapse_time_01 = end_time - start_time
print(elapse_time_01)

print('Вызовем 4 гномика')

start_time = datetime.now()
dwarf_01 = Thread(target=write_words, args=(10, 'example5.txt')) # помним, что передаем кортеж и так по каждому
dwarf_02 = Thread(target=write_words, args=(30, 'example6.txt'))
dwarf_03 = Thread(target=write_words, args=(200, 'example7.txt'))
dwarf_04 = Thread(target=write_words, args=(100, 'example8.txt'))

dwarf_01.start()    # первый гномик побежал и так по каждому
dwarf_02.start()
dwarf_03.start()
dwarf_04.start()

dwarf_01.join()     # контроль первый гномик прибежал и так по каждому
dwarf_02.join()
dwarf_03.join()
dwarf_04.join()

end_time = datetime.now()
elapse_time_02 = end_time - start_time
print(elapse_time_02)
print(elapse_time_01 - elapse_time_02)