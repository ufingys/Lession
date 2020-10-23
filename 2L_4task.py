"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
string = input("Введите строку из слов разделенных пробелами: ")
res_str = ''
str_list = []
flag = True
index = 0
for i in range(len(string)):
    if string[i] != ' ':
        res_str = res_str + string[i]
        flag = True
        continue
    if flag:
        str_list.append((index, res_str))
        index += 1
        res_str = ''
        flag = not flag
str_list.append((index, res_str))
for i, word in str_list:
    print(f"{i} {word}")
