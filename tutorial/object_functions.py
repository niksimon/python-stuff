class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

s1 = Student("simon", 26, 4.0)

print(s1.on_honor_roll())