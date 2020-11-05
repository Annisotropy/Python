number = input('Введите целое положительное число: ')
# number = '51293'

max_digit = 0
index = 0
length = len(number)
while index < length:
    current_digit = int(number[index])
    if current_digit > max_digit:
        max_digit = current_digit
    index = index + 1

print(max_digit)
