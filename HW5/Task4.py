with open('text4.txt', 'r', encoding='utf-8') as f:
    with open ('text4_new.txt', 'w', encoding='utf-8') as f2:
        for line in f:
            a = line.replace('One', 'один').replace('Two', 'два').replace('Three', 'три').replace('Four', 'четыре')
            f2.write(a)

