# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

from csv import DictReader, DictWriter
from os.path import exists


def create_file():
    with open('Phone.csv', "w", encoding="utf-8") as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()


def get_info():
    info = ['Иванов', 'Иван', '12-16-18']
    return info


def read_file(file_name):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res


def write_file(file_name, lst):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    obj = {"Фамилия": lst[0], "Имя": lst[1], "Номер": lst[2]}
    res.append(obj)
    with open('Phone.csv', "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)


def find_record(file_name):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    info = input("Введите данные для поиска: ")
    for el in res:
        for el2 in el.values():
            if info in el2:
                print(el)


def change_record(file_name, lst):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    obj = {"Фамилия": lst[0], "Имя": lst[1], "Номер": lst[2]}
    lst2 = ['Петров', 'Петр', '98-76-54']
    obj2 = {"Фамилия": lst2[0], "Имя": lst2[1], "Номер": lst2[2]}
    for i in range(len(res)):
        if obj == res[i]:
            res[i] = obj2
    with open('Phone.csv', "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)


def delete_record(file_name, lst):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    obj = {"Фамилия": lst[0], "Имя": lst[1], "Номер": lst[2]}
    for i in range(len(res)):
        if obj == res[i - len(res)]:
            res.pop(i)
    with open('Phone.csv', "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)


def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "r":
            if not exists('Phone.csv'):
                break
            print(read_file('Phone.csv'))
        elif command == "w":
            if not exists('Phone.csv'):
                create_file()
            write_file('Phone.csv', get_info())
        elif command == 'f':
            if not exists('Phone.csv'):
                print("Телефонный справочник пуст")
            find_record('Phone.csv')
        elif command == 'c':
            if not exists('Phone.csv'):
                print("Телефонный справочник пуст")
            change_record('Phone.csv', get_info())
        elif command == 'd':
            if not exists('Phone.csv'):
                print("Телефонный справочник пуст")
            delete_record('Phone.csv', get_info())


main()