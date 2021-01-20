class Student:
    def __init__(self, name, age, is_on_probation):
        self.name = name
        self.age = age
        self.is_on_probation = is_on_probation
    def print(self):
        print(self.name + " " + str(self.age))

s = Student("simon", 26, False)

s.print()