from itertools import cycle

a = 0
for el in cycle("ANNA"):
    if a > 11:
        break
    print(el)
    a += 1
    