def my_func(a, b, c):
    return sum([a, b, c]) - min(a, b, c)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print(my_func(a, b, c))
