current = list(map(int, list("1321131112")))
for _ in range(50):
    temp = []
    counter = 1
    for i in range(len(current)):
        try:
            if current[i] != current[i+1]:
                temp.append(counter)
                temp.append(current[i])
                counter = 1
            else:
                counter += 1
        except IndexError:
            temp.append(counter)
            temp.append(current[i])

    current = temp
print(f"Solution: {len(current)}")
