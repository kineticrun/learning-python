import random

min_num = 1
max_num = 100

choosen_number = random.randint(min_num, max_num)

while True:
    try:
        guess = int(input(f"Gondoltam egy számra {min_num} és {max_num} között. Szám: "))
        
        if guess == choosen_number:
            print("Kitaláltad a számot! Szép munka!")
            break

        if guess < choosen_number:
            print(f"A gondolt szám nagyobb mint {guess}")
        else:
            print(f"A gondolt szám kisebb mint {guess}")
    except ValueError:
        print("Csak számot adhatsz meg!")