from sys import argv


def salary(hours, rate, bonus):
    try:
        return int(hours) * float(rate) + float(bonus)
    except ValueError:
        print("Wrong format numbers")


name_script, hours_done, rate, bonus = argv
print(salary(hours_done, rate, bonus))