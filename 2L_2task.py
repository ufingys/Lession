"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
my_list = []
element = input("Введите элемент списка (для завершения введите 'q'): ")
while element != 'q':
    try:
        my_list.append(int(element))
    except ValueError:
        my_list.append(element)
    element = input("Введите элемент списка (для завершения введите 'q'): ")
print(my_list)
for i in range(0, len(my_list), 2):
    if i + 1 >= len(my_list):
        break
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)





