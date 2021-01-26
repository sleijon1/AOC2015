grid = {(x, y): 'off' for x in range(1000) for y in range(1000)}
with open("input.txt") as INP:
    for instr in INP.read().splitlines():
        split = instr.split(' ')
        split = split if split[0] != 'toggle' else ['dummy'] + split
        start = list(map(int, split[2].split(',')))
        end = list(map(int, split[-1].split(',')))
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if grid[(x, y)] == 'on' and split[1] in ('toggle', 'off'):
                    grid[(x, y)] = 'off'
                elif grid[(x, y)] == 'off' and split[1] in ('toggle', 'on'):
                    grid[(x, y)] = 'on'
on = list(grid.values()).count('on')
print(f"Solution part 1: {on}")
