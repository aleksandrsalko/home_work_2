# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

float_number = input('Введите вещественное число: ')

sum = 0
for i in float_number:
    if i != '.' and i != '-':
        sum += int(i)
print('Сумма числа =', sum)