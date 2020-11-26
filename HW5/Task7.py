import json

with open('text7.txt', encoding='utf-8') as f:
    lines = f.readlines()
    my_dict1 = {}
    for line in lines:
        split = line.split()
        company = split[0]
        profit = int(split[2]) - int(split[3])
        my_dict1[company] = profit
success = [i for i in my_dict1.values() if i > 0]
my_dict2 = {'average profit': sum(success)/len(success)}
my_list = [my_dict1, my_dict2]
print(my_list)

with open("text7.json", "w") as write_f:
    json.dump(my_list, write_f)
