passw = ['12345', '8888']
while True:
    inpt = input('Enter your password: ')
    if inpt == "":
        print('(!) строка пуста')
    elif inpt in passw:
        print('Вход разрешен')
    elif inpt == 'quit':
        break
    else:
        print('Не правильный пароль!')
