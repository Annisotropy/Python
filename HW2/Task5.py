my_list = [10, 7, 7, 4, 2, 2, 1]
rank = int(input('Введите любое целое число от 0 до 100: '))

i = 0
while i<len(my_list) and rank <= my_list[i]:
    i=i+1
my_list.insert(i, rank)
print(my_list)