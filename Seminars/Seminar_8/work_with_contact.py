from readfile import CreateDictionaryFromFile, ShowContacts


def AddContact():
    contacts_dict = CreateDictionaryFromFile()
    print('Добавляем новый контакт...')
    name = input('Введите ФИО: ')
    tel = input('Введите тел: ')
    comment = input('Введите комментарий: ')
    contacts_dict.update({len(contacts_dict.keys()) + 1: [name, tel, comment]})
    print(f'Добавлен братишка: {contacts_dict[len(contacts_dict.keys())][0]}')
    return contacts_dict


def WriteDictInFile(contacts_dict: dict):
    file = open('sample.txt', 'a', encoding='UTF-8')
    file.write(f'{contacts_dict[len(contacts_dict.keys())][0]};'
               f'{contacts_dict[len(contacts_dict.keys())][1]};'
               f'{contacts_dict[len(contacts_dict.keys())][2]}\n')
    file.close()


def DeleteContact(contact_number):
    contacts_dict = CreateDictionaryFromFile()
    del contacts_dict[contact_number]
    with open('sample.txt', 'w+') as file:
        for value in contacts_dict.values():
            file.write(f'{value[0]};'
                       f'{value[1]};'
                       f'{value[2]}')
    file.close()


def EditContact():
    contacts_dict = CreateDictionaryFromFile()
    ShowContacts()
    contact_number = int(input('Введите номер записи, которую вы хотите изменить (записи выше): '))
    index_in_contacts = input('Что вы хотите изменить? (Напишите "ФИО", "Телефон", "Комментарий"): ')
    new_values_list = contacts_dict[contact_number]
    new_value = input('Введите новое значение: ')
    if index_in_contacts == 'ФИО':
        new_values_list[0] = new_value
    if index_in_contacts == 'Телефон':
        new_values_list[1] = new_value
    if index_in_contacts == 'Комментарий':
        new_values_list[2] = new_value
    contacts_dict.update({len(contacts_dict.keys()) + 1: new_values_list})
    del contacts_dict[contact_number]
    with open('sample.txt', 'w+') as file:
        for value in contacts_dict.values():
            file.write(f'{value[0]};'
                       f'{value[1]};'
                       f'{value[2]}')
    file.close()
