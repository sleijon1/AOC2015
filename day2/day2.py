presents = open("input.txt").read().splitlines()
sq_ft = ribbon = 0
for present in presents:
    l, w, h = map(int, present.split('x'))
    ribbon += 2*min((l+h), (l+w), (w+h)) + l*w*h
    sq_ft += 2*sum((sum_ := (l*w, w*h, h*l))) + min(sum_)
print(f"Solution part 1: {sq_ft}")
print(f"Solution part 2: {ribbon}")
