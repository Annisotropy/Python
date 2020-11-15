n = int(input('Введите количество всех товаров: '))
my_list = []
i=1
while i <= n:
    my_list.append(
        (i, {'название': input('Введите наименование товара: '),
             'цена': input('Введите цену: '),
             'количество': input('Введите количество: '),
             'ед': input('Введите единицы (шт, кг, л): ')
             }
         )
    )
    i=i+1
print(my_list)

my_dict = {'название': [],
           'цена': [],
           'количество': [],
           'ед': []
           }

for g in my_list:
    name_of_product = g[1]['название']
    my_dict['название'].append(name_of_product)

    price = g[1]['цена']
    my_dict['цена'].append(price)

    quantity = g[1]['количество']
    my_dict['количество'].append(quantity)

    units = g[1]['ед']
    my_dict['ед'].append(units)

print(my_dict)
