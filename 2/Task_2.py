char = '*'

while True:
    user_command = input("Введите команду: ")
    if user_command == 'а':
        spaces = 0
        for i in range(9, 0, -1):
            print(" " * spaces + char * i)
            spaces += 1

    elif user_command == 'б':
        for i in range(1, 10):
            print(char * i)

    elif user_command == 'в':
        n = 5
        for i in range(n, 0, -1):
            print('{:^{str_len}}'.format('* ' * i, str_len=n * 2))

    elif user_command == 'г':
        n = 5
        for i in range(1, n+1):
            print('{:^{str_len}}'.format('* ' * i, str_len=n * 2))

    elif user_command == 'д':
        n = 5
        for i in range(n, 0, -1):
            print('{:^{str_len}}'.format('* ' * i, str_len=n * 2))
        n = 5
        for i in range(1, n + 1):
            print('{:^{str_len}}'.format('* ' * i, str_len=n * 2))

    elif user_command == 'е':
        columns = 5
        rows = 5
        for i in range(0, columns):
            for j in range(0, rows):
                if (j <= rows - 1 - i and j <= i) or (j >= rows - 1 - i and j >= i):
                    print('*', end='')
                else:
                    print(' ', end='')
            print('')

    elif user_command == 'ж':
        size = 6
        for i in range(size):
            print(*['*'] * (i if i < size // 2 else size - i))

    elif user_command == 'з':
        columns = 5
        rows = 5
        for i in range(0, columns):
            for j in range(0, rows):
                if j >= rows - 1 - i and j >= i:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('')

    elif user_command == 'и':
        for a in range(9, 0, -1):
            print(char * a)

    elif user_command == 'к':
        spaces = 8
        for i in range(1, 10):
            print(" " * spaces + char * i)
            spaces -= 1

    elif user_command == '0':
        exit()
    else:
        print("Ошибка! Нет такого варианта!")
