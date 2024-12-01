import csv
import numpy as np
import pdb

input_file = "input.txt"

list1 = []
list2 = []

with open(input_file) as input:
    for line in input:
            numbers = line.split()
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

    list1 = np.sort(list1)
    list2 = np.sort(list2)

    distances = []

    for i, number1 in enumerate(list1):
        distances.append(np.abs(list1[i] - list2[i]))

    total = sum(distances)
    print(f"Result: {total}")
