"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

my_file = open("text5.txt", "r+")
num_list = []
summa = 0
try:
    for i in range(20):
        random.seed
        num = int(random.random() * 1000)
        my_file.write(str(num) + " ")
    my_file.seek(0)
    num_list = my_file.read().split()
    for x in num_list:
        summa +=  int(x)
    print(f"Сумма чисел = {summa}")
except IOError:
    print("Input/output error")
except ValueError:
    print("Error format numbers")
finally:
    my_file.close()