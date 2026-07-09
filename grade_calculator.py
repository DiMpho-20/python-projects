import json

FILENAME = 'students.json'

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


def main():
    calc = GradeCalculator()

    while True:
        print('\n--- Student Grade Calculator ---')
        print('1. Add student')
        print('2. View all students')
        print('3. Search student')
        print('4. Delete student')
        print('5. Exit')

        choice = input('Choose an option: ')

        if choice == '1':
            name = input('Name: ')
            student_number = input('Student number: ')
            module = input('Module: ')
            mark = int(input('Mark: '))
            calc.add_student(name, student_number, module, mark)
        elif choice == '2':
            calc.view_all()
        elif choice == '3':
            student_number = input('Enter student number: ')
            student = calc.search_student(student_number)
            if student:
                print(student)
            else:
                print('Student not found.')
        elif choice == '4':
            student_number = input('Enter student number to delete: ')
            calc.delete_student(student_number)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid option, try again.')

main()