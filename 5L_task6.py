"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def parse_num(num_str):
    if len(num_str) == 0:
        return 0
    if ord(num_str[0]) >= 48 and ord(num_str[0]) <= 57:
        return (ord(num_str[0]) - 48) + parse_num(num_str[0+1:len(num_str)]) * 10
    return parse_num(num_str[0+1:len(num_str)])


my_file = open("text6.txt", "r", encoding="utf-8")
str_list = []
my_dict = {}
try:
    for line in my_file:
        summa = 0
        str_list = line.split()
        for i in range(1, len(str_list)):
            summa += parse_num(str_list[i][::-1])
        my_dict[str_list[0]] = summa
    print(my_dict)
except IOError:
    print("Input/output error")
finally:
    my_file.close()