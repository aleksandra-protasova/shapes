"""Главный исполняемый файл приложения"""

import sys
from tabulate import tabulate
from shapes import (
    Rectangle, Circle, Cube, Sphere,
    convert_units, compare_shapes_by_area, display_shape_info
)


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
    cube.convert_units('m')
    print(f"Куб после конвертации в метры: {cube}")

    cube.convert_units('cm')

    print("\n5. Характеристики всех фигур:")

    shapes = [rect, circle, cube, sphere]
    for shape in shapes:
        print(display_shape_info(shape))

    print("Программа завершена")

if __name__ == "__main__":
    main()