#! /usr/bin/env python

monkeys = {}
operator_monkeys = set()
with open('input') as f:
    while line := f.readline():
        if not (line := line.strip()):
            continue
        monkey = line[:4]
        val = line[6:]
        try:
            val = int(val)
        except ValueError:
            left, operator, right = val.split()
            assert left not in operator_monkeys
            assert right not in operator_monkeys
            operator_monkeys.add(left)
            operator_monkeys.add(right)
        monkeys[monkey] = val

monkeys_copy = monkeys.copy()


class HumanException(Exception):
    pass


def resolve(monkey, allow_human):
    if monkey == 'humn' and not allow_human:
        raise HumanException
    if isinstance(monkeys[monkey], int):
        return monkeys[monkey]
    left, operator, right = monkeys[monkey].split()
    left_val = resolve(left, allow_human)
    right_val = resolve(right, allow_human)
    if operator == '+':
        output = left_val + right_val
    elif operator == '-':
        output = left_val - right_val
    elif operator == '*':
        output = left_val * right_val
    elif operator == '/':
        output = left_val // right_val
    else:
        raise Exception(f'unknown operator: {operator}')
    monkeys[monkey] = output
    return output


print(resolve('root', True))


def pass_to_human(monkey, val):
    if monkey == 'humn':
        return val
    left, operator, right = monkeys[monkey].split()
    try:
        left_val = resolve(left, False)
        if operator == '+':
            right_val = val - left_val
        elif operator == '-':
            right_val = left_val - val
        elif operator == '*':
            right_val = val // left_val
        elif operator == '/':
            right_val = left_val // val
        else:
            raise Exception(f'unknown operator {operator}')
        return pass_to_human(right, right_val)
    except HumanException:
        right_val = resolve(right, False)
        if operator == '+':
            left_val = val - right_val
        elif operator == '-':
            left_val = val + right_val
        elif operator == '*':
            left_val = val // right_val
        elif operator == '/':
            left_val = val * right_val
        else:
            raise Exception(f'unknown operator {operator}')
        return pass_to_human(left, left_val)


monkeys = monkeys_copy

left, _, right = monkeys['root'].split()

try:
    left_val = resolve(left, False)
    print(pass_to_human(right, left_val))
except HumanException:
    right_val = resolve(right, False)
    print(pass_to_human(left, right_val))
