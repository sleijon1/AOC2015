sues = {}
real_sue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
            'akitas': 0, 'vizslas': 0, 'goldfish': 5,
            'trees': 3, 'cars': 2, 'perfumes': 1}
with open("input.txt") as INP:
    for line in INP.readlines():
        person = line.strip().split(', ')
        ID = person[0].split(' ')[1].strip(':')
        person[0] = person[0].split(': ')[1] + ': ' + \
            person[0].split(': ')[-1]
        pers_dict = {}
        for attr_count in person:
            name, count = attr_count.split(': ')
            pers_dict[name] = int(count)
        sues[ID] = (pers_dict)

for sue, sue_dict in sues.items():
    found_sue = True
    for attr, val in sue_dict.items():
        # part 2
        if attr in ('cats', 'trees'):
            if not val > real_sue[attr]:
                found_sue = False
                break
        # part 2
        elif attr in ('pomeranians', 'goldfish'):
            if not val < real_sue[attr]:
                found_sue = False
                break
        elif real_sue[attr] != val:
            found_sue = False
            break
    if found_sue:
        print(f"Solution part 2: {sue}")
