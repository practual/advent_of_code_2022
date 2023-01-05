#!/usr/bin/env python

with open('input') as f:
    input = f.read()


def x_range_for_y(sensor, distance, y):
    distance_to_y = abs(sensor[1] - y)
    spare_distance = distance - distance_to_y
    if spare_distance < 0:
        return None
    return (sensor[0] - spare_distance, sensor[0] + spare_distance)


def collapse_ranges(ranges):
    collapsed_ranges = []
    current_range = None
    for r in sorted(ranges, key=lambda r: r[0]):
        if current_range and r[0] <= current_range[1] and r[1] >= current_range[0]:
            r = (
                min(r[0], current_range[0]),
                max(r[1], current_range[1])
            )
            collapsed_ranges = collapsed_ranges[:-1]
        collapsed_ranges.append(r)
        current_range = r
    return collapsed_ranges
    

line_y = 2000000
sensors_and_ranges = []
beacons_on_y = set()
for row in input.split('\n'):
    if not row:
        continue
    sensor_details = row.split(' ')
    sensor = (
        int(sensor_details[2].split('=')[1].strip(',')),
        int(sensor_details[3].split('=')[1].strip(':'))
    )
    beacon = (
        int(sensor_details[8].split('=')[1].strip(',')),
        int(sensor_details[9].split('=')[1])
    )
    if beacon[1] == line_y:
        beacons_on_y.add(beacon[0])
    distance_to_beacon = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
    sensors_and_ranges.append((sensor, distance_to_beacon))

x_ranges = []
for sensor, sensor_range in sensors_and_ranges:
    x_range = x_range_for_y(sensor, sensor_range, line_y)
    if not x_range:
        continue
    x_ranges.append(x_range) 
collapsed_ranges = collapse_ranges(x_ranges)
blocked_positions = -len(beacons_on_y)
for r in collapsed_ranges:
    blocked_positions += r[1] - r[0] + 1
print(blocked_positions)

for y in range(0, 4000001):
    if not y % 100000:
        print('Checked "y" coordinates to {}'.format(y))
    x_ranges = []
    for sensor, sensor_range in sensors_and_ranges:
        x_range = x_range_for_y(sensor, sensor_range, y)
        if not x_range:
            continue
        x_ranges.append(x_range)
    collapsed_ranges = collapse_ranges(x_ranges)
    beacon_at_x = -1
    for r in collapsed_ranges:
        if r[0] > 0:
            beacon_at_x = r[0] - 1
        if r[1] < 4000000:
            beacon_at_x = r[1] + 1
    if beacon_at_x > -1:
        print(beacon_at_x * 4000000 + y)
        break

