#!/usr/bin/env python


with open('input') as f:
    input = f.read()


items = {}
operations = {}
tests = {}
if_true = {}
if_false = {}
monkey = -1
for row in input.split('\n'):
    if not row:
        continue
    row = row.strip()
    if row[:6] == 'Monkey':
        monkey += 1
    elif row[:8] == 'Starting':
        items[monkey] = [int(item.strip()) for item in row.split(':')[1].strip().split(',')]
    elif row[:9] == 'Operation':
        operations[monkey] = row.split('=')[1].strip()
    elif row[:4] == 'Test':
        tests[monkey] = int(row.split()[-1])
    elif row[:7] == 'If true':
        if_true[monkey] = int(row.split()[-1])
    elif row[:8] == 'If false':
        if_false[monkey] = int(row.split()[-1])


def reduce_by_remainders(x):
    global tests
    N = 1
    for n in tests.values():
        N *= n
    b = 0
    for n in tests.values():
        a = x % n
        y = N // n
        z = pow(y, -1, n)
        b += a * y * z
    return b


inspects = {m: 0 for m in range(monkey + 1)}
items_copy = {m: items[m].copy() for m in items}
for round in range(20):
    for m in range(monkey + 1):
        for old in items[m]:
            new = eval(operations[m])
            new = new // 3
            inspects[m] += 1
            if new % tests[m]:
                items[if_false[m]].append(new)
            else:
                items[if_true[m]].append(new)
        items[m] = []

max_inspects = sorted(inspects.values())
print(max_inspects[-1] * max_inspects[-2])

inspects = {m: 0 for m in range(monkey + 1)}
items = items_copy
for round in range(10000):
    for m in range(monkey + 1):
        for old in items[m]:
            new = eval(operations[m])
            new = reduce_by_remainders(new)
            inspects[m] += 1
            if new % tests[m]:
                items[if_false[m]].append(new)
            else:
                items[if_true[m]].append(new)
        items[m] = []

max_inspects = sorted(inspects.values())
print(max_inspects[-1] * max_inspects[-2])

