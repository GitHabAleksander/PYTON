# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и
# Вы должны реализовать функционал для изменения и удаления данных



def menu_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.csv')
    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname: ')
            result = find_by_lastname(phone_book, last_name)
            if result:
                print_result(result)
            else:
                print("Абонент не найден.")
        elif choice == 3:
            last_name = input('lastname: ')
            new_number = input('new number: ')
            result = change_number(phone_book, last_name, new_number)
            if result:
                print("Телефон изменен.")
            else:
                print("Абонент не найден.")
        elif choice == 4:
            lastname = input('lastname: ')
            result = delete_by_lastname(phone_book, lastname)
            if result:
                print("Абонент удален.")
            else:
                print("Абонент не найден.")
        elif choice == 5:
            number = input('number: ')
            result = find_by_number(phone_book, number)
            if result:
                print_result(result)
            else:
                print("Абонент не найден.")
        elif choice == 6:
            user_data = input('Введите фамилию, имя, номер телефона и описание через запятую: ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
            print("Абонент добавлен.")
        else:
            print("Ошибка в выборе.")
        choice = show_menu()


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for contact in phone_book:
            values = ','.join(contact.values())
            phout.write(f'{values}\n')


def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep='\n')
    while True:
        try:
            choice = int(input("Введите номер меню: "))
            if 1 <= choice <= 7:
                break
            else:
                print("Ошибка в выборе.")
        except ValueError:
            print("НОшибка в выборе.")
    return choice


def print_result(phone_book):
    if phone_book:
        for contact in phone_book:
            print(contact)
    else:
        print("Справочник пуст.")


def find_by_lastname(phone_book, last_name):
    result = []
    for contact in phone_book:
        if contact['Фамилия'] == last_name:
            result.append(contact)
    return result


def change_number(phone_book, last_name, new_number):
    for contact in phone_book:
        if contact['Фамилия'] == last_name:
            contact['Телефон'] = new_number
            return True
    return False


def delete_by_lastname(phone_book, last_name):
    removed = True
    phone_book[:] = [contact for contact in phone_book if contact['Фамилия'] != last_name]
    return removed


def find_by_number(phone_book, number):
    result = []
    for contact in phone_book:
        if contact['Телефон'] == number:
            result.append(contact)
    return result


def add_user(phone_book, user_data):
    data = user_data.split(',')
    if len(data) == 4:
        new_contact = {
            'Фамилия': data[0].strip(),
            'Имя': data[1].strip(),
            'Телефон': data[2].strip(),
            'Описание': data[3].strip()
        }
        phone_book.append(new_contact)
    else:
        print("Ошибка ввода.")


if __name__ == '__main__':
    menu_phonebook()