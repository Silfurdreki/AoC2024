import re
import pdb

input_file = "input.txt"

with open(input_file) as input:
    lines = []
    for line in input:
        lines.append(line)

pattern_instruct = "(mul\([0-9]+,[0-9]+\))|(do\(\))|(don\'t\(\))"
pattern_digits = "[0-9]+"

all_instructions = []

for line in lines:
    matches = re.findall(pattern_instruct, line)
    instructions = []
    for match in matches:
        for group in match:
            if group:
                instructions.append(group)
    all_instructions = all_instructions + instructions

def read_instrucion(instruction):
    pattern_digits = "[0-9]+"

    if instruction == "don't()":
        return False
    elif instruction == "do()":
        return True
    else:
        digits = re.findall(pattern_digits, instruction)
        digits = [int(x) for x in digits]
        return digits

enabled = True
numbers = []
products = []

for instruction in all_instructions:
    result = read_instrucion(instruction)
    if isinstance(result, bool):
        enabled = result
    else:
        if enabled:
            product = result[0] * result[1]
            numbers.append(result)
            products.append(product)

answer = sum(products)

print(f"Final sum: {answer}")
