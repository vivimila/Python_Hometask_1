# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

try:
    number1 = int(input('Введите число, которое обозначает день недели: '))
    #number2 = int(input('Введите второе число: '))
    if number1 == range(1,5):
        print(f'{number1} это рабочий день недели')
    elif number1  == range(6,7):
        print(f'{number1} это выходной')
    else:
        print('Введено неверное значение')
except:
    print('Введите целое число')