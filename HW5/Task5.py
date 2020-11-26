with open('text5.txt', 'w', encoding='utf-8') as f:
    f.write('1 2 3 4 5 6 7')
with open('text5.txt', 'r', encoding='utf-8') as f2:
    content = f2.read().split()
    a = [int(i) for i in content]
    print(sum(a))

