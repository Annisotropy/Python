with open('my_text.txt', 'w', encoding='utf-8') as f:
    user_list = input('Введите данные: ')
    while user_list:
        f.writelines(user_list + '\n')
        user_list = input('Введите данные: ')
