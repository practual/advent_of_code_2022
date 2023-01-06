#!/usr/bin/env python

import math
from itertools import permutations

with open('input') as f:
    input = f.read()


connections = {}
rates = {}
for row in input.split('\n'):
    if not row:
        continue
    row_parts = row.split()
    room = row_parts[1]
    rates[room] = int(row_parts[4].split('=')[1].strip(';'))
    connections[room] = [r.strip(',') for r in row_parts[9:]]

valve_rooms = {r for r in rates if rates[r]}



def get_distance_to_neighbours(a, b, distance, visited):
    shortest = math.inf
    visited.add(a)
    for neighbour in connections[a]:
        if neighbour == b:
            return distance + 1
        if neighbour not in visited:
            shortest = min(shortest, get_distance_to_neighbours(neighbour, b, distance + 1, visited.copy()))
    return shortest


shortest_distances = {}


def get_distance(a, b):
    try:
        return shortest_distances[(a, b)]
    except KeyError:
        pass
    try:
        return shortest_distances[(b, a)]
    except KeyError:
        pass
    shortest_distances[(a, b)] = get_distance_to_neighbours(a, b, 0, set())
    return shortest_distances[(a, b)] 


max_rate = 0


def get_contribution_to_rate(current_room, valve_room, current_steps, steps):
    distance = get_distance(current_room, valve_room)
    steps_to_turn_on = current_steps + distance + 1
    return rates[valve_room] * (steps - steps_to_turn_on), steps_to_turn_on


def test_valve_permutations(rate, explorers, valves_done, max_steps):
    global max_rate
    remaining_valves = valve_rooms - valves_done
    num_explorers = len(explorers)
    for valves in permutations(remaining_valves, num_explorers):
        next_explorers = []
        new_rate = rate
        valves_copy = valves_done.copy()
        for i, explorer in enumerate(explorers):
            steps, room = explorer
            valve = valves[i]
            rate_addition, new_steps = get_contribution_to_rate(room, valve, steps, max_steps)
            if new_steps <= max_steps:
                new_rate += rate_addition
                if new_rate > max_rate:
                    max_rate = new_rate
                    print('new max rate', new_rate)
                valves_copy.add(valve)
                # Will need at least two more steps to do anything useful (move and turn on valve)
                if new_steps <= max_steps - 2:
                    next_explorers.append([new_steps, valve])
        if next_explorers:
            test_valve_permutations(new_rate, next_explorers, valves_copy, max_steps)


test_valve_permutations(0, [[0, 'AA']], set(), 30)
print(max_rate)

max_rate = 0
test_valve_permutations(0, [[0, 'AA'], [0, 'AA']], set(), 26)
print(max_rate)

