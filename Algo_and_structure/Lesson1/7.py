print('Введите длины трегольника.')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('Треугольник существует.')
    if a == b and b == c:
        print('Этот треугольник равнобедренный.')
#   if <условие прямоугольного треуголика>:
#       print('Этот треугольник прямоугольный.')
#
else:
    print('Треугольник не существует.')
