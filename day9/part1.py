import pdb

input_file = "example.txt"

with open(input_file) as input:
    for line in input:
        file_map = line.strip()

is_file = True
index = 0
file_id = 0
files = {}
empty_space = []
file_space = []


for char in file_map:
    if is_file:
        file_pos = []
        file_start_pos = int(index)
        while index < file_start_pos + int(char):
            file_pos.append(index)
            index += 1
        file_space += file_pos
        files.update({file_id: file_pos})
        file_id += 1
        is_file = False
    else:
        empty_start_pos = int(index)
        while index < empty_start_pos + int(char):
            empty_space.append(index)
            index += 1
        is_file = True

file_id -= 1
while len(empty_space) > 0:
    for i in range(1,len(files[file_id])+1):
        try:
            print(files, empty_space)
            pdb.set_trace()
            files[file_id][-i] = empty_space.pop(0)
        except IndexError:
            break
    file_id -= 1

checksum = 0

for id, poss in files.items():
    for pos in poss:
        checksum += pos * id
        print(pos, id, checksum)
pdb.set_trace()
