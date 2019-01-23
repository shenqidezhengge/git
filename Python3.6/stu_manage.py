import json


def menu():
    menu_message = {'1': 'show student info', '2': 'add student info', '3': 'delete student info',
                    '4': 'exit system'}
    message = """
=============student manage system=============
1. %s\t\t\t2. %s
3. %s\t\t\t4. %s
    """ %(menu_message['1'], menu_message['2'], menu_message['3'], menu_message['4'])
    return message


def show_student(student_message):
    print('=' * 15 + 'student info' + '=' * 15)
    if student_message:
        print('|{:<5}|{:<10}|{:<4}|{:<10}|'.format('number', 'name', 'age', 'class'))
        print('-' * 40)
        for student in student_message:
            name = student
            age = student_message[name][0]
            classid = student_message[name][1]
            # message =
    else:
        print('no such student, please add student info!')
    input('press Enter to continue...')


def add_student(student_message):
    print('add student info')
    student_name = input('please input name: ')
    student_age = input('please input age: ')
    student_class = input('please input class: ')

    student_message[student_name] = [student_age, student_class]
    print('%s, add student successfully!' % student_name)
    input('type Enter to continue...')
    return student_message


def del_student(student_message):
    print('=' * 10 + 'delete student info' + '=' * 10)
    if student_message:
        student_name = input('please input student name you want to delete: ')
        if student_name in student_message:
            student_message.pop(student_name)
        else:
            print('%s student info does not exit!' % student_name)
    else:
        print('student info does not exist!')


def main():
    print(menu())
    student_message = dict()
    try:
        with open('student_message.json', mode='r', encoding='utf-8') as f:
            student_message = json.load(f)
    except Exception:
        pass
    while True:
        command = input('input your option: ')
        if command == '4':
            print('=============good-bye=============')
            with open('student_message.json', mode='w', encoding='utf-8') as f:
                json.dump(student_message, f)
            break
        elif command == '1':
            show_student(student_message)
            print(menu())
        elif command == '2':
            add_student(student_message)
            print(menu())
        elif command == '3':
            del_student(student_message)
            print(menu())
        else:
            print('wrong input, please re-input.')


if __name__ == '__main__':
    main()
