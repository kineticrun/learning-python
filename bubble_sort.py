import random

def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - i - 1):
            if my_list[j] < my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp

my_list = [random.randint(1, 1000) for i in range(1, 100 + 1)]
print(my_list)
bubble_sort(my_list)
print(my_list)