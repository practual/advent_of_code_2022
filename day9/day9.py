#!/usr/bin/env python


with open('input') as f:
    input = f.read()


def update_head(head, direction):
    if direction == 'U':
        return (head[0], head[1] - 1)
    if direction == 'D':
        return (head[0], head[1] + 1)
    if direction == 'L':
        return (head[0] - 1, head[1])
    if direction == 'R':
        return (head[0] + 1, head[1])
    raise Exception('Unknown direction {}'.format(direction))


def update_tail(tail, head):
    x, y = 0, 0
    distance = abs(tail[0] - head[0]) + abs(tail[1] - head[1])
    if distance == 2 and (tail[0] == head[0] or tail[1] == head[1]):
        if tail[0] == head[0]:
            y = 2 * int(tail[1] < head[1]) - 1
        else:
            x = 2 * int(tail[0] < head[0]) - 1
    elif distance >= 3:
        y = 2 * int(tail[1] < head[1]) - 1
        x = 2 * int(tail[0] < head[0]) - 1
    return (tail[0] + x, tail[1] + y)
    

head = (0, 0)
tail = (0, 0)
tail_stops = {tail}
for instruction in input.split('\n'):
    if not instruction:
        continue
    direction, distance = instruction.split()
    for step in range(int(distance)):
        head = update_head(head, direction)
        tail = update_tail(tail, head)
        tail_stops.add(tail)

print(len(tail_stops))


knots = {i: (0, 0) for i in range(10)}
tail_stops = {knots[9]}
for instruction in input.split('\n'):
    if not instruction:
        continue
    direction, distance = instruction.split()
    for step in range(int(distance)):
        knots[0] = update_head(knots[0], direction)
        for i in range(1, 10):
            knots[i] = update_tail(knots[i], knots[i - 1])
        tail_stops.add(knots[9])

print(len(tail_stops))

