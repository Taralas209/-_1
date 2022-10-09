def find_number(name):
    if name in telbook:
        return name, telbook[name]
    else:
        return 'undefined'

def output(result):
    if result == 'undefined':
        print(f"Cannot find '{name}'")
    else:
        print(f"{result[0]}`s number: {result[1]}")

telbook = {"John": "3916", "Кate": "1298", "Lena": "0010"}

name = input('Enter name:')
result = find_number(name)
output(result)
