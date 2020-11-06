"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки", end=" ")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(self.title)


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(self.title)


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(self.title)


pen = Pen("Ручкой")
pencil = Pencil("Карандашом")
handle = Handle("Маркером")
pen.draw()
pencil.draw()
handle.draw()