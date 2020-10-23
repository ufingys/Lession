n = int(input("Введите целое положительное число: "))
max_n = n % 10
while n > 0:
    if max_n < n % 10:
        max_n = n % 10
    n = n // 10
print("Самая большая цифра в числе: %d" % max_n)