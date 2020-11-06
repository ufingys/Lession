"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed} км/ч")


class TownCar(Car):

    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f" Текущая скорость автомобиля {self.speed} км/ч, превышение скорости на {self.speed - 60} км/ч"
        else:
            return "скорость не превышена"


class WorkCar(Car):

    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Текущая скорость автомобиля {self.speed} км/ч, превышение скорости на {self.speed - 40} км/ч"
        else:
            return "скорость не превышена"


class SportCar(Car):

    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 90:
            return f"Текущая скорость автомобиля {self.speed} км/ч, превышение скорости на {self.speed - 90} км/ч"
        else:
            return "скорость не превышена"


class PoliceCar(Car):

    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 50:
            return f"Текущая скорость автомобиля {self.speed} км/ч, превышение скорости на {self.speed - 50} км/ч"
        else:
            return "скорость не превышена"


town_car = TownCar("BMV", 90, "Black", False)
work_car = WorkCar("VW", 70, "Green", False)
sport_car = SportCar("Lamborgini", 170, "Red", False)
police_car = SportCar("Ford", 70, "White", True)
print(f"Town Car: name - {town_car.name}, color - {town_car.color}, speed - {town_car.speed}, is police - {town_car.is_police}, {town_car.show_speed()}")
print(f"Work Car: name - {work_car.name}, color - {work_car.color}, speed - {work_car.speed}, is police - {work_car.is_police}, {work_car.show_speed()}")
print(f"Sport Car: name - {sport_car.name}, color - {sport_car.color}, speed - {sport_car.speed}, is police - {sport_car.is_police}, {sport_car.show_speed()} ")
print(f"Police Car: name - {police_car.name}, color - {police_car.color}, speed - {police_car.speed}, is police - {police_car.is_police}, {police_car.show_speed()}")