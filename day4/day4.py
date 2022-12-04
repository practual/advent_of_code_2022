#!/usr/bin/env python


with open('input') as f:
    input = f.read()


full_overlaps = 0
partial_overlaps = 0
for pairs in input.split('\n'):
    if not pairs:
        continue
    range_1, range_2 = pairs.split(',')
    range_1_min, range_1_max = map(int, range_1.split('-'))
    range_2_min, range_2_max = map(int, range_2.split('-'))
    if range_1_min <= range_2_min and range_1_max >= range_2_max:
        full_overlaps += 1
    elif range_2_min <= range_1_min and range_2_max >= range_1_max:
        full_overlaps += 1
    if range_1_min <= range_2_min and range_1_max >= range_2_min:
        partial_overlaps += 1
    elif range_2_min <= range_1_min and range_2_max >= range_1_min:
        partial_overlaps += 1

print(full_overlaps)
print(partial_overlaps)

