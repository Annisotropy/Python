elements = input('Введите любые числа или слова через пробел: ')
elements = elements.split()

print(elements)
for i, e in enumerate(elements):
    if i % 2 == 0:
        try:
            elements[i] = elements[i + 1]
            elements[i+1] = e
        except IndexError:
            print('...')
print(elements)

