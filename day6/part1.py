import numpy as np
import pdb
import time

def draw_map(map):
    for row in map:
        line = ''
        for char in row:
            line = line + char
        print(line)

def step(map, pos, dir):
    dirs = {0: [pos[0] - 1, pos[1]],
            1: [pos[0], pos[1] + 1],
            2: [pos[0] + 1, pos[1]],
            3: [pos[0], pos[1] - 1]}
    dir_symbols = {0: '^',
                   1: '>',
                   2: 'v',
                   3: '<'}
    next_row = dirs[dir % 4][0]
    next_col = dirs[dir % 4][1]
    cur_row = pos[0]
    cur_col = pos[1]
    try:
        if next_row < 0 or next_col < 0:
            raise IndexError

        if map[next_row, next_col] == '#':
            dir += 1
            next_row = dirs[dir % 4][0]
            next_col = dirs[dir % 4][1]

    except IndexError:
        map[cur_row, cur_col] = 'X'
        return map, pos, dir, False

    map[cur_row, cur_col] = 'X'
    map[next_row, next_col] = dir_symbols[dir % 4]
    pos = [next_row, next_col]

    return map, pos, dir, True

input_file = "input.txt"

map = []

with open(input_file) as input:
    for line in input:
        map.append(list(line.strip()))

map = np.array(map)
position = [int(x) for x in np.where(map == '^')]
direction = 0
inside = True

while inside:
    prev_dir = direction
    map, position, direction, inside = step(map, position, direction)

draw_map(map)
visited = len(np.where(map == 'X')[0])
print(f'Visited {visited} distinct locations.')
