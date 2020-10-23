"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
def my_func(arg1, arg2, arg3):
    t = arg1
    if arg2 < t:
        t = arg2
    if arg3 < t:
        t = arg3
    return (arg1 + arg2 + arg3) - t

print("Сумма наибольших из двух чисел")
try:
    numb1 = float(input("Введите число №1: "))
    numb2 = float(input("Введите число №2: "))
    numb3 = float(input("Введите число №3: "))
    print(my_func(numb1, numb2, numb3))
except ValueError:
    print("Неправильный формат чисел..")