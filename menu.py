

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
                  print('Открыть файл')
            case 2:
                  print('Показать контакты')
            case 3:
                  print('Сохранить файл')
            case 4:
                  print('Добавить контакт')
            case 5:
                  print('Найти контакт')
            case 6:
                  print('Изменить контакт')
            case 7:
                  print('Удалить контакт')
            case 8:
                  print('Выход')
      break
