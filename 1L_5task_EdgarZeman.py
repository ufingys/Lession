proceeds = int(input("Введите значение выручки: "))
cost = int(input("Введите значение издержек: "))
loss = 0    #убыток
profit = proceeds - cost
if profit < 0:
    loss = profit * -1
    profit = 0
    print("Финансовый результат: убыток %d" % (profit, loss))
else:
    rentab = profit / proceeds
    quantity = int(input("Введите количество сотрудников: "))
    print("Финансовый результат: прибыль %d, убыток %d, рентабельность %f, прибыль на сотрудника %d" % (profit, loss, rentab, profit / quantity))