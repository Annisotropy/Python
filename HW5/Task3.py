with open('text3.txt', 'r') as f:
    employees = f.readlines()
    add = 0
    for employee in employees:
        employee = employee.split()
        if int(employee[2]) < 20000:
            print(employee[1])
        add += int(employee[2])
    average = add/len(employees)
    print('Average salary: ', average)
