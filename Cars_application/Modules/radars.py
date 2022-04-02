from pprint import pprint
from datetime import *

# 1. Введите справочную функцию fileToDictionary, которая имеет имя файла параметра. Эта функция должна считывать текстовое имя файла с камеры контроля скорости, которое содержит номер автомобиля, дату и время каждого проезда. Функция должна возвращать словарь с номером автомобиля в качестве ключа и временем в качестве значения для ключа.
# Пример запуска функции в файле box_a.txt, как показано на рисунке: (показаны только 3 первые записи)

# 'NB72826': '2022-01-03 07:11:41'
# 'ZH85499': '2022-01-03 07:15:56'
# 'FY99401': '2022-01-03 07:22:33'

def fileToDictionary(file, sep):
    dict_lines = {}
    with open(file) as file:
        lines = file.readlines()
    for line in lines:
        line_lst = line.split(sep)
        key, value = line_lst
        dict_lines[key] = value.strip()
    return dict_lines

def seconds_betweeen(date1: str, date2: str):
    FORMAT = "%Y-%m-%d %H:%M:%S"

    d1 = datetime.strptime(date1, FORMAT)
    d2 = datetime.strptime(date2, FORMAT)

    return (d2-d1).seconds


# pprint(fileToDictionary("box_a.txt", ", "))
# pprint(seconds_betweeen('2022-01-03 07:11:41', '2022-01-03 07:15:56'))

# 2. Напишите функцию listSpeeders, которая имеет четыре параметра filename_a, filename_b, speed_limit и distance. Первые два параметра — это имена файлов из камер контроля скорости A и B соответственно. Функция должна использовать метод fileToDictionary (имя файла) из пункта 1 для загрузки файлов.
# Функция должна возвращать словарь с регистрационным номером в качестве ключа для всех автомобилей, превысивших скоростной режим на заданное расстояние, значение ключа словаря должно быть кортежем из двух элементов: время нахождения на расстоянии и дата с временем. Разрешено превышение ограничения скорости на 5%, например. в зоне 60 км/ч штрафы/штрафы не налагаются при средней скорости до 63 км/ч.

# Пример словаря, возвращаемого функцией listSpeeders с двумя файлами, зарегистрированными на расстоянии 5 км и ограничении скорости 60 км/ч:

# {'FY99401': (72.289, '2022-01-03 07:22:33'), 'DA49644': (68.441, '2022-01-03 07:27:14'), 'SY60306': (78.260, '2022-01-03 08:03:11')}

def listSpeeders(filename_a, filename_b, speed_limit, distance):
    dict_a = fileToDictionary("Cars_application/Source/" + filename_a, ", ")
    dict_b = fileToDictionary("Cars_application/Source/" + filename_b, ", ")

    violators = {}
    
    for reg_num, date_time in dict_a.items():
        if reg_num in dict_b:
            date1 = date_time
            date2 = dict_b[reg_num]

            time_seconds = seconds_betweeen(date1, date2)
            speed_m_s = distance * 1000 / time_seconds
            speed_km_h = speed_m_s * 3.6

            if speed_km_h > speed_limit * 1.05:
                violators[reg_num] = (round(speed_km_h, 3), date1)
            
    return violators

violators = listSpeeders("box_a.txt", "box_b.txt", 60, 5)


# 5. 6. Создайте пункт меню для проверки нарушений скоростного режима. Для каждого транспортного средства необходимо просмотреть словарь из listSpeeders, если номер автомобиля зарегистрирован, необходимо создать и позаботиться об объекте типа SpeedTicket для рассматриваемого транспортного средства.



# 7. При чтении/записи в файл когда идет запуск/завершение программы эти тоже должны быть прочитаны/записаны. Совет: используйте pickle.
# !!!это означает, что мы будем читать из документа при запуске программы и сохранять в документ при завершении программы. И он хочет, чтобы мы использовали pickle(То же самое, что и во второй части, но так, чтобы это работало и со всем новым)