phrase = input('Введите предложение из нескольких слов, разделенных пробелами: ')
words = phrase.split()
print(words)

for i, w in enumerate(words):
    print(i, w[0:10])
