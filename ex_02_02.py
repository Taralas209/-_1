calc = input("Enter: ")

if '#' in calc:
    position = calc.find('#')
    second = float(calc[position+1:])
    first = float(calc[:position])
    print(second % first)

elif '!' in calc:
    position = calc.find('!')
    second = calc[position + 1:]
    first = calc[:position]
    totalf = 0
    totals = 0

    for i in first:
        totalf = totalf + int(i)
    for i in second:
        totals = totals + int(i)
    #а можно это всё в один цикл??

    if totalf > totals:
        print(first)
    elif totalf < totals:
        print(second)
    else:
        print('same amount')

elif '@' in calc:
    position = calc.find('@')
    second = int(calc[position + 1:])
    first = int(calc[:position])

    if first > second:
        print(first)
    elif first < second:
        print(second)
    else:
        print('numbers are equal')

elif '$' in calc:
    position = calc.find('$')
    second = len(calc[position + 1:])
    first = len(calc[:position])

    if first > second:
        print(first)
    elif first < second:
        print(second)
    else:
        print('numbers have same length')

else:
     print('Try again')
