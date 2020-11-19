def my_func(word):
    return word[0].upper() + word[1:]

phrase = input('Введите любую фразу с маленькой буквы: ')
phrase = phrase.split()
new_phrase = ''
for word in phrase:
    new_phrase += my_func(word) + ' '
print(new_phrase)

