def addition():
    game_on = True
    my_sum=0
    while game_on:
        numbers = input('Введите числа через пробел.\n Вы можете выйти в любой момент, нажав q: ')
        numbers = numbers.split()
        for number in numbers:
            if number =='q':
                game_on = False
                break
            my_sum += int(number)
        print(my_sum)
    print('finish')

    
addition()

