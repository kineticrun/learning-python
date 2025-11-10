"""
Készítsünk konzol programot, mely előállítja egy lottó sorsolás számait!
A lottó számok nem ismétlődhetnek.
"""

import random

lottery = []

while len(lottery) < 5:
    number = random.randint(1,90)
    if number not in lottery:
        lottery.append(number)
        print(number)

print(sorted(lottery))