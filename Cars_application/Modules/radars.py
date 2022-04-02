from pprint import pprint
from datetime import *


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

# violators = listSpeeders("box_a.txt", "box_b.txt", 60, 5)