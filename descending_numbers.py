"""

    6 5 4 3 2 1  
    6 5 4 3 2
    6 5 4 3
    6 5 4
    6 5
    6
    
"""

number = 0

while True:
    num = input("Kérem adjon meg egy pozitív egész számot 3 és 100 között: ")
    if num.isdigit():
        num = int(num)
        if num >= 3 and num <= 100:
            number = num
            break

for i in range(1, number + 1):
    for j in range(number, i-1, -1):
        print(j, end=" ")
    print(" ")