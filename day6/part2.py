import numpy as np
import pdb
import time

def next_coords(pos, dir):
    dirs = {0: [pos[0] - 1, pos[1]],
            1: [pos[0], pos[1] + 1],
            2: [pos[0] + 1, pos[1]],
            3: [pos[0], pos[1] - 1]}

    return dirs[dir % 4][0], dirs[dir % 4][1]

def draw_map(map):
    for row in map:
        line = ''
        for char in row:
            line = line + char
        print(line)

def step(map, pos, dir):
    dir_symbols = {0: '^',
                   1: '>',
                   2: 'v',
                   3: '<'}
    next_pos = next_coords(pos, dir)
    cur_row = pos[0]
    cur_col = pos[1]
    try:
        if next_pos.__contains__(-1):
            raise IndexError

        if map[next_pos] == '#' or map[next_pos] == 'O':
            dir += 1
            next_pos = next_coords(pos, dir)

    except IndexError:
        map[cur_row, cur_col] = trail
        return map, pos, dir, False

    map[cur_row, cur_col] = trail
    map[next_pos] = dir_symbols[dir % 4]
    pos = list(next_pos)

    return map, pos, dir, True

tic = time.time()

input_file = "input.txt"

map = []

with open(input_file) as input:
    for line in input:
        map.append(list(line.strip()))

map = np.array(map)
position = [int(x) for x in np.where(map == '^')]
start_position = list(position)
direction = 0
inside = True
loops = 0
steps = 0
obstacle_positions = []
global trail
trail = 'X'


while inside:

    loop_steps = 0
    next_position = next_coords(position, direction)
    mod_map = np.array(map)
    mod_position = list(position)
    mod_start_position = list(position)
    mod_direction = int(direction)
    mod_start_direction = int(direction)
    mod_inside = True
    trail = '$'
    try:
        if next_position.__contains__(-1):
            raise IndexError
        elif map[next_position] == '#':
            mod_inside = False
        mod_map[next_position] = 'O'
        obstacle_position = list(next_position)
        enc_obstacle = [[obstacle_position, list(position)]]
        if obstacle_position == start_position or obstacle_positions.__contains__(obstacle_position):
            mod_inside = False

    except IndexError:
        mod_inside = False

    while mod_inside:
        try:
            if next_position.__contains__(-1):
                raise IndexError
            elif mod_map[next_position] == '#' or mod_map[next_position] == 'O':
                enc_obstacle.append([list(next_position), mod_position])
        except IndexError:
            pass

        mod_map, mod_position, mod_direction, mod_inside = step(mod_map, mod_position, mod_direction)

        next_position = next_coords(mod_position, mod_direction)
        if enc_obstacle.__contains__([list(next_position), mod_position]):
            obstacle_positions.append(obstacle_position)
            loops += 1
            print(steps, loops, loop_steps)
            break
        loop_steps += 1

    trail = 'X'
    prev_dir = direction
    map, position, direction, inside = step(map, position, direction)
    steps += 1
#    draw_map(mod_map)
#    pdb.set_trace()

elapsed = time.time() - tic
print(f'{loops} different loops. Took {elapsed} seconds.')
pdb.set_trace()
