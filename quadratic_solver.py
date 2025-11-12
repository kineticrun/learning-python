import math

a = None
b = None
c = None

def check_input(value):
    if value.count('.') > 1:
        return False
    elif value.count('.') > 0:
        value = value.replace(".", '')
    if value.lstrip('-').isdigit():
        return True
    return False

print("Adja meg a másodfokú polinom eggyüthatóit.")

while True:
    a = input("a: ")
    if check_input(a) and float(a) != 0:
            break
    print("Hibás adatot adott meg!")


while True:
    b = input("b: ")
    if check_input(b):
        break
    print("Hibás adatot adott meg!")


while True:
    c = input("c: ")
    if check_input(c):
        break
    print("Hibás adatot adott meg!")

a = float(a)
b = float(b)
c = float(c)

discriminant = (b**2) - (4 * a * c)

if discriminant < 0:
    print("Az egyenletnek nincs valós gyöke.")
elif discriminant == 0:
    result = -b / (2 * a)
    print(f"Az egyenletnek egy megoldása van: x = {result}")
    print(f"Gyöktényezős alak: (x-({result}))^2")
elif discriminant > 0:
    result1 = (-b + math.sqrt(discriminant)) / (2 * a)
    result2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Az egyenletnek két valós gyöke van: x1 = {result1} és x2 = {result2}")
    print(f"Gyöktényezős alak: {a}*(x-({result1}))*(x-({result2}))")