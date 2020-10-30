"""
Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


def str_gen(source_list):
    if source_list[0] == "One":
        return "Один" + " " + source_list[1] + " " + source_list[2] + "\n"
    elif source_list[0] == "Two":
        return "Два" + " " + source_list[1] + " " + source_list[2] + "\n"
    elif source_list[0] == "Three":
        return "Три" + " " + source_list[1] + " " + source_list[2] + "\n"
    elif source_list[0] == "Four":
        return "Четыре" + " " + source_list[1] + " " + source_list[2] + "\n"


my_file = open("text4.txt", "r")
new_file = open("new_text.txt", "w", encoding="utf-8")
str_list = []
try:
    for line in my_file:
        str_list = line.split()
        new_file.write(str_gen(str_list))
except IOError:
    print("Input/output error")
finally:
    my_file.close()
    new_file.close()
