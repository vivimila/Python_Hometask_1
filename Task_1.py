# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

try:
    number1 = int(input('Введите число, которое обозначает день недели: '))
    #number2 = int(input('Введите второе число: '))
    if number1 == number1 < 6:
        print(f'это рабочий день недели')
    elif number1  == 6 <= number1 or number1 <= 7:
        print(f'это выходной')
    else:
        print('Введено неверное значение')
except:
    print('Введите целое число')