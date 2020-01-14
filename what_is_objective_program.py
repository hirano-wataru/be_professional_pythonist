# python3 /Users/lawrie_6strings/be_professional_pythonist/what_is_objective_program.py
# -*- coding: utf-8 -*-

# 1.
class Shape:
    def what_am_i(self):
        print("I am a Shape")


class Rectangle(Shape):
    def __init__(self, height, bottom):
        self.height = height
        self.bottom = bottom

    def caliculate_perimeter(self):
        return (self.height * self.bottom) * 2


class Square(Shape):
    def __init__(self, height):
        self.height = height

    def caliculate_perimeter(self):
        return self.height * 4

    def chenge_size(self, h):
        self.height = h


print(Rectangle(2, 4).caliculate_perimeter())
print(Square(4).caliculate_perimeter())

# 2.
square = Square(4)
print(square.caliculate_perimeter())
square.chenge_size(2)
print(square.caliculate_perimeter())

# 3.
Rectangle(2, 3).what_am_i()
Square(3).what_am_i()


# 4.
class Horse:
    def __init__(self, rider, name):
        self.rider = rider
        self.name = name

    def call_name(self):
        print(self.rider.name) #=> メソッドの変数が引き継がれているこれが左近ポジション。
        print(self.name)



class Rider:
    def __init__(self, name):
        self.name = name


rider = Rider("wataru")
horse = Horse(rider,"akibao-")
horse.call_name()
