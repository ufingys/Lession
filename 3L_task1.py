"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def division(value1, value2):
    try:
        return value1 / value2
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        return

while True:
    print("Введите числа для деления (для завершения ввода введите 'любой символ')")
    try:
        numb1 = float(input("Введите число №1: "))
        numb2 = float(input("Введите число №2: "))
        print(division(numb1, numb2))
    except ValueError:
        print("end")
        break