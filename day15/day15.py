import math

attribute_list = []
with open("input.txt") as INP:
    for line in INP.readlines():
        name, attributes = line.split(":")
        attribute_list.append([int(attr[-2:]) for attr in attributes.split(',')])


def max_score(p1=True):
    max_total = 0
    for i in range(100):
        for j in range(100-i):
            for k in range(100-j):
                for l in range(100-k):
                    if sum([i, j, k, l]) != 100:
                        continue
                    no_ingr = 4 if p1 else 5
                    total = [i*attribute_list[0][x]+j*attribute_list[1][x] +
                             k*attribute_list[2][x]+l*attribute_list[3][x]
                             for x in range(no_ingr)]
                    if any([num < 0 for num in total]) or (not p1 and total[-1] != 500):
                        continue
                    product = 1
                    for num in total[0:4]:
                        product *= num
                    if product > max_total:
                        max_total = product
    return max_total
print(f"Solution part 1: {max_score()}")
print(f"Solution part 2: {max_score(False)}")
