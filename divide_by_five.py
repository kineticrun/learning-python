def check_input(value):
    if value.isdigit():
        value = int(value)
        if value >= 1 and value <= 100:
            return True
    return False

interval = []

while True:
    text = input("Adja meg az intervallum minimumát 1-100: ")
    if check_input(text):
        text = int(text)
        interval.append(text)
        break

while True:
    text = input("Adja meg az intervallum maximumát 1-100: ")
    if check_input(text):
        text = int(text)
        if text > interval[0]:
            interval.append(text)
            break
        else:
            print("Az maximum érték nem lehet kisebb mint a minimum.")

divide_by_five = []

for i in range(interval[0], interval[1] + 1):
    if i % 5 == 0:
        divide_by_five.append(i)

print(sum(divide_by_five))
