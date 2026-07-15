import json
from config import FILENAME
from student import Student

class GradeCalculator:
    def __init__(self):
        self.students = []
        self.load()

    def add_student(self, name, student_number, module, mark):
        student = Student(name, student_number, module, mark)
        self.students.append(student)
        self.save()
        print(f'Student {name} added.')

    def view_all(self):
        if not self.students:
            print('No students found.')
            return
        for student in self.students:
            print(student)

    def search_student(self, student_number):
        for student in self.students:
            if student.student_number == student_number:
                return student
        return None

    def delete_student(self, student_number):
        self.students = [s for s in self.students if s.student_number != student_number]
        self.save()
        print(f'Student {student_number} deleted.')

    def save(self):
        data = [{'name': s.name, 'student_number': s.student_number, 'module': s.module, 'mark': s.mark, 'grade': s.grade} for s in self.students]
        with open(FILENAME, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self):
        try:
            with open(FILENAME) as f:
                data = json.load(f)
            self.students = [Student(d['name'], d['student_number'], d['module'], d['mark']) for d in data]
        except FileNotFoundError:
            self.students = []

