#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Исп. линейный алгоритм

three_digit_number = int(input('Введите число от 100 до 999: '))
first_digit = (three_digit_number//100)
second_digit = three_digit_number%100//10
third_digit = three_digit_number-first_digit*100-second_digit*10
if first_digit == 0 or (first_digit == 0 and second_digit == 0):
    print('Это не трехзначное число. Слева располагается цифра 0. '
          '\nВведите число без нулей в первых разрядах. Например, 123. '
          '\nУ вас осталась последняя попытка!!!')
    three_digit_number = int(input('Введите число от 100 до 999 еще раз: '))
    first_digit = (three_digit_number // 100)
    second_digit = three_digit_number % 100 // 10
    third_digit = three_digit_number - first_digit * 100 - second_digit * 10
    if first_digit == 0 or (first_digit == 0 and second_digit == 0):
        print('Это не трехзначное число. '
              'Слева располагается цифра 0. '
              'Введите число без нулей в первых разрядах.')
print(f"Первая цифра в этом числе: {first_digit}")
print(f"Вторая цифра в этом числе: {second_digit}")
print(f"Третья цифра в этом числе: {second_digit}")
summary = first_digit+second_digit+third_digit
composition = first_digit*second_digit*third_digit
print('Cумма цифр числа:', summary)
print('Произведение цифр числа:', composition)





