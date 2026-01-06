"""
utils.py - Простые вспомогательные функции для работы с фигурами.
"""

import math


def convert_units(value, from_unit, to_unit):
    """
    Конвертирует значение из одних единиц в другие.

    Простые коэффициенты конвертации:
    - Метрическая система: mm, cm, m
    - Имперская система: in, ft

    """
    factors = {
        # Метрическая система
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,

        # Имперская система (примерные значения)
        'in': 0.0254,  # 1 дюйм = 0.0254 метра
        'ft': 0.3048,  # 1 фут = 0.3048 метра
    }

    if from_unit not in factors or to_unit not in factors:
        raise ValueError(f"Единицы {from_unit} или {to_unit} не поддерживаются")

    if from_unit == to_unit:
        return value, to_unit

    value_in_meters = value * factors[from_unit]
    converted_value = value_in_meters / factors[to_unit]

    return converted_value, to_unit


def compare_by_area(shape1, shape2):
    """
    Сравнивает две фигуры по площади поверхности.

    Возвращает строку с результатом сравнения.
    """
    area1 = shape1.surface_area()
    area2 = shape2.surface_area()

    if area1 > area2:
        return f"Первая фигура больше: {area1:.1f} vs {area2:.1f}"
    elif area2 > area1:
        return f"Вторая фигура больше: {area2:.1f} vs {area1:.1f}"
    else:
        return f"Фигуры равны по площади: {area1:.1f}"


def format_number(value, is_volume=False):
    """
    Форматирует число для красивого вывода.

    Если число очень большое, показывает в более удобных единицах.
    """
    if is_volume:
        suffix = "³"
    else:
        suffix = "²"

    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M{suffix}"
    elif value >= 1_000:
        return f"{value / 1_000:.2f}K{suffix}"
    else:
        return f"{value:.2f}{suffix}"


def show_shape_info(shape):
    """
    Показывает основную информацию о фигуре.
    """
    print(f"\n{shape.__class__.__name__}:")
    print(f"  Размер: {getattr(shape, 'side', getattr(shape, 'radius', '?'))} {shape.unit}")
    print(f"  Площадь: {shape.surface_area():.2f} {shape.unit}²")
    print(f"  Объём: {shape.volume():.2f} {shape.unit}³")


def get_volume_ratio(shape1, shape2):
    """
    Возвращает отношение объёмов двух фигур.

    """
    v1 = shape1.volume()
    v2 = shape2.volume()

    if v2 == 0:
        return float('inf')

    return v1 / v2


def scale_shape(shape, factor):
    """
    Создаёт новую фигуру, увеличенную/уменьшенную в factor раз.

    Работает только для Cube и Sphere.
    """
    from copy import copy

    new_shape = copy(shape)

    if hasattr(new_shape, 'side'):
        new_shape.side *= factor
    elif hasattr(new_shape, 'radius'):
        new_shape.radius *= factor

    return new_shape
