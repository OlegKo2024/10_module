
print('Обработка ошибок в потоках: try - except')

import threading
import time

def some_fun():
    time.sleep(1)
    raise Exception('it is gonna be ok')

def thread_fun():
    try:
        some_fun()
    except Exception as e:
        print(f'Wow - {e}')

t1 = threading.Thread(target=thread_fun())
t2 = threading.Thread(target=thread_fun())
t3 = threading.Thread(target=thread_fun())

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print('Обработка ошибок в потоках: exceptionhook')

import threading
import time

def some_fun():
    time.sleep(2)
    raise Exception('it is gonna be ok')
# 1. Определение функции исключений:
# Вы создаете свою функцию, например, def excepthook(args):, которая будет обрабатывать исключения. В этой функции вы
# можете определить, что именно делать при возникновении исключения (например, логирование или вывод сообщений)
def my_excepthook(args):
    print(args.thread.is_alive())
    print(args.thread.name)
# 2. Подключение функции к threading:
# С помощью выражения threading.excepthook = my_excepthook вы связываете вашу функцию с атрибутом модуля threading.
# Это значит, что теперь, когда произойдет необработанное исключение в любом из потоков, ваша функция excepthook будет
# вызвана с аргументами, которые содержат информацию о произошедшем исключении
# 3. Без ссылки на функцию:
# Если вы не назначите свою функцию на threading.excepthook, то в случае возникновения исключений в потоках будут
# срабатывать стандартные механизмы обработки исключений Python. Необработанные исключения приведут к завершению
# соответствующего потока, и вы получите сообщение об ошибке в консоли. Однако, программа в целом может продолжать
# выполнение (если это исключение произошло в одном из потоков, а не в основном потоке, который управляет запуском
# программы).

threading.excepthook = my_excepthook

# Присвоение ссылки на функцию
# Когда вы пишете <code>threading.excepthook = excepthook</code>, вы на самом деле присваиваете атрибуту
# threading.excepthook ссылку на функцию excepthook. Это означает, что в дальнейшем, когда возникнет необработанное
# исключение в потоке, модуль threading вызовет вашу функцию excepthook.
# ### 2. Почему без скобок
# - Без скобок (т.е. excepthook): Когда вы пишите только имя функции (без скобок), вы передаете ссылку на объект
# функции. Это позволяет другим частям кода ссылаться на эту функцию и, в определенный момент, вызывать ее.
# - С использованием скобок (т.е. excepthook()): Если бы вы написали <code>threading.excepthook = excepthook()</code>,
# это вызвало бы функцию excepthook сразу же, и результат выполнения этой функции (исключая саму функцию) был бы
# присвоен threading.excepthook. То есть, если внутри excepthook есть код, который вызывает исключение,
# программа завершится, не дождавшись вызова этой функции по событию.
# ### 3. Важно помнить
# Так что, чтобы кратко подытожить ваш вопрос:
# - <code>threading.excepthook = excepthook</code> — присваивает атрибуту threading.excepthook ссылку на вашу функцию
# excepthook, которая будет вызвана при возникновении исключения.
# - Это присвоение позволяет использовать обработчик исключений, сохраняя нормальную работу программы и позволяя
# выполнять специфические для вашего кода действия при возникновении ошибки.

t1 = threading.Thread(target=some_fun)
t2 = threading.Thread(target=some_fun)

t1.start()
t2.start()
t1.join()
t2.join()

print('Обработка ошибок в потоках: exception sys')

import threading
import sys
import time

def some_fun():
    time.sleep(3)
    raise Exception('it is gonna be ok')

def my_excepthook(args):
    print(args.thread.is_alive())
    print(args.thread.name)

threading.excepthook = my_excepthook


def my_excepthook_sys(args, a, b):
    print('handled')


threading.excepthook = my_excepthook_sys

t1 = threading.Thread(target=thread_fun())
t2 = threading.Thread(target=thread_fun())

t1.start()
t2.start()

t1.join()
t2.join()

# raise Exception





