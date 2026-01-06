"""
Модуль для работы с трёхмерными геометрическими фигурами.
"""

import math
from typing import Union, Type


class Cube:
    """
    Класс для работы с кубом.
    """

    def __init__(self, side: float, unit: str = "cm"):
        """
        Инициализация куба.

        Args:
            side: Длина стороны куба
            unit: Единица измерения (по умолчанию "cm")
        """
        if side <= 0:
            raise ValueError("Длина стороны должна быть положительной")
        self.side = side
        self.unit = unit

    def volume(self) -> float:
        """
        Вычисление объёма куба.
        """
        return self.side ** 3

    def surface_area(self) -> float:
        """
        Вычисление площади поверхности куба.
        """
        return 6 * (self.side ** 2)

    def __str__(self) -> str:
        """
        Строковое представление куба.
        """
        return (f"Куб:\n"
                f"  Сторона: {self.side} {self.unit}\n"
                f"  Объём: {self.volume():.2f} {self.unit}³\n"
                f"  Площадь поверхности: {self.surface_area():.2f} {self.unit}²")

    def convert_units(self, conversion_factor: float, new_unit: str) -> None:
        """
        Конвертация единиц измерения.

        Args:
            conversion_factor: Коэффициент конвертации
            new_unit: Новая единица измерения
        """
        self.side *= conversion_factor
        self.unit = new_unit

class Sphere:
    """
    Класс для работы со сферой.
    """

    def __init__(self, radius: float, unit: str = "cm"):
        """
        Инициализация сферы.

        Args:
            radius: Радиус сферы
            unit: Единица измерения (по умолчанию "cm")
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius
        self.unit = unit

    def volume(self) -> float:
        """
        Вычисление объёма сферы.
        """
        return (4 / 3) * math.pi * (self.radius ** 3)

    def surface_area(self) -> float:
        """
        Вычисление площади поверхности сферы.
        """
        return 4 * math.pi * (self.radius ** 2)

    def __str__(self) -> str:
        """
        Строковое представление сферы.
        """
        return (f"Сфера:\n"
                f"  Радиус: {self.radius} {self.unit}\n"
                f"  Диаметр: {2 * self.radius:.2f} {self.unit}\n"
                f"  Объём: {self.volume():.2f} {self.unit}³\n"
                f"  Площадь поверхности: {self.surface_area():.2f} {self.unit}²")

    def convert_units(self, conversion_factor: float, new_unit: str) -> None:
        """
        Конвертация единиц измерения.

        Args:
            conversion_factor: Коэффициент конвертации
            new_unit: Новая единица измерения
        """
        self.radius *= conversion_factor
        self.unit = new_unit


def compare_surface_areas(shape1: Union[Cube, Sphere], shape2: Union[Cube, Sphere]) -> str:
    """
    Сравнение фигур по площади поверхности.

    Args:
        shape1: Первая фигура
        shape2: Вторая фигура

    Returns:
        Строка с результатом сравнения
    """
    area1 = shape1.surface_area()
    area2 = shape2.surface_area()

    if area1 > area2:
        return f"{type(shape1).__name__} имеет бóльшую площадь поверхности ({area1:.2f} vs {area2:.2f} {shape1.unit}²)"
    elif area2 > area1:
        return f"{type(shape2).__name__} имеет бóльшую площадь поверхности ({area2:.2f} vs {area1:.2f} {shape1.unit}²)"
    else:
        return f"Фигуры имеют одинаковую площадь поверхности ({area1:.2f} {shape1.unit}²)"

