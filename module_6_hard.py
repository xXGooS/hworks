class Figure:
    sides_count = 0
    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = sides
        self.__color = color
        self.filded = False

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        return all(0 <= colors <=255 for colors in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        if (isinstance(side, int) and side >= 0 for side in new_sides) and len(new_sides) == self.sides_count:
            return True
        else:
            return False
    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color=(0, 0, 0), *sides):
        from math import pi
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi) #R=P/(2π)

    def get_square(self):
        from math import pi
        return pi * self.__radius ** 2 #S=πR^2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a+b+c) / 2
        return (p * (p-a) * (p-b) * (p-c)) ** 0.5

class Cube(Figure):
    sides_count = 12
    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) != 1:
            sides = [0]
        super().__init__(color, *sides * self.sides_count)

    def get_volume(self):
        return self.get_sides()[0] ** 3

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