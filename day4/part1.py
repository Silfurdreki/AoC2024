import pdb
import numpy as np
import re

input_file = "input.txt"

with open(input_file) as input:
    lines = []
    for line in input:
        line_list = list(line.strip())
        lines.append(line_list)

array = np.array(lines)

count = 0

for row in array:
    row_str = ''.join(x for x in row)
    count += len(re.findall('XMAS', row_str))
    count += len(re.findall('XMAS', row_str[::-1]))
    print(count, row_str)

for row in array.T:
    row_str = ''.join(x for x in row)
    count += len(re.findall('XMAS', row_str))
    count += len(re.findall('XMAS', row_str[::-1]))
    print(count, row_str)

mirrors = [array, np.fliplr(array)]

for mirror in mirrors:
    diag_main = mirror.diagonal(0)
    diag_main_str = ''.join(x for x in diag_main)
    count += len(re.findall('XMAS', diag_main_str))
    count += len(re.findall('XMAS', diag_main_str[::-1]))

    diag_offset = 1
    diag_pos = [1,2,3,4,5]
    while len(diag_pos) > 4:
        diag_pos = mirror.diagonal(diag_offset)
        diag_neg = mirror.diagonal(-diag_offset)
        diag_pos_str = ''.join(x for x in diag_pos)
        diag_neg_str = ''.join(x for x in diag_neg)
        count += len(re.findall('XMAS', diag_pos_str))
        count += len(re.findall('XMAS', diag_neg_str))
        count += len(re.findall('XMAS', diag_pos_str[::-1]))
        count += len(re.findall('XMAS', diag_neg_str[::-1]))
        diag_offset += 1
        print(count, diag_pos_str, diag_neg_str)

print(count)
