
import numpy as np

with open('day02/input.txt','r') as f:
    data = f.read().splitlines()

def safe_check(level):
    diff = np.diff(level)
    only_increasing = np.all(diff>0)
    only_decreasing = np.all(diff<0)
    within_tolerance = np.all( (np.abs(diff) >=1) & (np.abs(diff) <= 3))
    return (only_increasing or only_decreasing) and within_tolerance

levels = [list(map(int, x.split())) for x in data]

# Part 1
total_safe = sum(safe_check(l) for l in levels)
print(total_safe)

# Part 2
total_safe = 0
for level in levels:
    if safe_check(level):
        total_safe += 1
    else:
        for i in range(len(level)):
            new_level = level[:i] + level[i+1:]
            if safe_check(new_level):
                total_safe += 1
                break
print(total_safe)


