"""
Készítsünk programot, mely bekér két számot, majd kiírja az összegüket, a különbségüket, a szorzatukat és a hányadosukat.
Az adatokat a billentyűzetről olvassuk be. 
A beolvasást mindaddig végezzük, míg helyes adatokat nem kapunk.
"""

num_vector = []

while len(num_vector) < 2:
    num = input("Kérem adjon meg egy számot: ")
    if not num.isdigit():
        print("Csak pozitív egész számokat adhat meg!")
        continue
    elif int(num) <= 0:
        print("Csak pozitív egész számokat adhat meg!")
        continue
    num_vector.append(int(num))

sum_of_two = sum(num_vector)
sub = num_vector[0] - num_vector[1]
prod = num_vector[0] * num_vector[1]
div = num_vector[0] / num_vector[1]

print("A két szám összege: " + str(sum_of_two))
print("A két szám külömbsége: " + str(sub))
print("A két szám szorzata: " + str(prod))
print("A két szám hányadosa: " + str(div))