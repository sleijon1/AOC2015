import re
strings = open("input.txt").read().splitlines()
nice = []
for string in strings:
    if len(re.findall('[aeiou]', string)) >= 3\
       and re.search(r'(\w)\1', string)\
       and not re.search(r'(ab|cd|pq|xy)', string):
        nice.append(string)
print(f"Solution part 1: {len(nice)}")
nice2 = []
for string in strings:
    if not re.search(r'((\w){2}).*\1', string):
        continue
    if not re.search(r'(\w).{1}\1', string):
        continue
    nice2.append(string)
print(f"Solution part 2: {len(nice2)}")
