instructions = open("input.txt").read()
print("Solution part 1:", instructions.count('(')-instructions.count(')'))
position = 0
for i, stair in enumerate(instructions):
    if stair == '(':
        position += 1
    else:
        position -= 1
    if position < 0:
        print("Solution part 2: {}".format(i+1))
        exit(0)
