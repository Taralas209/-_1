def find_number(name):
    # конструкцию if-else можно заменить однострочником:
    # print(telbook.get(name, "undefined"))
    if name in telbook:
       print(f" Номер {name}:{telbook[name]}")
    else:
        print("undefined")

telbook = {"Иван": "3916", "Катя": "1298", "Лена": "0010"}

name = input("Введите имя:")
# желательно name чистить после пользователя
# name = input("Введите имя:").strip().capitalize()
# функцию лучше проектировать без функций print внутри..
# функция должна принять значение и вернуть значение
# а мы сами уже решим, что с возвращенным значением делать

find_number(name)
