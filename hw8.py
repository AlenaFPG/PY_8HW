def name_data():
    name = input('Введите Ваше имя: ')
    return name


def surname_data():
    surname = input('Введите Вашу фамилию: ')
    return surname


def phone_data():
    # import re
    phone = input('Введите Ваш телефон: ')
    return phone


def address_data():
    address = input('Введите Ваш адрес: ')
    return address

def copy_line(source_file, target_file, line_number):
    with open(source_file, 'r') as file:
        lines = file.readlines()
    if line_number < 1 or line_number > len(lines):
        print('Некорректный номер строки')
        return
    with ope(target_file, 'w') as file:
        file.write(lines[line_number - 1])
        for i in range(len(lines)):
            if i != line_number - 1:
                file.write(lines[1])
    print('Копирование строки успешно выполнено')

source_file = 'source.txt'
target_file = 'target.txt'
line_number = int(input('Введите номер строки : '))

copy_line(source_file, target_file, line_number)