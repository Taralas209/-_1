calc = input("Enter: ")

if '#' in calc:
    position = calc.find('#')
    second = float(calc[position+1:])
    first = float(calc[:position])
    print(second % first)

    # можно разбивать строку так:
    # first, second = calc.split('#')
    # print(int(second) % int(first))

elif '!' in calc:
    position = calc.find('!')
    second = calc[position + 1:]
    first = calc[:position]
    totalf = 0
    totals = 0

    for i in first:
        totalf = totalf + int(i)
        # аналог: totalf += int(i)
    for i in second:
        totals = totals + int(i)
        # вот такой метод тоже интересный
        # string = '123456'
        # numbers_sum = sum([int(num) for num in string])
        # numbers_sum = sum(map(int, string))

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
    print(type(first))
    print(type(second))

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
