#!/usr/bin/env python

from collections import defaultdict

with open('input') as f:
    input = f.read()


def coords_to_key(coords):
    return tuple(map(int, coords.split(',')))

cave = defaultdict(str)
lowest_rock = 0
for row in input.split('\n'):
    if not row:
        continue
    coords = row.split(' -> ')
    prev_coord = coords_to_key(coords[0])
    cave[prev_coord] = '#'
    lowest_rock = max(lowest_rock, prev_coord[1])
    for coord in coords[1:]:
        coord = coords_to_key(coord)
        if prev_coord[0] == coord[0]:
            for y in range(min(prev_coord[1], coord[1]), max(prev_coord[1], coord[1])):
                cave[(prev_coord[0], y)] = '#'
        else:
            for x in range(min(prev_coord[0], coord[0]), max(prev_coord[0], coord[0])):
                cave[(x, prev_coord[1])] = '#'
        cave[coord] = '#'
        lowest_rock = max(lowest_rock, coord[1])
        prev_coord = coord


def get_cave_item(position, has_floor):
    if has_floor and position[1] == lowest_rock + 2:
        return '#'
    return cave[position]


def drop_sand(position, has_floor):
    if not has_floor and position[1] + 1 > lowest_rock:
        return False
    if get_cave_item(position, has_floor):
        return False
    if not get_cave_item((position[0], position[1] + 1), has_floor):
        return drop_sand((position[0], position[1] + 1), has_floor)
    if not get_cave_item((position[0] - 1, position[1] + 1), has_floor):
        return drop_sand((position[0] - 1, position[1] + 1), has_floor)
    if not get_cave_item((position[0] + 1, position[1] + 1), has_floor):
        return drop_sand((position[0] + 1, position[1] + 1), has_floor)
    cave[position] = 'o'
    return True


cave_copy = cave.copy()
sand_units = 0
while drop_sand((500, 0), False):
    sand_units += 1
print(sand_units)

cave = cave_copy
sand_units = 0
while drop_sand((500, 0), True):
    sand_units += 1
print(sand_units)

