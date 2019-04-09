print('Введите три числа.')
one_number = int(input('Первое число:'))
two_number = int(input('Второе число:'))
three_number = int(input('Третье число:'))

if two_number < one_number < three_number or two_number > one_number > three_number:
        print('Среднее число первое.')
if one_number < two_number < three_number or one_number > two_number > three_number:
        print('Среднее число второе.')
if one_number > three_number > two_number or one_number < three_number < two_number:
        print('\nСреднее число третье.')

