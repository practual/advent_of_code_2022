#!/usr/bin/env python

from functools import cmp_to_key


with open('input') as f:
    input = f.read()


pairs = []
pair = []
all_packets = []
for row in input.split('\n'):
    if not row and pair:
        pairs.append(pair)
        pair = []
    elif row:
        packet = eval(row)
        all_packets.append(packet)
        pair.append(packet)


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        if a > b:
            return False
        return None
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    for x, y in zip(a, b):
        item_comparison = compare(x, y)
        if item_comparison is not None:
            return item_comparison
    if len(a) < len(b):
        return True
    if len(a) > len(b):
        return False
    return None


correct_pair_sum = 0
for i, pair in enumerate(pairs):
    if compare(*pair):
        correct_pair_sum += i + 1
print(correct_pair_sum)

divider_packets = [[[2]], [[6]]]
all_packets += divider_packets
sorted_packets = sorted(all_packets, key=cmp_to_key(lambda x, y: -1 if compare(x, y) else 1))
decoder_key = 1
for i, packet in enumerate(sorted_packets):
    if packet in divider_packets:
        decoder_key *= i + 1
print(decoder_key)

