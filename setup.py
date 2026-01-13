from setuptools import setup, find_packages

setup(
    name='geometric_shapes',
    version='0.0.1',
    packages=find_packages("."),
    scripts=["bin/shapes_app.py"],
    url='https://github.com/aleksandra-protasova/protasova_av',
    license='Apache-2.0',
    author='Протасова Александра Владимировна',
    author_email='aleksandraprotasova4@gmail.com',
    description='Пакет на Python для работы с 2D и 3D геометрическими фигурами',
    include_package_data=True,
    install_requires=[
        'tabulate>=0.8.9',
    ],

)
