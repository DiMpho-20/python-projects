class Student:
    def __init__(self, name, student_number, module, mark):
        self.name = name
        self.student_number = student_number
        self.module = module
        self.mark = mark
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark < 50:
            return "Fail"
        elif self.mark < 75:
            return "Pass"
        else:
            return "Distinction"

    def __str__(self):
        return f'Name: {self.name} | Student No: {self.student_number} | Module: {self.module} | Mark: {self.mark} | Grade: {self.grade}'