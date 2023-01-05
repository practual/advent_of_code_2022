#!/usr/bin/env python

import math

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


def test_valve_permutations(rate, steps, room, valves_done):
    global max_rate
    remaining_valves = valve_rooms - valves_done
    for valve in remaining_valves:
        distance = get_distance(room, valve)
        steps_to_turn_on = steps + distance + 1
        if steps_to_turn_on > 30:
            continue
        new_rate = rate + rates[valve] * (30 - steps_to_turn_on)
        max_rate = max(max_rate, new_rate)
        valves_copy = valves_done.copy()
        valves_copy.add(valve)
        test_valve_permutations(new_rate, steps_to_turn_on, valve, valves_copy)


test_valve_permutations(0, 0, 'AA', set())
print(max_rate)

