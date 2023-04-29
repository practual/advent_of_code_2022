#!/usr/bin/env python


with open('input') as f:
    jets = f.readline().strip()

jet_len = len(jets)

rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]


class Rock:
    def __init__(self, ptr):
        self.ptr = ptr
        self.width = max(pebble[0] for pebble in self.pebbles) + 1

    @property
    def pebbles(self):
        return rocks[self.ptr]


class RockPile:
    def __init__(self, pile=None):
        self.pile = pile if pile else set()
        self.height = max(p[1] + 1 for p in self.pile) if self.pile else 0
        self.floors = {0: 0}

    def test_position(self, rock, rock_pos):
        if rock_pos[0] < 0:
            return False
        if rock_pos[0] > 7 - rock.width:
            return False
        if rock_pos[1] < 0:
            return False
        for pebble in rock.pebbles:
            if (pebble[0] + rock_pos[0], pebble[1] + rock_pos[1]) in self.pile:
                return False
        return True

    def add_to_pile(self, rock, rock_pos):
        for floor in self.floors:
            self.floors[floor] += 1
        y_vals_to_check = set()
        for pebble in rock.pebbles:
            x = pebble[0] + rock_pos[0]
            y = pebble[1] + rock_pos[1]
            self.pile.add((x, y))
            y_vals_to_check.add(y)
        self.height = max(self.height - 1, *y_vals_to_check) + 1
        floors = set()
        for y in y_vals_to_check:
            if all((x, y) in self.pile for x in range(7)):
                floors.add(y)
        if floors:
            floor = max(floors)
            self.floors[floor] = 0
            return floor
        return -1

    def pebbles_above_floor(self, floor):
        pebbles = set()
        for y in range(floor + 1, self.height):
            for x in range(7):
                if (x, y) in self.pile:
                    pebbles.add((x, y - floor - 1))
        return pebbles


def find_height_after_rocks(num_rocks):
    num_rocks_landed = 0
    pile_height_offset = 0
    rock_pile = RockPile()
    rock_ptr = 0
    rock = Rock(rock_ptr)
    rock_pos = (2, rock_pile.height + 3)
    jet_ptr = 0
    floor_params = {(frozenset(), 0, 0): 0}
    loop_identified = False
    while num_rocks_landed < num_rocks:
        rock_jet_pos = (rock_pos[0] + (1 if jets[jet_ptr] == '>' else -1), rock_pos[1])
        if rock_pile.test_position(rock, rock_jet_pos):
            rock_pos = rock_jet_pos
        rock_fall_pos = (rock_pos[0], rock_pos[1] - 1)
        if rock_pile.test_position(rock, rock_fall_pos):
            rock_pos = rock_fall_pos
        else:
            num_rocks_landed += 1
            floor = rock_pile.add_to_pile(rock, rock_pos)

            if not loop_identified and floor >= 0:
                new_floor_params = (frozenset(rock_pile.pebbles_above_floor(floor)), rock_ptr, jet_ptr)
                if new_floor_params in floor_params:
                    rocks_remaining = num_rocks - num_rocks_landed
                    old_floor = floor_params[new_floor_params]
                    rocks_in_loop = rock_pile.floors[old_floor]
                    loops_remaining = rocks_remaining // rocks_in_loop
                    num_rocks_landed += rock_pile.floors[old_floor] * loops_remaining
                    height_in_loop = floor - old_floor
                    pile_height_offset = floor + 1 + (floor - old_floor) * loops_remaining
                    loop_identified = True
                    rock_pile = RockPile(rock_pile.pebbles_above_floor(floor))
                floor_params[new_floor_params] = floor

            rock_ptr = (rock_ptr + 1) % 5
            rock = Rock(rock_ptr)
            rock_pos = (2, rock_pile.height + 3)
        jet_ptr = (jet_ptr + 1) % jet_len
    return pile_height_offset + rock_pile.height


print(find_height_after_rocks(2022))
print(find_height_after_rocks(1000000000000))
