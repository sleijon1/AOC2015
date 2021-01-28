import re
import json

INP = open("input.txt").read()
part_1 = sum(map(int, re.findall(r'-?\d+', INP)))
print(f"Solution part 1: {part_1}")
#print(json.loads(INP)[0][1][0])
