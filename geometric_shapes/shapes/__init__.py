"""
Пакет для работы с геометрическими фигурами.
"""

from .shapes2d import Shape, Rectangle, Circle
from .shapes3d import ThreeDShape, Cube, Sphere
from .utils import (
    convert_units,
    compare_shapes_by_area,
    create_shapes_demo,
)

__version__ = '1.0.0'
__author__ = 'Протасова Александра Владимировна'
__email__ = 'aleksandraprotasova4@gmail.com'

__all__ = [
    # Классы 2D фигур
    'Shape',
    'Rectangle',
    'Circle',

    # Классы 3D фигур
    'ThreeDShape',
    'Cube',
    'Sphere',

    # Вспомогательные функции
    'convert_units',
    'compare_shapes_by_area',
    'create_shapes_demo',

    # Данные
    '__version__',
    '__author__',
    '__email__',
]

if __name__ == '__main__':
    ...