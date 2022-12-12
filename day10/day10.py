#!/usr/bin/env python


with open('input') as f:
    input = f.read()


cycles = 0
register = 1
strength = 0
pixels = []

def increment_cycle():
    global cycles, pixels, register, strength
    if cycles % 40 in [register - 1, register, register + 1]:
        pixels.append('#')
    else:
        pixels.append('.')
    cycles += 1
    if cycles in [20, 60, 100, 140, 180, 220]:
        strength += cycles * register


for instruction in input.split('\n'):
    if not instruction:
        continue
    increment_cycle()
    if instruction != 'noop':
        increment_cycle()
        operator, operand = instruction.split()
        register += int(operand)

print(strength)
for i in range(0, len(pixels), 40):
    print(''.join(pixels[i:i+40]))
