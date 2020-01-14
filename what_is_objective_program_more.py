# python3 /Users/lawrie_6strings/be_professional_pythonist/what_is_objective_program_more.py
# -*- coding: utf-8 -*-

# 1.
class Square:
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(s1)

    def __repr__(self):
        return "{} by {} by {} by {} by ".format(self.s1,self.s1,self.s1,self.s1)

    def true_or_false(self,a, b):
        return a is b



print(Square(4))
print(Square(5))
print(Square(6))

print(Square.square_list)


# 2.
print(Square(4))

# 3.
print(Square(4).true_or_false(1,"1"))