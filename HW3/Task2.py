def user_info(name, surname, year, city, email, phone):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город: {city}, Почтa: {email}, Телефон: {phone}')


n = input('Имя: ')
s = input('Фамилия: ')
y = input('Год рождения: ')
c = input('Город: ')
e = input('Почтa: ')
p = input('Телефон: ')

user_info(name=n, surname=s, year=y, city=c, email=e, phone=p)
