#!/usr/bin/env python


with open('input') as f:
    input = f.read()


def get_score_for_round(oppo, you):
    if oppo == you:
        return 3 + you + 1
    if (oppo_val + 1) % 3 == you:
        return 6 + you + 1
    return you + 1


part_1_score = 0
part_2_score = 0
for game_round in input.split('\n'):
    if not game_round:
        continue
    oppo, you = game_round.split(' ')
    oppo_val = ord(oppo) - 65  # ord('A') == 65
    you_val = ord(you) - 88  # ord('X') == 88
    part_1_score += get_score_for_round(oppo_val, you_val)
    part_2_score += get_score_for_round(oppo_val, (oppo_val + you_val - 1) % 3)


print(part_1_score, part_2_score)

