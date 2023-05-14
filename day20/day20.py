#! /usr/bin/env python

values = {}
with open('input') as f:
    for i, raw_value in enumerate(f.read().split('\n')):
        value = raw_value.strip()
        if not value:
            continue
        values[i] = [i - 1, int(value), i + 1]

queue_size = len(values)
values[0][0] = queue_size - 1
values[queue_size - 1][2] = 0

values2 = {i: data.copy() for i, data in values.items()}

for i in range(queue_size):
    left, jump, right = values[i]
    if not jump:
        zero_ptr = i
        continue
    values[left][2] = right
    values[right][0] = left
    if jump > 0:
        jump %= (queue_size - 1)
        prev = left
        for j in range(jump):
            prev = values[prev][2]
        values[i][0] = prev
        values[i][2] = values[prev][2]
        values[values[prev][2]][0] = i
        values[prev][2] = i
    else:
        jump = abs(jump) % (queue_size - 1)
        nex = right
        for j in range(jump):
            nex = values[nex][0]
        values[i][2] = nex
        values[i][0] = values[nex][0]
        values[values[nex][0]][2] = i
        values[nex][0] = i

coords = 0
ptr = zero_ptr
for i in range(3):
    for j in range(1000):
        ptr = values[ptr][2]
    coords += values[ptr][1]

print(coords)

values = values2

for i in range(queue_size * 10):
    t = i % queue_size
    left, jump, right = values[t]
    if not jump:
        continue
    jump *= 811589153
    values[left][2] = right
    values[right][0] = left
    if jump > 0:
        jump %= (queue_size - 1)
        prev = left
        for j in range(jump):
            prev = values[prev][2]
        values[t][0] = prev
        values[t][2] = values[prev][2]
        values[values[prev][2]][0] = t
        values[prev][2] = t
    else:
        jump = abs(jump) % (queue_size - 1)
        nex = right
        for j in range(jump):
            nex = values[nex][0]
        values[t][2] = nex
        values[t][0] = values[nex][0]
        values[values[nex][0]][2] = t
        values[nex][0] = t

coords = 0
ptr = zero_ptr
for i in range(3):
    for j in range(1000):
        ptr = values[ptr][2]
    coords += values[ptr][1] * 811589153

print(coords)
