def division(a, b):
    if b == 0:
        b = int(input('Введите второе число, не равное нулю: '))
    return a/b


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print('Деление: ', division(a, b))

division(1, 2)
division(a=1, b=2)