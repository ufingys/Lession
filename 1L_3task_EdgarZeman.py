n = int(input("Введите число "))
total = n
d = 1
while total >= 1:
    d *= 10
    total //= d
total = n + (n * d + n) + (n * d * d + n * d + n);
print("Сумма типа: n+nn+nnn = %d" % (total))