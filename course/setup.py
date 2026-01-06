from setuptools import setup, find_packages

setup(
    name='geometric',
    version='0.1.0',
    packages=find_packages("."),
    scripts=[""],  # Расположение главного исполняемого файла.
    url='https://github.com/aleksandra-protasova/protasova_av',  # Адрес репозитория с вашей курсовой работой.
    license='',
    author='Протасова Александра Протасова',
    author_email='aleksandraprotasova4@gmail.com',
    description='Пакет на Python для работы с геометрическими фигурами, включающий классы Shape, Rectangle, Circle, Cube, Sphere и вспомогательные функции.',
    include_package_data=True,
    install_requires=[],

)