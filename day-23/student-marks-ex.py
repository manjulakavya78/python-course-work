class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        avg = sum(self.marks) / len(self.marks)
        if avg>=40:
            print("Passed")
        else:
            print("Fail")

s1 = Student("kavya", [45, 56, 60])
s1.is_passed()
