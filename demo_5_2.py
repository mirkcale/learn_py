#!/usr/bin/env python3
from Animal import Animal 
class Student (Animal) :
    def __init__ (self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    pass

mike = Student('mike', 60)
print (mike.name)
print (Student, mike.run())