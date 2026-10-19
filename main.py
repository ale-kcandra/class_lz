from octagon import Octagon # импорт класса из octagon.py

side = float(input("Сторона: ")) # ввод стороны 
o = Octagon(side) # создание объекта класса

o.opisanaya_circle() # считать описанную окружность
o.vpisanaya_circle() # считать вписанную окружность
o.octagon_plochad_perimeter() # считать площадь и периметр
o.draw() # нарисовать все фигуры