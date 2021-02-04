from itertools import combinations

containers = []
fill_exactly = []
with open("input.txt") as INP:
    for size in INP.readlines():
        containers.append(int(size))

least_containers = None
combinations_least = 0
for i in range(len(containers)):
    for c in combinations(containers, i):
        if sum(c) == 150:
            if least_containers is None or least_containers == i:
                least_containers = i
                combinations_least += 1
            fill_exactly.append(c)
print(f"Solution part 1: {len(fill_exactly)}")
print(f"Solution part 2: {combinations_least}")
