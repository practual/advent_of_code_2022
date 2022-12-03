#!/usr/bin/env python


with open('input') as f:
    input = f.read()


total_priority = 0
for rucksack in input.split('\n'):
    if not rucksack:
        continue
    compartment_one = set(rucksack[:len(rucksack) // 2])
    compartment_two = set(rucksack[len(rucksack) // 2:])
    priority = ord((compartment_one & compartment_two).pop()) - 96
    if priority < 0:
        priority += 58
    total_priority += priority

print(total_priority)


rucksacks = [rucksack for rucksack in input.split('\n') if rucksack]
total_priority = 0
for i in range(0, len(rucksacks), 3):
    priority = ord((set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])).pop()) - 96
    if priority < 0:
        priority += 58
    total_priority += priority

print(total_priority)

