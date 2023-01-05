#!/usr/bin/env python

import math
import sys

with open('input') as f:
    input = f.read()


height_map = {}
start = None
end = None
foothills = []
for row_num, row in enumerate(input.split('\n')):
    if not row:
        continue
    for col_num, col in enumerate(row):
        if col == 'S':
            start = (row_num, col_num)
            height = 1
        elif col == 'E':
            end = (row_num, col_num)
            height = 26
        else:
            height = ord(col) - 96
        height_map[(row_num, col_num)] = height
        if height == 1:
            foothills.append((row_num, col_num))

distance_map = {end: 0}
offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def update_distances_for_neighbours(position):
    height = height_map[position]
    distance = distance_map[position] + 1
    for offset in offsets:
        neighbour = (position[0] + offset[0], position[1] + offset[1])
        neighbour_height = height_map.get(neighbour)
        if not neighbour_height:
            continue
        if height - neighbour_height > 1:
            continue
        current_distance = distance_map.get(neighbour, math.inf)
        if distance < current_distance:
            distance_map[neighbour] = distance
            update_distances_for_neighbours(neighbour)

sys.setrecursionlimit(2000)
update_distances_for_neighbours(end)
print(distance_map[start])

fastest_route = math.inf
for foothill in foothills:
    fastest_route = min(fastest_route, distance_map.get(foothill, math.inf))
print(fastest_route)
 
