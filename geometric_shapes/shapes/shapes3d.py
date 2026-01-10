"""
Модуль для представления 3D геометрических фигур.
"""

from math import pi
from typing import Union


class ThreeDShape:
    """
    Базовый класс для всех 3D геометрических фигур.
    """

    def __init__(self, unit: str = 'cm'):
        """
        Базовый конструктор класса ThreeDShape.

        :param unit: Единица измерения
        """
        if not isinstance(unit, str):
            raise TypeError("Единица измерения должна быть строкой.")

        self.__unit = unit

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

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта ThreeDShape.

        :return: Строковое представление
        """
        return f"{self.__class__.__name__}(unit={self.__unit})"


class Cube(ThreeDShape):
    """
    Класс для представления куба.
    """

    def __init__(self, side: float, unit: str = 'cm'):
        """
        Конструктор класса Cube.

        :param side: Длина стороны куба
        :param unit: Единица измерения
        """
        super().__init__(unit)

        if not isinstance(side, (int, float)):
            raise TypeError("Длина стороны должна быть числом.")
        if side <= 0:
            raise ValueError("Длина стороны должна быть положительным числом.")

        self.__side = side

    def volume(self) -> float:
        """
        Вычисляет объем куба.

        Формула: сторона³

        :return: Объем куба
        """
        return self.__side ** 3

    def surface_area(self) -> float:
        """
        Вычисляет площадь поверхности куба.

        Формула: 6 * сторона²

        :return: Площадь поверхности куба
        """
        return 6 * self.__side ** 2

    def get_side(self) -> float:
        """
        Возвращает длину стороны куба.

        :return: Длина стороны куба
        """
        return self.__side

    def set_side(self, side: float):
        """
        Устанавливает новое значение длины стороны.

        :param side: Новая длина стороны куба
        """
        if not isinstance(side, (int, float)):
            raise TypeError("Длина стороны должна быть числом.")
        if side <= 0:
            raise ValueError("Длина стороны должна быть положительным числом.")
        self.__side = side

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Cube.

        :return: Строковое представление куба
        """
        return (f"Cube(side={self.__side}{self.get_unit()}, "
                f"volume={self.volume():.2f}{self.get_unit()}³, "
                f"surface_area={self.surface_area():.2f}{self.get_unit()}²)")


class Sphere(ThreeDShape):
    """
    Класс для представления сферы.
    """

    def __init__(self, radius: float, unit: str = 'cm'):
        """
        Конструктор класса Sphere.

        :param radius: Радиус сферы
        :param unit: Единица измерения
        """
        super().__init__(unit)

        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть числом.")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")

        self.__radius = radius

    def volume(self) -> float:
        """
        Вычисляет объем сферы.

        Формула: (4/3) * π * радиус³

        :return: Объем сферы
        """
        return (4 / 3) * pi * self.__radius ** 3

    def surface_area(self) -> float:
        """
        Вычисляет площадь поверхности сферы.

        Формула: 4 * π * радиус²

        :return: Площадь поверхности сферы
        """
        return 4 * pi * self.__radius ** 2

    def get_radius(self) -> float:
        """
        Возвращает радиус сферы.

        :return: Радиус сферы
        """
        return self.__radius

    def set_radius(self, radius: float):
        """
        Устанавливает новое значение радиуса.

        :param radius: Новый радиус сферы
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть числом.")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.__radius = radius

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Sphere.

        :return: Строковое представление сферы
        """
        return (f"Sphere(radius={self.__radius}{self.get_unit()}, "
                f"volume={self.volume():.2f}{self.get_unit()}³, "
                f"surface_area={self.surface_area():.2f}{self.get_unit()}²)")

if __name__ == '__main__':
    ...