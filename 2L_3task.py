"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
# решение через список
while True:
    month = int(input("Введите номер месяца: "))
    if month >= 1 and month <= 12:
        break
season_list = [(12, 1, 2, 'зима'), (3, 4, 5, 'весна'), (6, 7, 8, 'лето'), (9, 10, 11, 'осень')]
for season in season_list:
    if month in season:
        print(season[3])
        break
# решение через словарь
season_dict = {(12, 1, 2):'зима', (3, 4, 5):'весна', (6, 7, 8):'лето', (9, 10, 11):'осень'}
for season in season_dict:
    if month in season:
        print(season_dict.get(season))
        break