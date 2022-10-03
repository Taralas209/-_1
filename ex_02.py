letters = 'Who keeps company with the wolf, will learn to howl.'
template = 'w'
exclude = 'l'
count = 0

for i in letters:
    if i == template:
        count = count + 1
    if not i == exclude:
        print(i)
    
print('Количество символов:', count)