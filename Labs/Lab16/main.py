"""
Дано:  фигура - прямоугольник ,  d1,d2-диагональ, alfa-угол между диагоналями
Задание:
1. Создать класс
2. Создать методы, выводящие площадь, периметр
3. Создать метод перемещения по плоскости
4. Создать метод, который говорит можно ли из данного объекта сделать 3d-объект путем многократного дублирования самого объекта
5*. Создать класс-наследник, если возможен пункт 4 и повторить для него пункты 2 и 3
"""
import os
import datetime
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from math import sin, pow
from colorama import*
# from abc import ABC, abstractmethod
from time import sleep


date = datetime.datetime.now()


def cls():
    os.system('cls')


def my_shiny_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Yes, I'm decorator")
        function_to_decorate()
        print("I'm decorator after func")

    return the_wrapper_around_the_original_function


print(Fore.CYAN + "Date and time: " + Fore.WHITE + ("{:%d/%m/%Y %H:%M}".format(date)) + Fore.WHITE)


class rectangle:
    # d = diagonal, alpha = alpha (angle between diagonals)
    def __init__(self, d, alpha):
        self.d = d
        self.alpha = alpha

    def display_coordinates(self):
        print(f'Diagonal: {self.d}')

    def display_area(self):
        s = 0, 5 * pow(self.d, 2) * sin(self.alpha)
        print(f'Area: {s}')

    def display_perimeter(self):
        p = (sin(self.alpha) * pow(self.d, 2)) * 1 / 2
        print(f'Perimeter: {p}')


first_rectangle = rectangle(12, 60)
first_rectangle.display_coordinates()
first_rectangle.display_perimeter()
first_rectangle.display_area()


def print_rectangle(value):
    match value:
        case "0":
            sleep(1)
            print("ERROR! \nPlease enter a valid value.")
        case "1":
            sleep(1)
            fig, ax = plt.subplots()
            ax.plot([1, first_rectangle.d], [1, first_rectangle.d])
            ax.add_patch(
                patches.Rectangle(
                    (1, 1),
                    first_rectangle.d,
                    first_rectangle.d,
                    edgecolor='black',
                    facecolor='pink',
                    fill=True
                ))

            plt.show()

            patches.Rectangle(
                (first_rectangle.d, first_rectangle.d),
                1,
                2,
                edgecolor='blue',
                facecolor='red',
                fill=True
            )
        case "2":
            sleep(1)
            b = int(input('Enter x1:'))
            a = int(input('Enter x2:'))
            symbol = input('Enter symbol:')
            print(symbol * a)
            for i in range(b - 2):
                print(symbol, ' ' * (a - 2), symbol, sep='')
            print(symbol * a)
        case "3":
            sleep(1)
            for i in range(first_rectangle.d):
                if i == 0 or i == first_rectangle.d - 1:
                    for j in range(20):
                        print('-', end='')
                else:
                    print('|', end='')
                    for j in range(1, 19):
                        print(' ', end='')
                    print('|', end='')
                print()


@my_shiny_new_decorator
def decorator_example():
    print("YES-SIR!")


decorator_example()
print_rectangle("1")