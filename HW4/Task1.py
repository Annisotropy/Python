from sys import argv


def salary(rate, hours, bonus):
    sal = int(rate)*int(hours) + int(bonus) 
    return sal


script_name, rate, hours, bonus = argv
sal = salary(rate, hours, bonus)


print("Имя скрипта: ", script_name)
print("Salary: ", sal)
