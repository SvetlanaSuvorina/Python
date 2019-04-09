import random
import string

print('Введите границы диапазона, в которых нужно вывести случайное целое число.'
      '\n'
      '\nВнимание! Начало границы диапазона должно быть меньше конца границы диапазона.'
      '\n')
value_start = int(input('Начало границы диапазона: '))
value_end = int(input('Конец границы диапазона: '))
print(f'\nСлучайное целое число в диапазоне [{value_start};{value_end}]: {random.randint(value_start,value_end)}.')

print('\nВведите границы диапазона, в которых нужно вывести случайное вещественное число.')
value_start = float(input('Начало границы диапазона: '))
value_end = float(input('Конец границы диапазона: '))
print(f'Случайное вещественное число в диапазоне [{value_start};{value_end}]: {random.uniform(value_start,value_end)}.')

print('\nВведите границы диапазона, в которых нужно вывести случайный символ.')
value_start = input('Начало границы диапазона: ')
value_end = input('Конец границы диапазона: ')
print(f'Случайный символ между {value_start} и {value_end}: {chr(random.randint(ord(value_start),ord(value_end)))}.')

