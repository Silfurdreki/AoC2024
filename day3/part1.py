import re
import pdb

input_file = "input.txt"

with open(input_file) as input:
    lines = []
    for line in input:
        lines.append(line)

pattern_instruct = "mul\([0-9]+,[0-9]+\)"
pattern_digits = "[0-9]+"

all_instructions = []

for line in lines:
    instructions = re.findall(pattern_instruct, line)
    all_instructions = all_instructions + instructions


products = []
numbers = []

for instruction in all_instructions:
    digits = re.findall(pattern_digits, instruction)
    digits = [int(x) for x in digits]
    numbers.append(digits)
    product = digits[0] * digits[1]
    products.append(product)

answer = sum(products)

print(f"Final sum: {answer}")
