#! /usr/bin/env python

import math
import sys

sys.setrecursionlimit(1500)

with open('input') as f:
    all_coords = f.read().split()

x_range = (math.inf, -math.inf)
y_range = (math.inf, -math.inf)
z_range = (math.inf, -math.inf)

cube_coords = set(tuple(map(int, coords.split(','))) for coords in all_coords)

total_faces = 0

for cube in cube_coords:
    x, y, z = cube
    x_range = (min(x_range[0], x), max(x_range[1], x))
    y_range = (min(y_range[0], y), max(y_range[1], y))
    z_range = (min(z_range[0], z), max(z_range[1], z))
    if (x - 1, y, z) not in cube_coords:
        total_faces += 1
    if (x + 1, y, z) not in cube_coords:
        total_faces += 1
    if (x, y - 1, z) not in cube_coords:
        total_faces += 1
    if (x, y + 1, z) not in cube_coords:
        total_faces += 1
    if (x, y, z - 1) not in cube_coords:
        total_faces += 1
    if (x, y, z + 1) not in cube_coords:
        total_faces += 1

print(total_faces)


def translate_cube(cube, face):
    face_axis = face[0]
    face_direction = face[1]
    mutated = list(cube)
    mutated[face_axis] += face_direction
    return tuple(mutated)


def get_face_rotations(cube, face, rotation_axis, direction):
    face_axis = face[0]
    face_direction = face[1]
    cube = translate_cube(cube, face)
    face = (rotation_axis, direction)
    yield [cube, face]
    cube = translate_cube(cube, face)
    face = (rotation_axis, -direction)
    yield [cube, face]
    face = (face_axis, -face_direction)
    yield [cube, face]
    cube = translate_cube(cube, face)
    face = (face_axis, face_direction)
    yield [cube, face]
    face = (rotation_axis, -direction)
    yield [cube, face]
    cube = translate_cube(cube, face)
    face = (rotation_axis, direction)
    yield [cube, face]


def find_neighbours(cube, face):
    face_sig = (*cube, *face)
    if face_sig in visited_faces:
        return
    visited_faces.add(face_sig)
    for rotation_axis in range(3):
        if rotation_axis == face[0]:
            continue
        for direction in (1, -1):
            rotations = get_face_rotations(cube, face, rotation_axis, direction)
            while True:
                neighbour_cube, neighbour_face = next(rotations)
                if neighbour_cube in cube_coords:
                    break
            find_neighbours(neighbour_cube, neighbour_face)


outer_cube = None
for cube in cube_coords:
    if cube[0] == x_range[1]:
        outer_cube = cube
        break

visited_faces = set()

find_neighbours(outer_cube, (0, 1))

print(len(visited_faces))
