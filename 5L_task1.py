"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_file = open("text1.txt", "w")
try:
    while True:
        my_str = input("Введите строку чисел (для завершения нажмите 'enter'): ")
        if my_str == "":
            break
        my_file.write(my_str + "\n")
except IOError:
    print("Input/output error")
finally:
    my_file.close()