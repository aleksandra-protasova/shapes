"""Главный исполняемый файл приложения"""

from shapes.shapes2d import Rectangle, Circle
from shapes.shapes3d import Cube, Sphere
from shapes.utils import convert_units, compare_shapes_by_area

if __name__ == "__main__":

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

    print("\n3. Сравнение фигур по площади:")

    print(f"Сравнение прямоугольника и круга: {compare_shapes_by_area(rect, circle)}")
    print(f"Сравнение куба и сферы (по площади поверхности): {compare_shapes_by_area(cube, sphere)}")

    print("\n4. Конвертация единиц измерения:")

    print(f"Куб до конвертации: {cube}")
    cube.convert_units('m')
    print(f"Куб после конвертации в метры: {cube}")

    cube.convert_units('cm')

    print("\n5. Характеристики всех фигур:")

    print("Программа завершена")
