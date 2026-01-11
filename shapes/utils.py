"""
Вспомогательные функции для работы с геометрическими фигурами.
"""

from typing import Union, List
from shapes.shapes2d import Shape
from shapes.shapes3d import ThreeDShape


def convert_units(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует значение из одних единиц измерения в другие.

    Поддерживаемые единицы: mm, cm, dm, m, km

    :param value: Значение для конвертации
    :param from_unit: Исходная единица измерения
    :param to_unit: Целевая единица измерения
    :return: Конвертированное значение
    :raises ValueError: Если указана неизвестная единица измерения
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Значение должно быть числом.")
    if not all(isinstance(unit, str) for unit in [from_unit, to_unit]):
        raise TypeError("Единицы измерения должны быть строками.")

    conversion_factors = {
        'mm': 0.001,  # миллиметры в метры
        'cm': 0.01,  # сантиметры в метры
        'dm': 0.1,  # дециметры в метры
        'm': 1.0,  # метры
        'km': 1000.0,  # километры в метры
    }

    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    if from_unit_lower not in conversion_factors:
        raise ValueError(f"Неизвестная исходная единица измерения: {from_unit}")
    if to_unit_lower not in conversion_factors:
        raise ValueError(f"Неизвестная целевая единица измерения: {to_unit}")

    # Конвертируем в метры, затем в целевую единицу
    value_in_meters = value * conversion_factors[from_unit_lower]
    converted_value = value_in_meters / conversion_factors[to_unit_lower]

    return converted_value


def compare_shapes_by_area(shape1: Union[Shape, ThreeDShape],
                           shape2: Union[Shape, ThreeDShape]) -> str:
    """
    Сравнивает две фигуры по площади/площади поверхности.

    :param shape1: Первая фигура для сравнения
    :param shape2: Вторая фигура для сравнения
    :return: Строка с результатом сравнения
    :raises TypeError: Если переданы объекты неверного типа
    """
    if not (isinstance(shape1, (Shape, ThreeDShape)) and
            isinstance(shape2, (Shape, ThreeDShape))):
        raise TypeError("Оба аргумента должны быть геометрическими фигурами.")

    # Получаем площади/площади поверхностей
    if isinstance(shape1, Shape):
        area1 = shape1.area()
    else:
        area1 = shape1.surface_area()

    if isinstance(shape2, Shape):
        area2 = shape2.area()
    else:
        area2 = shape2.surface_area()

    # Сравниваем с заданной точностью
    if abs(area1 - area2) < 1e-10:
        return f"Фигуры имеют одинаковую площадь ({area1:.2f})"
    elif area1 > area2:
        diff = area1 - area2
        return (f"{shape1.__class__.__name__} больше {shape2.__class__.__name__} "
                f"на {diff:.2f} единиц²")
    else:
        diff = area2 - area1
        return (f"{shape1.__class__.__name__} меньше {shape2.__class__.__name__} "
                f"на {diff:.2f} единиц²")

def create_shapes_demo() -> List[Union[Shape, ThreeDShape]]:
    """
    Создает демонстрационный набор фигур.

    :return: Список созданных фигур
    """
    from shapes.shapes2d import Rectangle, Circle
    from shapes.shapes3d import Cube, Sphere

    shapes = [
        Rectangle(10.0, 5.0, 'cm'),
        Rectangle(3.0, 7.0, 'm'),
        Circle(4.0, 'cm'),
        Circle(2.5, 'm'),
        Cube(5.0, 'cm'),
        Cube(2.0, 'm'),
        Sphere(3.0, 'cm'),
        Sphere(1.5, 'm'),
    ]

    return shapes

if __name__ == '__main__':
    ...