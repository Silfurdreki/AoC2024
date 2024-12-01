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

    list2_numbers = {}
    for number in set(list2):
        count = list2.count(number)
        list2_numbers.update({number: count})

        sim_scores = []
    for number in list1:
        try:
            sim_scores.append(number * list2_numbers[number])
        except KeyError:
            sim_scores.append(0)

    total = sum(sim_scores)
    print(f"Result: {total}")
