#!/usr/bin/env python


with open('input') as f:
    input = f.read()


start_of_package_marker, start_of_message_marker = 0, 0
for i in range(0, len(input) - 3):
    if not start_of_package_marker and len(set(input[i + j] for j in range(4))) == 4:
        start_of_package_marker = i + 4
    if not start_of_message_marker and len(set(input[i + j] for j in range(14))) == 14:
        start_of_message_marker = i + 14
    if start_of_package_marker and start_of_message_marker:
        break

print(start_of_package_marker)
print(start_of_message_marker)

