time_in_sec = int(input("Введите время в секундах: "));
sec = time_in_sec % 60
minutes = (time_in_sec // 60) % 60
hours = (time_in_sec // 60) // 60
print("Время %02d:%02d:%02d" % (hours, minutes, sec))