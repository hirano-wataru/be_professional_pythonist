# python3 /Users/lawrie_6strings/be_professional_pythonist/programing_paradime.py
# -*- coding: utf-8 -*-

# 1.
class Apple:
    def __init__(self, c, s, f, t):
        self.color = c
        self.size = s
        self.flaver = f
        self.t = t


# 2.
class Circle:
    def area(r):
        import math
        return r * r * math.pi


print(Circle.area(2))


# 3.
class Triangle:
    def area(height, bottom):
        return height * bottom / 2


print(Triangle.area(2, 4))


# 4.
class Hexagon:
    def calculate_perimeter(r):
        return r * 6


print(Hexagon.calculate_perimeter(2))
