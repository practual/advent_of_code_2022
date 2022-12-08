#!/usr/bin/env python


with open('input') as f:
    input = f.read()


visible = set()
cols = None
for row_num, row in enumerate(input.split('\n')):
    if not row:
        continue
    max_tree = -1
    max_col = 0
    for col_num, tree in enumerate(row):
        if int(tree) > max_tree:
            visible.add((row_num, col_num))
            max_tree = int(tree)
        max_col = col_num
    if not cols:
        cols = list([] for i in range(max_col + 1))
    max_tree = -1
    for rev_col_num, tree in enumerate(reversed(row)):
        if int(tree) > max_tree:
            visible.add((row_num, max_col - rev_col_num))
            max_tree = int(tree)
        cols[max_col - rev_col_num].append(int(tree))

for col_num, col in enumerate(cols):
    max_tree = -1
    max_row = 0
    for row_num, tree in enumerate(col):
        if tree > max_tree:
            visible.add((row_num, col_num))
            max_tree = tree
        max_row = row_num
    max_tree = -1
    for rev_row_num, tree in enumerate(reversed(col)):
        if tree > max_tree:
            visible.add((max_row - rev_row_num, col_num))
            max_tree = tree

print(len(visible))


def get_visible_distance(height, x, y, direction):
    if x < 0 or y < 0:
        return 0
    try:
        if cols[x][y] >= height:
            return 1
    except IndexError:
        return 0
    if direction == 0:
        return 1 + get_visible_distance(height, x - 1, y, direction)
    if direction == 1:
        return 1 + get_visible_distance(height, x + 1, y, direction)
    if direction == 2:
        return 1 + get_visible_distance(height, x, y - 1, direction)
    if direction == 3:
        return 1 + get_visible_distance(height, x, y + 1, direction)
         

max_view = 0
for col_num, col in enumerate(cols):
    for row_num, tree in enumerate(col):
        view = 1
        view *= get_visible_distance(tree, col_num - 1, row_num, 0)
        view *= get_visible_distance(tree, col_num + 1, row_num, 1)
        view *= get_visible_distance(tree, col_num, row_num - 1, 2)
        view *= get_visible_distance(tree, col_num, row_num + 1, 3)
        max_view = max(max_view, view)

print(max_view)

