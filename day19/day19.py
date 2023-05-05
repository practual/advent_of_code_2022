#! /usr/bin/env python

with open('input') as f:
    blueprints = f.read().split('\n')


def mine(state):
    state['ore'] += state['r_ore']
    state['clay'] += state['r_clay']
    state['obs'] += state['r_obs']
    state['geo'] += state['r_geo']


def evolve_state(max_time, state, blueprint, target_robot=None):
    minute = state['minute']
    if minute == max_time:
        return state['geo']
    max_rate_ore = max(blueprint['c_clay'], blueprint['c_obs_ore'], blueprint['c_geo_ore'])
    max_rate_clay = blueprint['c_obs_clay']
    max_rate_obs = blueprint['c_geo_obs']
    best_output = state['geo']
    if target_robot:
        if target_robot == 'r_geo':
            if state['ore'] >= blueprint['c_geo_ore'] and state['obs'] >= blueprint['c_geo_obs']:
                new_state = state.copy()
                mine(new_state)
                new_state['ore'] -= blueprint['c_geo_ore']
                new_state['obs'] -= blueprint['c_geo_obs']
                new_state['r_geo'] += 1
                new_state['minute'] += 1
                best_output = max(best_output, evolve_state(max_time, new_state, blueprint))
            else:
                new_state = state.copy()
                mine(new_state)
                new_state['minute'] += 1
                best_output = max(best_output, evolve_state(max_time, new_state, blueprint, target_robot))
        elif target_robot == 'r_obs':
            if state['ore'] >= blueprint['c_obs_ore'] and state['clay'] >= blueprint['c_obs_clay']:
                new_state = state.copy()
                mine(new_state)
                new_state['ore'] -= blueprint['c_obs_ore']
                new_state['clay'] -= blueprint['c_obs_clay']
                new_state['r_obs'] += 1
                new_state['minute'] += 1
                best_output = max(best_output, evolve_state(max_time, new_state, blueprint))
            else:
                new_state = state.copy()
                mine(new_state)
                new_state['minute'] += 1
                best_output = max(best_output, evolve_state(max_time, new_state, blueprint, target_robot))
        elif target_robot == 'r_clay':
            if state['ore'] >= blueprint['c_clay']:
                new_state = state.copy()
                mine(new_state)
                new_state['ore'] -= blueprint['c_clay']
                new_state['r_clay'] += 1
                new_state['minute'] += 1
                best_output = max(best_output, evolve_state(max_time, new_state, blueprint))
            else:
                new_state = state.copy()
                mine(new_state)
                new_state['minute'] += 1
                best_output = max(best_output, evolve_state(max_time, new_state, blueprint, target_robot))
        else:
            if state['ore'] >= blueprint['c_ore'] and state['r_ore'] < max_rate_ore:
                new_state = state.copy()
                mine(new_state)
                new_state['ore'] -= blueprint['c_ore']
                new_state['r_ore'] += 1
                new_state['minute'] += 1
                best_output = max(best_output, evolve_state(max_time, new_state, blueprint))
            else:
                new_state = state.copy()
                mine(new_state)
                new_state['minute'] += 1
                best_output = max(best_output, evolve_state(max_time, new_state, blueprint, target_robot))
    else:
        time_left = max_time - 1 - state['minute']
        if (state['ore'] + state['r_ore'] * time_left >= blueprint['c_geo_ore']
                and state['obs'] + state['r_obs'] * time_left >= blueprint['c_geo_obs']):
            new_state = state.copy()
            best_output = max(best_output, evolve_state(max_time, new_state, blueprint, 'r_geo'))
        if (state['ore'] + state['r_ore'] * time_left >= blueprint['c_obs_ore']
                and state['clay'] + state['r_clay'] * time_left >= blueprint['c_obs_clay']
                and state['r_obs'] < max_rate_obs):
            new_state = state.copy()
            best_output = max(best_output, evolve_state(max_time, new_state, blueprint, 'r_obs'))
        if (state['ore'] + state['r_ore'] * time_left >= blueprint['c_clay']
                and state['r_clay'] < max_rate_clay):
            new_state = state.copy()
            best_output = max(best_output, evolve_state(max_time, new_state, blueprint, 'r_clay'))
        if (state['ore'] + state['r_ore'] * time_left >= blueprint['c_ore']
                and state['r_ore'] < max_rate_ore):
            new_state = state.copy()
            best_output = max(best_output, evolve_state(max_time, new_state, blueprint, 'r_ore'))

    return best_output


quality_level = 0
first_blueprints = []
for i, blueprint_str in enumerate(blueprints):
    if not blueprint_str:
        continue
    state = {
        'minute': 0,
        'r_ore': 1,
        'ore': 0,
        'r_clay': 0,
        'clay': 0,
        'r_obs': 0,
        'obs': 0,
        'r_geo': 0,
        'geo': 0,
    }
    blueprint_tokens = blueprint_str.split()
    blueprint = {
        'c_ore': int(blueprint_tokens[6]),
        'c_clay': int(blueprint_tokens[12]),
        'c_obs_ore': int(blueprint_tokens[18]),
        'c_obs_clay': int(blueprint_tokens[21]),
        'c_geo_ore': int(blueprint_tokens[27]),
        'c_geo_obs': int(blueprint_tokens[30]),
    }
    if i < 3:
        first_blueprints.append(blueprint)
    geodes = evolve_state(24, state, blueprint)
    print(f'Can make {geodes} geodes with blueprint {i + 1} in 24 minutes')
    quality_level += (i + 1) * geodes

print(quality_level)

quality_level = 1
for i in range(3):
    state = {
        'minute': 0,
        'r_ore': 1,
        'ore': 0,
        'r_clay': 0,
        'clay': 0,
        'r_obs': 0,
        'obs': 0,
        'r_geo': 0,
        'geo': 0,
    }
    geodes = evolve_state(32, state, first_blueprints[i])
    print(f'Can make {geodes} geodes with blueprint {i + 1} in 32 minutes')
    quality_level *= geodes

print(quality_level)
