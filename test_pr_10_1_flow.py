print('Потоковая запись в файлы')

print('Запись типа i слов')
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')  # Теперь будет 10
write_words(30, 'example2.txt')  # Теперь будет 30
write_words(200, 'example3.txt')  # Теперь будет 200
write_words(100, 'example4.txt')  # Теперь будет 100

print('Запись типа i слов, но добавляем меняя значение переменной start_number - интересно, но не для этого задания')
# from time import sleep
#
# def write_words(word_count, file_name):
#     start_number = 1  # Начинаем с единицы
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for i in range(word_count):
#             file.write(f'Какое-то слово № {start_number}\n')
#             start_number += 1  # Увеличиваем номер слова
#             sleep(0.1)  # Пауза 0.1 секунды
#     print(f'Завершилась запись в файл {file_name}')
#
# # Вызовы функции
# write_words(10, 'example1.txt')
# write_words(30, 'example2.txt')
# write_words(200, 'example3.txt')
# write_words(100, 'example4.txt')

print('Как записывать, с конца предыдущего до конца текущего - обновляем total_word_count после каждого перебора')
# from time import sleep
#
# total_word_count = 0
#
# def write_words(word_count, file_name):
#     global total_word_count
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for i in range(total_word_count + 1, total_word_count + word_count + 1):
#             file.write(f'Какое-то слово № {i}\n')
#             sleep(0.1)
#     # Обновляем общее количество слов
#     total_word_count += word_count
#     print(f'Завершилась запись в файл {file_name}')
#
# # Вызов функции с указанными параметрами
# write_words(10, 'example1.txt')  # Теперь будет от 0 до 10
# write_words(30, 'example2.txt')  # Теперь будет 11 до 40
# write_words(200, 'example3.txt')  # Теперь будет от 41 до 240
# write_words(100, 'example4.txt')  # Теперь будет от 241 до 340


print('Чтобы накапливать и записывать, но один раз с добавлением атрибута current_count, который возвращается')

# В каждом из вызовов переменная current_count обновляется новым значением, что позволяет корректно подсчитывать
# количество написанных слов. Как это происходит:
# c первым запуска current_count = 0, далее current_count += word_count = 10, далее return current_count и это значит
# переменная current_count становится 10, она же передается в функцию при втором запуске в write_words(current_count...
# current_count = write_words(current_count, 30, 'example2.txt') и в конце получаем на возврат 40 и так далее...

# from time import sleep
#
# def write_words(current_count, word_count, file_name):
#     current_count += word_count
#     with open(file_name, 'w', encoding='utf-8') as file:
#         file.write(f'Какое-то слово № {current_count}\n')
#         sleep(0.1)
#     print(f'Завершилась запись в файл {file_name}')
#     return current_count
#
# # Начальное количество слов
# current_count = 0
#
# # Записываем слова в файлы, обновляя количество
# current_count = write_words(current_count, 10, 'example1.txt')  # Какое-то слово № 10
# current_count = write_words(current_count, 30, 'example2.txt')  # Какое-то слово № 40
# current_count = write_words(current_count, 200, 'example3.txt')  # Какое-то слово № 240
# current_count = write_words(current_count, 100, 'example4.txt')  # Какое-то слово № 340

print('Чтобы накапливать и записывать, но один раз и с global')

# from time import sleep
#
# total_count = 0
# def write_words(word_count, file_name):
#     global total_count
#     total_count += word_count
#     with open(file_name, 'w', encoding='utf-8') as file:
#         file.write(f'Какое-то слово № {total_count}\n')
#         sleep(0.1)
#     print(f'Завершилась запись в файл {file_name}')
#
#
# # Записываем слова в файлы, обновляя количество
# write_words(10, 'example1.txt')  # Какое-то слово № 10
# write_words(30, 'example2.txt')  # Какое-то слово № 40
# write_words(200, 'example3.txt')  # Какое-то слово № 240
# write_words(100, 'example4.txt')  # Какое-то слово № 340
