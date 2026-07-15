from calculator import GradeCalculator

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

if __name__ == "__main__":
    main()