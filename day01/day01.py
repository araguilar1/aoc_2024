from collections import Counter

with open('day01/input.txt','r') as f:
    data = f.read().splitlines()


left  = sorted([int(x.split()[0]) for x in data])
right = sorted([int(x.split()[1]) for x in data])

# Part 1
total_dist = sum(abs(i-j) for i,j in zip(left,right))
print(total_dist)

# Part 2
counter = Counter(right)

sim_score = sum(num*counter[num] for num in left)

print(sim_score)