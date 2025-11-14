"""
Valósítsunk meg a Fizz buzz játékot! A játék lényege, hogy 1-től
kezdve soroljuk az egész számokat. Ha a következő szám osztható
3-mal, akkor a szám helyett "fizz"-t mondunk, ha 5-tel osztható,
akkor "buzz"-t, viszont ha mindkettővel osztható, akkor "fizzbuzz"-t.
Legyen szabályozható, hogy mettől meddig szeretnénk számolni!
"""

num_from = 1
num_to = 100

for i in range(num_from, num_to + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)