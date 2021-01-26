directions = open("input.txt").read().strip()
dir_dict = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
s_x, s_y = r_x, r_y = 0, 0
(houses := set()).add((0, 0))
for i, d in enumerate(directions):
    dx, dy = dir_dict[d]
    if i % 2 == 0:
        s_x, s_y = s_x+dx, s_y+dy
        x, y = s_x, s_y
    else:
        r_x, r_y = r_x+dx, r_y+dy
        x, y = r_x, r_y
    houses.add((x, y))
print(f"Solution part 2: {len(houses)}")
