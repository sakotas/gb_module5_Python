import readfile as rf
import work_with_contact as wc

if __name__ == '__main__':
    rf.ShowMenu()

    while True:
        choice = int(input('Выберите пункт меню (Показать меню "5"): '))
        if choice == 1:
            rf.ShowContacts()
            print()
        if choice == 2:
            new_contact_dict = wc.AddContact()
            wc.WriteDictInFile(new_contact_dict)
            print()
        if choice == 3:
            wc.EditContact()
        if choice == 4:
            rf.ShowContacts()
            contact_number = int(input('Номер записи, которую необходимо удалить: '))
            wc.DeleteContact(contact_number)
        if choice == 5:
            rf.ShowMenu()
        if choice == 6:
            print('Спасибо, что воспользовались этой прекрасной записной книжкой')
            break
