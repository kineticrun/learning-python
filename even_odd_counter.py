"""
Írjunk olyan programot, amely addig kér be egész számokat a billentyűzetről, amíg azok összege meg nem haladja a 100-at. 
A beolvasás végén írjuk ki azt, hogy a bekért számok közül hány volt páros, és hány volt
páratlan.
"""

num_vector = []
total = 0

while True:
    num = input("Kérem adjon meg egy pozitív egész számot: ")
    if num.isdigit() and int(num) > 0:
        num = int(num)
        num_vector.append(num)
        total += num
        if total >= 100:
            break
    else:
        print("Csak számokat adhat meg.")

even_numbers_count = len([i for i in num_vector if i % 2 == 0])
odd_numbers_count = len(num_vector) - even_numbers_count

print(f"A megadott számok közül {even_numbers_count} páros és {odd_numbers_count} páratlan szám fordult elő.")