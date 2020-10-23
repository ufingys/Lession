"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
def user_data(name, family, birth, city, email, tel):
    return f"Имя пользователя: {name};  Фамилия пользователя: {family}; Дата рождения: {birth}; Город проживания: {city}; E-mail: {email}; Телефон: {tel} "

user_name = input("Введите имя: ")
user_family = input("Введите фамилию: ")
user_birth = input("Введите дату рождения: ")
user_city = input("Введите дату город: ")
user_email = input("Введите электронную почту: ")
user_tel = input("Введите номер телефона: ")
print(user_data(name=user_name, tel=user_tel, family=user_family, birth=user_birth, city=user_city, email=user_email))
