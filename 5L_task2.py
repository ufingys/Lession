"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_file = open("text2.txt", "r")
str_list = []
countStr = 0
countWord = []
try:
    for line in my_file:
        str_list = line.split()
        countStr += 1
        countWord.append(len(str_list))
except IOError:
    print("Input/output error")
finally:
    my_file.close()
print("Количество строк: %d" %countStr)
for i in range(len(countWord)):
    print(f"Количество слов в строке {i+1} = {countWord[i]}")
