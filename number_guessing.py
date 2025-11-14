import random

min_num = 1
max_num = 100

choosen_number = random.randint(min_num, max_num)
attempts = 0

while True:
    try:
        guess = int(input(f"Gondoltam egy számra {min_num} és {max_num} között. Szám: "))
        
        if guess < min_num or guess > max_num:
            print(f"A szám csak {min_num} és {max_num} között lehet!")
            continue

        attempts += 1

        if guess == choosen_number:
            print(f"Kitaláltad a számot {attempts} próbálkozásból! Szép munka!")
            restart = input("Szeretnél egy új játékot kezdeni? Üsd be az 'i' betűt ha igen: ")
            if restart == 'i':
                choosen_number = random.randint(min_num, max_num)
                attempts = 0
                continue
            else:
                print("Kilépés...")
                break

        if guess < choosen_number:
            print(f"A gondolt szám nagyobb mint {guess}")
        else:
            print(f"A gondolt szám kisebb mint {guess}")

    except ValueError:
        print("Csak számot adhatsz meg!")