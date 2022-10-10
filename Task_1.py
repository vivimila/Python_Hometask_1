try:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    if number1 ** 2 == number2:
        print(f'{number2} является квадратом числа {number1}')
    elif number2 ** 2 == number1:
        print(f'{number1} является квадратом числа {number2}')
    else:
        print('Ни одно из числе не является квадратом другого')
except:
    print('Введите целое число')