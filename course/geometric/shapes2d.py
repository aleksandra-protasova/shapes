"""
Модуль для работы с двумерными геометрическими фигурами.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Абстрактный базовый класс для геометрических фигур.
    """

    def __init__(self, name):
        """
        Text
        :param name: Имя чего-то
        """
        self.name = name

    @abstractmethod
    def area(self):
        """
        Вычисление площади фигуры.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Вычисление периметра фигуры.
        """
        pass

    def display_info(self):
        """
        Вернуть тототото
        :return: Текст информации.
        """
        return f"Фигура: {self.name}\nПлощадь: {self.area():.2f}\nПериметр: {self.perimeter():.2f}"

    def __str__(self):
        return f"{self.name} [Площадь: {self.area():.2f}]"

    def __eq__(self, other):
        """
        Сравнение фигур по площади.
        """
        if not isinstance(other, Shape):
            return NotImplemented
        return math.isclose(self.area(), other.area())

    def __lt__(self, other):
        """
        Сравнение фигур по площади (меньше).
        """
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() < other.area()

    def __gt__(self, other):
        """
        Сравнение фигур по площади (больше).
        """
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() > other.area()


class Rectangle(Shape):
    """
    Класс прямоугольника.
    """

    def __init__(self, width, height, name="Прямоугольник"):
        """
        Инициализация прямоугольника.

        Args:
            width (float): Ширина прямоугольника
            height (float): Высота прямоугольника
            name (str): Название прямоугольника
        """
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        """
        Вычисление площади прямоугольника.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Вычисление периметра прямоугольника.
        """
        return 2 * (self.width + self.height)

    def diagonal(self):
        """
        Вычисление диагонали прямоугольника.
        """
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def display_info(self):
        """
        Отображение информации о прямоугольнике.
        """
        info = super().display_info()
        info += f"\nШирина: {self.width:.2f}"
        info += f"\nВысота: {self.height:.2f}"
        info += f"\nДиагональ: {self.diagonal():.2f}"
        return info


class Circle(Shape):
    """
    Класс круга.
    """

    def __init__(self, radius, name="Круг"):
        """
        Инициализация круга.

        Args:
            radius (float): Радиус круга
            name (str): Название круга
        """
        super().__init__(name)
        self.radius = radius

    def area(self):
        """
        Вычисление площади круга.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Вычисление периметра (длины окружности) круга.
        """
        return 2 * math.pi * self.radius

    def diameter(self):
        """
        Вычисление диаметра круга.
        """
        return 2 * self.radius

    def display_info(self):
        """
        Отображение информации о круге.
        """
        info = super().display_info()
        info += f"\nРадиус: {self.radius:.2f}"
        info += f"\nДиаметр: {self.diameter():.2f}"
        return info
