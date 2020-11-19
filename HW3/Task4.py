#1
def func(x, y):
    r = x**y
    return r


a = int(input('Введите действительное число: '))
b = int(input('Введите целое отрицательное число: '))
print(func(a, b))

#2
def func2(x, y):
    i = 1
    result = 1
    while i <= abs(y):
        result *= 1/x
        i += 1
    print(result)


n = int(input('Введите действительное число: '))
k = int(input('Введите целое отрицательное число: '))
func2(n, k)



