a = float(input("Введите сколько км спортсмен пробежал в 1-й день: "))
b = int(input("Введите сколько спортсмен должен пробежть всего км: "))
counter = 1
while a < b:
    print("%d-й день: %.2f" % (counter, a))
    a *= 1.1
    counter += 1
print("%d-й день: %.2f" % (counter, a))
