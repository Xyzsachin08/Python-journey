class Student:
    def __init__(self, name):
        self.name = name   # self.name is attribute

    def show(self):
        print("Name:", self.name)

s1 = Student("Sachin")
s2 = Student("Rahul")

s1.show()
s2.show()