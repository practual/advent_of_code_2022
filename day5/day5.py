#!/usr/bin/env python


with open('input') as f:
    structure = []
    finished_structure = False
    instructions = []
    while line := f.readline():
        if line == '\n' and not finished_structure:
            finished_structure = True
        elif not finished_structure:
            structure.append(line)
        elif line != '\n':
            instructions.append(line)

num_stacks = int(structure[-1].strip().split(' ')[-1])
stacks = list([] for i in range(num_stacks))

for row in structure[-2::-1]:
    for i in range(0, len(row), 4):
        crate = row[i+1]
        if crate == ' ':
            continue
        stacks[i // 4].append(crate)

stacks_copy = list(stack.copy() for stack in stacks)

for instruction in instructions:
    _, num, _, start, _, end = instruction.strip().split()
    num, start, end = map(int, [num, start, end])
    # CrateMover 9000 method
    for i in range(num):
        crate = stacks[start - 1].pop()
        stacks[end - 1].append(crate)
    # CrateMover 9001 method
    crates_to_move = stacks_copy[start - 1][-num:]
    del stacks_copy[start - 1][-num:]
    stacks_copy[end - 1] += crates_to_move

print(''.join(stack.pop() for stack in stacks))
print(''.join(stack.pop() for stack in stacks_copy))

