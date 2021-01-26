from itertools import permutations

distances = {}
destinations = set()
with open("input.txt") as INP:
    for line in INP.readlines():
        start, dest = line.split(" to ")
        dest, dist = dest.split(" = ")
        key = tuple(sorted((start, dest)))
        distances[key] = int(dist)
        destinations.add(start)
        destinations.add(dest)

perms = permutations(destinations, len(destinations))
total_distances = {}
for perm in perms:
    total_distances[perm] = sum([distances[tuple(sorted((perm[i], perm[i+1])))]
                                 for i in range(len(perm)-1)])

print(f"Solution part 1: {min(total_distances.values())}")
print(f"Solution part 2: {max(total_distances.values())}")
