def CreateDictionaryFromFile():
    contacts_dict = {}
    file = open('sample.txt', 'r', encoding='UTF-8')
    for key, value in enumerate(file.readlines(), start=1):
        contacts_dict[key] = value
    file.close()
    for key, value in contacts_dict.items():
        contacts_dict[key] = value.split(';')
    return contacts_dict


def ShowContacts():
    print('Показываю все контакты: ')
    contacts_dict = CreateDictionaryFromFile()
    for key, value in contacts_dict.items():
        print(f"Запись № {key}")
        print(f"ФИО: {value[0]}")
        print(f"Тел: {value[1]}")
        print(f"Комментарий: {value[2]}")


def ShowMenu():
    print('Главное меню: ')
    print('1. Показать всю книгу')
    print('2. Добавить новую запись')
    print('3. Редактировать запись')
    print('4. Удалить запись')
    print('5. Показать меню')
    print('6. Выйти')
    print()
