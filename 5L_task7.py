"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

str_list = []
firm_dict = {}
firm_list = []
profit = 0
profit_average = 0
count_average = 0
try:
    with open("text7.txt", "r", encoding="utf-8") as my_file:
        for line in my_file:
            str_list = line.split()
            profit = int(str_list[2]) - int(str_list[3])
            firm_dict[str_list[0]] = profit
            if profit > 0:
                profit_average += profit
                count_average += 1
        firm_list.append(firm_dict)
        firm_list.append({"average_profit": profit_average / count_average})
        print(firm_list)
    with open("my_json_file.json", "w", encoding="utf-8") as firm_json_file:
        json.dump(firm_list, firm_json_file)
except IOError:
    print("Input/output error")
except ValueError:
    print("Error format numbers")