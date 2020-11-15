#1
month1 = input('Введите любой месяц цифрой от 1 до 12: ')
my_dict = {'1': 'winter', '2': 'winter', '3': 'spring', '4': 'spring', '5': 'spring', '6': 'summer', '7': 'summer',
           '8': 'summer', '9': 'autumn', '10': 'autumn', '11': 'autumn', '12': 'winter'}
print(my_dict[month1])
#2
month2 = input('Введите любой месяц цифрой от 1 до 12: ')
my_dict = {'winter': ['1', '2', '12'], 'spring': ['3', '4', '5'], 'summer': ['6', '7', '8'], 'autumn':  ['9', '10', '11']}
for k, v in my_dict.items():
    if month2 in v:
        print(k)

