seconds = int(input('Введите количество секунд: '))
print('Вы ввели: ', seconds, 'секунд')

m, s = divmod(seconds, 60)
h, m = divmod(m, 60)

# print(h, ':', m, ':', s)
# print(str(h) + ':' + str(m) + ':' + str(s))
print('Точное время: ', '{:02d}:{:02d}:{:02d}'.format(h, m, s))



