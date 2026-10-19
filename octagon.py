import math # библиотека для π и √
import matplotlib.pyplot as plt # для рисунка
from matplotlib.patches import RegularPolygon, Circle # готовые фигуры многоугольника и круга

class Octagon: # класс «Октагон»
    def __init__(self, side_length): # конструктор, который принимает сторону
        self.side_length = side_length  # сторона октагона
        self.internal_angle = 135 # внутренний угол, она же константа
        self.k_constant = 1 + math.sqrt(2) # k = 1 + √2, тоже

    def opisanaya_circle(self): # описанная окружность
        radius = self.side_length * self.k_constant / 2 # R = a·k/2
        print(f"радиус описанной: {radius}") # выводим радиус
        print(f"площадь описанной: {math.pi * radius ** 2}\n") # S = πR²

    def vpisanaya_circle(self): # вписанная окружность
        radius = self.side_length / 2 # r = a/2
        print(f"радиус вписанной: {radius}") # выводим радиус
        print(f"площадь вписанной: {math.pi * radius ** 2}\n") # S = πr²

    def octagon_plochad_perimeter(self): # площадь и периметр октагона
        print(f"периметр октагона: {8 * self.side_length}") # P = 8a
        print(f"площадь октагона: {2 * self.side_length ** 2 * self.k_constant}\n") # S = 2a²k

    def draw(self): # рисунок всех фигур
        R = self.side_length * self.k_constant / 2 # радиус описанной окружности
        r = self.side_length / 2 # радиус вписанной окружности

        fig, ax = plt.subplots(figsize=(6, 6)) # окно графика 6×6
        ax.set_aspect("equal") # равный масштаб осей

        ax.add_patch(RegularPolygon((0, 0), numVertices=8, radius=R, # правильный 8-угольник
        orientation=math.pi / 8, # поворот на 22.5°
        fill=False, edgecolor="black", # чёрный контур
        label="октагон"))

        ax.add_patch(Circle((0, 0), R, fill=False, color="pink", label="описанная")) # описанная окружность
        ax.add_patch(Circle((0, 0), r, fill=False, color="purple", label="вписанная")) # вписанная окружность

        ax.set_xlim(-R * 1.2, R * 1.2) # границы по X
        ax.set_ylim(-R * 1.2, R * 1.2) # границы по Y
        ax.legend() 
        plt.show() # вывод графика