open_file
show_contacts
save_file
add_contact
find_contact
change_contact
delete_contact

def menu():
    print('Это меню телефонного справочника:\n'
          '1.Открыть файл\n'
          '2.Сохранить файл\n'
          '3.Показать контакты\n'
          '4 Добавить контакт\n'
          '5 Найти контакт\n'
          '6 Изменить контакт\n'
          '7 Удалить контакт\n'
          '8 Выход\n')
    data = int(input('Выберите действия: '))
    return data
while True:
      user_choise = menu()
      match user_choise:
            case 1:
                  open_file()
            case 2:
                  save_file()
            case 3:
                  show_contacts()
            case 4:
                  add_contact()
            case 5:
                  find_contact()
            case 6:
                  change_contact()
            case 7:
                  delete_contact()
            case 8:
                  print('Выход')
                  break
