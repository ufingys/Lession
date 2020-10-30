"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
my_file = open("text3.txt", "r", encoding="utf-8")
str_list = []
countWorker = {}
midvalue = 0
count = 0
try:
    for line in my_file:
        str_list = line.split()
        midvalue += float(str_list[1])
        if float(str_list[1]) < 20000:
            countWorker[str_list[0]] = float(str_list[1])
            print(float(str_list[1]))
        count += 1
    print(f"Средняя величина дохода сотрудников: {midvalue / count}")
    for key, val in countWorker.items():
        print(f"Меньше 20т.р. получает: {key} его зарпла = {val}")
except IOError:
    print("Input/output error")
except ValueError:
    print("Number format error")
except ZeroDivisionError:
    print("count = 0")
finally:
    my_file.close()