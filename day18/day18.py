import sys
from copy import deepcopy

sys.path.append('../../pyutils/geometry/')
from map import adjacent_tiles

ACTIVE = '#'
INACTIVE = '.'

grid = []
with open("input.txt") as INP:
    for line in INP.readlines():
        grid.append(list(line.strip()))

def evolve_grid(grid: list, ticks: int, part_two=False):
    if part_two:
        grid = deepcopy(grid)
        grid[0][0] = grid[0][-1] = grid[-1][0] = grid[-1][-1] = '#'
    for _ in range(ticks):
        temp = deepcopy(grid)
        for y, row in enumerate(grid):
            for x, el in enumerate(row):
                if part_two and ((x, y) in [(0, 0), (len(grid[0])-1, 0),
                                            (0, len(grid)-1),
                                            (len(grid[0])-1, len(grid)-1)]):
                    continue
                if el == ACTIVE:
                    if adjacent_tiles(grid, (x, y)).count('#') in (2, 3):
                        pass
                    else:
                        temp[y][x] = '.'
                elif el == INACTIVE:
                    if adjacent_tiles(grid, (x, y)).count('#') == 3:
                        temp[y][x] = '#'
        grid = temp
    return grid


p1_grid = evolve_grid(grid, 100)
on_count = sum([row.count('#') for row in p1_grid])
print(f"Solution part 1: {on_count}")
# part_2
p2_grid = evolve_grid(grid, 100, True)
on_count = sum([row.count('#') for row in p2_grid])
print(f"Solution part 2: {on_count}")
