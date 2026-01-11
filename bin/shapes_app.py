"""Главный исполняемый файл приложения"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tabulate import tabulate
from shapes import (
    Rectangle, Circle, Cube, Sphere,
    convert_units, compare_shapes_by_area
)


def display_shape_info(shape):
    """
    Отображает информацию о фигуре.

    :param shape: Геометрическая фигура
    :return: Строка с информацией о фигуре
    """
    info = f"Фигура: {shape.__class__.__name__}\n"

    if hasattr(shape, 'get_width'):
        info += f"  Ширина: {shape.get_width()}{shape.get_unit()}\n"
    if hasattr(shape, 'get_height'):
        info += f"  Высота: {shape.get_height()}{shape.get_unit()}\n"
    if hasattr(shape, 'get_radius'):
        info += f"  Радиус: {shape.get_radius()}{shape.get_unit()}\n"
    if hasattr(shape, 'get_side'):
        info += f"  Сторона: {shape.get_side()}{shape.get_unit()}\n"

    if hasattr(shape, 'area'):
        info += f"  Площадь: {shape.area():.2f}{shape.get_unit()}²\n"
    if hasattr(shape, 'perimeter'):
        info += f"  Периметр: {shape.perimeter():.2f}{shape.get_unit()}\n"
    if hasattr(shape, 'surface_area'):
        info += f"  Площадь поверхности: {shape.surface_area():.2f}{shape.get_unit()}²\n"
    if hasattr(shape, 'volume'):
        info += f"  Объем: {shape.volume():.2f}{shape.get_unit()}³\n"

    return info


def main():
    """Основная функция приложения"""

    print("Геометрические фигуры")

    print("\n1. Создание фигур:")

    # 2D фигуры
    rect = Rectangle(10, 5, 'cm')
    circle = Circle(7, 'cm')

    print(f"Создан: {rect}")
    print(f"Создан: {circle}")

    # 3D фигуры
    cube = Cube(5, 'cm')
    sphere = Sphere(4, 'cm')

    print(f"Создан: {cube}")
    print(f"Создан: {sphere}")

    # Расчет площади/объема
    print("\n2. Расчёты:")

    calculations = [
        ["Прямоугольник", f"{rect.area():.2f} см²", f"{rect.perimeter():.2f} см", "-"],
        ["Круг", f"{circle.area():.2f} см²", f"{circle.perimeter():.2f} см", "-"],
        ["Куб", f"{cube.surface_area():.2f} см²", "-", f"{cube.volume():.2f} см³"],
        ["Сфера", f"{sphere.surface_area():.2f} см²", "-", f"{sphere.volume():.2f} см³"],
    ]

    print(tabulate(calculations,
                   headers=["Фигура", "Площадь", "Периметр/Окружность", "Объем"],
                   tablefmt="grid"))

    print("\n3. Сравнение фигур по площади:")

    print(f"Сравнение прямоугольника и круга: {compare_shapes_by_area(rect, circle)}")
    print(f"Сравнение куба и сферы (по площади поверхности): {compare_shapes_by_area(cube, sphere)}")

    print("\n4. Конвертация единиц измерения:")

    print(f"Куб до конвертации: {cube}")

    side_in_m = convert_units(cube.get_side(), 'cm', 'm')
    cube_in_m = Cube(side_in_m, 'm')
    print(f"Куб после конвертации в метры: {cube_in_m}")

    cube.set_side(5)
    cube.set_unit('cm')

    print("\n5. Характеристики всех фигур:")

    shapes = [rect, circle, cube, sphere]
    for shape in shapes:
        print(display_shape_info(shape))

    print("Программа завершена")

if __name__ == "__main__":
    main()