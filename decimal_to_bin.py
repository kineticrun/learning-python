"""
Írjunk egy Python függvényt, amely bemenetül egy 10-es számrendszerű számot kap, és 
visszatér annak bináris formájával. Ha a bemenet nem pozitív egész, akkor 0-val térjen vissza! A 
megoldásban használja az előre megadott szintaktikát!
"""

def decimal_to_bin(number):
    if number <= 0:
        return 0
    return bin(number)[2:].zfill(8)

print(decimal_to_bin(42))
print(decimal_to_bin(0))
print(decimal_to_bin(-42))