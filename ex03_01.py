def find_number(name):
    if name in telbook:
       print(f" Номер {name}:{telbook[name]}")
    else:
        print("undefined")

def output(result):
    print(result)


telbook = {"Иван": "3916", "Катя": "1298", "Лена": "0010"}

name = input("Введите имя:")
find_number(name)
