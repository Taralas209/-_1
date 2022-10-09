def find_number(name, telbook={"Иван": "3916", "Катя": "1298", "Лена": "0010"}):
    if name in telbook:
       print(f" Номер {name}:{telbook[name]}")
    else:
        print("undefined")

telbook = {"Иван": "3916", "Катя": "1298", "Лена": "0010"}

name = input("Введите имя:")
find_number(name)
