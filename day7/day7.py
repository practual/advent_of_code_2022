#!/usr/bin/env python


with open('input') as f:
    input = f.read()


cwd = ['root']
dir_sizes = {}
for line in input.split('\n'):
    if not line:
        continue
    components = line.split()
    if components[0] == '$' and components[1] == 'cd':
       cd = components[-1]
       if cd == '/':
           cwd = ['root']
       elif cd == '..':
           cwd = cwd[:-1]
       else:
           cwd.append(cd)
    elif components[0] != '$' and components[0] != 'dir':
        size = int(components[0])
        for i in range(len(cwd)):
            cwd_key = tuple(cwd[:i+1])
            if cwd_key not in dir_sizes:
                dir_sizes[cwd_key] = 0
            dir_sizes[cwd_key] += size


small_dir_size = 0
for size in dir_sizes.values():
    if size <= 100000:
        small_dir_size += size
print(small_dir_size)


free_space = 70000000 - dir_sizes[('root',)]
space_to_delete = 30000000 - free_space
candidates = []
for size in dir_sizes.values():
    if size >= space_to_delete:
        candidates.append(size)
print(sorted(candidates)[0])

