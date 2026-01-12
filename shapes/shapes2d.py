"""
Модуль для представления 2D геометрических фигур.
"""

from abc import ABC, abstractmethod
from math import pi
from typing import Union

class Shape(ABC):
    """
    Абстрактный базовый класс для всех геометрических фигур.
    """

    def __init__(self, unit: str = 'cm'):
        """
        Базовый конструктор класса Shape.

        :param unit: Единица измерения
        """
        if not isinstance(unit, str):
            raise TypeError("Единица измерения должна быть строкой.")

        self.__unit = unit

    @abstractmethod
    def area(self) -> float:
        """
        Вычисляет площадь фигуры.

        :return: Площадь фигуры
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Вычисляет периметр фигуры.

        :return: Периметр
        """
        pass

    def get_unit(self) -> str:
        """
        Возвращает единицу измерения фигуры.

        :return: Единица измерения
        """
        return self.__unit

    def set_unit(self, unit: str):
        """
        Устанавливает новое значение единицы измерения.

        :param unit: Новая единица измерения
        """
        if not isinstance(unit, str):
            raise TypeError("Единица измерения должна быть строкой.")
        self.__unit = unit

    def __eq__(self, other: 'Shape') -> bool:
        """
        Сравнение фигур по площади.

        :param other: Другая фигура для сравнения
        :return: True если площади равны, иначе False
        """
        if not isinstance(other, Shape):
            return NotImplemented
        return abs(self.area() - other.area()) < 1e-10

    def __lt__(self, other: 'Shape') -> bool:
        """
        Сравнение фигур по площади (меньше).

        :param other: Другая фигура для сравнения
        :return: True если площадь текущей фигуры меньше, иначе False
        """
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() < other.area()

    def __gt__(self, other: 'Shape') -> bool:
        """
        Сравнение фигур по площади (больше).

        :param other: Другая фигура для сравнения
        :return: True если площадь текущей фигуры больше, иначе False
        """
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() > other.area()

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Shape.

        :return: Строковое представление
        """
        return f"{self.__class__.__name__}(unit={self.__unit})"


class Rectangle(Shape):
    """
    Класс для представления прямоугольника.
    """

    def __init__(self, width: float, height: float, unit: str = 'cm'):
        """
        Конструктор класса Rectangle.

        :param width: Ширина прямоугольника
        :param height: Высота прямоугольника
        :param unit: Единица измерения
        """
        super().__init__(unit)

        if not all(isinstance(arg, (int, float)) for arg in [width, height]):
            raise TypeError("Ширина и высота должны быть числами.")
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами.")

        self.__width = width
        self.__height = height

    def area(self) -> float:
        """
        Вычисляет площадь прямоугольника.

        Формула: ширина * высота

        :return: Площадь прямоугольника
        """
        return self.__width * self.__height

    def perimeter(self) -> float:
        """
        Вычисляет периметр прямоугольника.

        Формула: 2 * (ширина + высота)

        :return: Периметр прямоугольника
        """
        return 2 * (self.__width + self.__height)

    def get_width(self) -> float:
        """
        Возвращает ширину прямоугольника.

        :return: Ширина прямоугольника
        """
        return self.__width

    def get_height(self) -> float:
        """
        Возвращает высоту прямоугольника.

        :return: Высота прямоугольника
        """
        return self.__height

    def set_width(self, width: float):
        """
        Устанавливает новое значение ширины.

        :param width: Новая ширина прямоугольника
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть числом.")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом.")
        self.__width = width

    def set_height(self, height: float):
        """
        Устанавливает новое значение высоты.

        :param height: Новая высота прямоугольника
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть числом.")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        self.__height = height

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Rectangle.

        :return: Строковое представление прямоугольника
        """
        return (f"Rectangle(width={self.__width}{self.get_unit()}, "
                f"height={self.__height}{self.get_unit()}, "
                f"area={self.area():.2f}{self.get_unit()}², "
                f"perimeter={self.perimeter():.2f}{self.get_unit()})")


class Circle(Shape):
    """
    Класс для представления круга.
    """

    def __init__(self, radius: float, unit: str = 'cm'):
        """
        Конструктор класса Circle.

        :param radius: Радиус круга
        :param unit: Единица измерения
        """
        super().__init__(unit)

        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть числом.")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")

        self.__radius = radius

    def area(self) -> float:
        """
        Вычисляет площадь круга.

        Формула: π * радиус²

        :return: Площадь круга
        """
        return pi * self.__radius ** 2

    def perimeter(self) -> float:
        """
        Вычисляет длину окружности.

        Формула: 2 * π * радиус

        :return: Длина окружности
        """
        return 2 * pi * self.__radius

    def get_radius(self) -> float:
        """
        Возвращает радиус круга.

        :return: Радиус круга
        """
        return self.__radius

    def set_radius(self, radius: float):
        """
        Устанавливает новое значение радиуса.

        :param radius: Новый радиус круга
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть числом.")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.__radius = radius

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Circle.

        :return: Строковое представление круга
        """
        return (f"Circle(radius={self.__radius}{self.get_unit()}, "
                f"area={self.area():.2f}{self.get_unit()}², "
                f"circumference={self.perimeter():.2f}{self.get_unit()})")

if __name__ == '__main__':
    ...