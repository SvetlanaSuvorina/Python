# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4


"""
print("Введите число: ")
n = int(input())
while n >= 10 or n <= 0:
    n = int(input('Число неверно. Введите число от 0 до 10: '))
if n > 0 and n < 10:
    print('Вы ввели корректное число.')
    print('Число',n,'в степени 2 равно ',n**2,'.') # как в строке выше выводить символ точки '.' сразу за значением без пробела? см.вывод.


"""


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

a = int(input('Введите значение 1-ой переменной: '))
b = int(input('Введите значение 2-ой переменной: '))
b = a + b
a = b - a
b = b - a
print('Знчение 1 -> 2: ', a)
print('Знчение 2 -> 1: ', b)

#вдогонку к задаче easy