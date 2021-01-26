grid = {(x, y): 0 for x in range(1000) for y in range(1000)}
bn_dict = {'on': 1, 'off': -1, 'toggle': 2}
with open("input.txt") as INP:
    for instr in INP.read().splitlines():
        split = instr.split(' ')
        split = split if split[0] != 'toggle' else ['dummy'] + split
        start = list(map(int, split[2].split(',')))
        end = list(map(int, split[-1].split(',')))
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid[(x, y)] += bn_dict[split[1]]
                grid[(x, y)] = grid[(x, y)] if grid[(x, y)] >= 0 else 0
brightness = sum(grid.values())
print(f"Solution part 2: {brightness}")
