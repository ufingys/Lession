"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""

def parse_string(string):
    numb_list = []
    string += ' '
    begin = 0
    notspan = True
    quit = False
    for i in range(len(string)):
        if string[i] == chr(32) or string[i] == 'q':
            if notspan:
                numb_list.append(int(string[begin:i]))
                notspan = False
            if string[i] == 'q':
                quit = True
                break
            continue
        if not notspan:
            begin = i
        notspan = True
    return numb_list, quit

while True:
    numbers = input("Введите строку чисел (для завершения ввода введите 'q'): ")
    result = parse_string(numbers)
    print(sum(result[0]))
    if result[1]:
        break