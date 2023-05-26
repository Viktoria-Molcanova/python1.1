#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import sys
def homepage(Phone_book):
    while True:
        print('Программа телефонный справочник. Введите команду')
        user = input('\n1 - Найти\n2- Добавить контактn\n3 - Изменить контакт\n4 - Удалить контакт\n5 - Просмотр всех контактов\n6 - Выход\n')
        print( )
        if user == '1':
            contact_list = ReadFile(Phone_book)
            find(contact_list)
        elif user == '2':
            add(Phone_book)
        elif user == '3':
            edit(Phone_book)
        elif user== '4':
            delete(Phone_book)
        elif user == '5':
            show(Phone_book)
        elif user == '6':
           sys.exit() # Выход из приложения
        else:
            print('Ошибка! Повторите попытку ввода')
            print()
            continue
            
# Создание файла

from os import path
filename = "data.txt"
if not path.exists(filename):
    with open(filename, "w", encoding="utf-8") as _:
        pass


def ReadFile(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def readFile(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list

# Поиск  контакта

def Search():
    print('Данные для поиска')
    field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    ValueSearch = None
    if field == '1':
        ValueSearch = input('Введите фамилию ')
        print()
    elif field == '2':
        ValueSearch = input('Введите имя  ')
        print()
    elif field == '3':
        ValueSearch = input('Введите номер  ')
        print()
    return field, ValueSearch


def find(contact_list):
    field, ValueSearch = Search()
    ValueSearch_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    contact__ = []
    for contact in contact_list:
        if contact[ValueSearch_dict[field]] == ValueSearch:
            contact__.append(contact)
    if len(contact__) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(contact__)
    print()

 # Новый контакт

def new():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    print('Контакт сохранён')
    return last_name, first_name, phone_number


def add(file_name):
    info = ' '.join(new())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')
        
# Просмотр всех контактов

def show(file_name):
    list_of_contacts = sorted(ReadFile(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts
  
# Изменение контакта

def Modify(contact_list: list):
    field, ValueSearch = Search()
    res = []
    for contact in contact_list:
        if contact[int (field) - 1] == ValueSearch:
            res.append(contact)
    if len(res) == 1:
        return res[0]
    elif len(res) > 1:
        print('Найдено несколько контактов')
        for i in range(len(res)):
            print(f'{i + 1} - {res[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return res[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def edit(file_name):
    contact_list = readFile(file_name)
    number_to_change = Modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)

# Удаление контакта

def delete(file_name):
    contact_list = readFile(file_name)
    number_to_change = Modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'Phone_book.txt'
    homepage(file)
