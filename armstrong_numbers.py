"""
Írjon egy Python függvényt, ami a bemenetül kapott számról eldönti, hogy Armstrong-szám 
vagy sem! Armstrong-számnak nevezzük az olyan n jegyű számot, melynek minden számjegyét 
az n-edik hatványra emelve és összeadva az eredeti számot kapjuk. A megoldásban használja az 
előre megadott szintaktikát! A függvénynek átadott paraméter helyességét nem kell 
ellenőriznie
"""


def is_armstrong(number):
    sum = 0
    for n in number:
        sum += (int(n)**int(len(number)))
    if sum == int(number):
        return True
    return False

number = input("Adjon meg egy számot: ")
print(is_armstrong(number))