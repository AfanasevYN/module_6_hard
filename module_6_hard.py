import math

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        if not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count()
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != len(self.__sides):
            return False
        return all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1  # Круг имеет одну сторону (длину окружности)

    def __init__(self, color, circle_l):
        super().__init__(color)
        self.set_sides(circle_l)  # Устанавливаем длину окружности

    # Реализация метода __len__
    def __len__(self):
        return self.get_circle_l()  # Длина окружности

    def get_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.get_radius() ** 2)

    def get_circle_l(self):
        return self.get_sides()[0]

    def set_sides(self, circle_l):
        self.__sides = [circle_l]

    def get_sides(self):
        return self.__sides

class Triangle(Figure):
    sides_count = 3
    def __init__(self, side1, side2, side3, color=(0, 0, 0)):
        super().__init__(color)
        self.set_sides(side1, side2, side3)

    def get_square(self):
        # Используем формулу Герона
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def set_sides(self, side1, side2, side3):
        self.__sides = [side1, side2, side3]

    def get_sides(self):
        return self.__sides


class Cube(Figure):
    sides_count = 12  # Куб имеет 12 одинаковых сторон

    def __init__(self, color, side_length):
        super().__init__(color)
        self.set_sides(*([side_length] * Cube.sides_count))  # Устанавливаем 12 одинаковых сторон

    def get_volume(self):
        side_length = self.get_sides()[0]  # Все стороны одинаковые
        return side_length ** 3

    # Переопределяем метод для установки сторон
    def set_sides(self, *new_sides):
        if len(new_sides) == Cube.sides_count:
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())