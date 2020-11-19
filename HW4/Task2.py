my_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_numbers[i] for i in range(1, len(my_numbers)) if my_numbers[i] > my_numbers[i-1]]
print(new_list)