def menu():
    menu_message = {1: 'show student info', 2: 'add student info', 3: 'delete student info', 4: 'exit system'}
    print('{0}{1}{0}'.format('=' * 10, 'Student Management System'))
    i = 0
    for key, value in menu_message.items():
        temp = '{}. {}'.format(key, value)
        print('{:<26}'.format(temp), end='')
        i += 1
        if i == 2:
            print()
            i = 0
    print('=' * 45)


def show_student_info():
    print('{0}{1}{0}'.format('=' * 14, 'Show Student Info'))
    print('|{:<8}|{:<16}|{:<8}|{:<8}|'.format('No.', 'Name', 'Age', 'Class'))
    print('-' * 45)
    for i in student_info:
        print('|{:<8}|{:<16}|{:<8}|{:<8}|'.format(i, student_info[i][0], student_info[i][1], student_info[i][2]))


def add_student_info():
    print('{0}{1}{0}'.format('=' * 15, 'Add Student Info'))
    number = input('please input student\'s No.: ')
    name = input('please input student\'s name: ')
    age = input('please input student\'s age: ')
    class_stu = input('please input student\'s class: ')
    student_info[number] = [name, age, class_stu]
    print('No. {} student info added successfully!'.format(number))


def delete_student_info():
    print('{0}{1}{0}'.format('=' * 13, 'Delete Student Info'))
    number = input('please input student No.: ')
    student_info.pop(number)
    print('No.{} student info deleted successfully!'.format(number))


def exit_system():
    print('{0}{1}{0}'.format('=' * 18, 'Good-Bye'))


if __name__ == '__main__':
    student_info = {'1111': ['zhengyx17', '24', '02'], '1112': ['liujh17', '24', '03']}
    menu()
    while True:
        option = input('please input your option: ')
        if option == '1':
            show_student_info()
            input('press Enter to continue...')
            print('\n')
            menu()
        elif option == '2':
            add_student_info()
            input('press Enter to continue...')
            print('\n')
            menu()
        elif option == '3':
            delete_student_info()
            input('press Enter to continue...')
            print('\n')
            menu()
        elif option == '4':
            exit_system()
            break
        else:
            print('wrong input! please input number from 1 to 4!')
