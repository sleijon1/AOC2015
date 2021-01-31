from itertools import permutations
relation_hp = {}
people = set()
with open("input.txt") as INP:
    for line in INP:
        split = line.strip().split()
        person_1, sign, val, person_2 = \
            split[0], split[2], split[3], split[-1].strip('.')
        people.add(person_1)
        people.add(person_2)
        if sign == 'lose':
            relation_hp[(person_1, person_2)] = -int(val)
        else:
            relation_hp[(person_1, person_2)] = int(val)


def calc_hp(order: list):
    hp = 0
    min_hp = 1000
    for i in range(len(order)):
        right = i+1 if i < len(order)-1 else 0
        hp_1 = relation_hp[(order[i], order[right])]
        hp_2 = relation_hp[(order[i], order[i-1])]
        hp_3 = relation_hp[(order[i-1], order[i])]
        if hp_3 + hp_2 < min_hp:
            min_hp = hp_3 + hp_2
        hp += hp_1 + hp_2
    return hp, min_hp


max_hp = 0
max_order = None
min_hp = 1000
for perm in permutations(people):
    hp, temp_min = calc_hp(perm)
    if hp > max_hp:
        max_hp, max_order, min_hp = hp, perm, temp_min
print(f"Solution part 1: {max_hp}")
print(f"Solution part 2: {max_hp-min_hp}")
