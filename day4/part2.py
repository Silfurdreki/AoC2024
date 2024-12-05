import numpy as np

input_file = "input.txt"

with open(input_file) as input:
    lines = []
    for line in input:
        line_list = list(line.strip())
        lines.append(line_list)

array = np.array(lines)

count = 0

for x, row in enumerate(array):
    if x == 0 or x == array.shape[0]-1:
        continue
    for y, letter in enumerate(row):
        if y == 0 or y == array.shape[1]-1:
            continue
        if letter == "A":
            corners = [array[x-1,y-1], array[x+1,y-1], array[x-1,y+1], array[x+1, y+1]]
            if corners.count('S') == 2 and corners.count('M') == 2 and corners[0] != corners[-1]:
                count += 1

print(count)
