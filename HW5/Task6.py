with open('text6.txt', encoding='utf-8') as f:
    lines = f.readlines()
    my_dict = {}
    for line in lines:
        split = line.split(':')
        subject = split[0]
        hours = split[1]
        hours = hours.replace('(л)', '').replace('(пр)', '').replace('-', '').replace('(лаб)', '').replace('\n', '').replace('.', '')
        hours = [int(i) for i in hours.split()]
        my_dict[subject] = sum(hours)
print(my_dict)


