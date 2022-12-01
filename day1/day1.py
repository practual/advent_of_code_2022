#!/usr/bin/env python


with open('input') as f:
    input = f.read()


calories_per_elf = []
elf_calories = 0
for line in input.split('\n'):
    if not line:
        calories_per_elf.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(line)

top_calories = sorted(calories_per_elf, reverse=True)

print(top_calories[0])
print(sum(top_calories[0:3]))

