with open('text2.txt', 'r') as f:
    content = f.readlines()
    print('Lines number: ', len(content))
    for line in content:
        words = len(line.split())
        print('Words number in line: ', words)