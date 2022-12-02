with open("input.txt") as f:
    floor = 0
    for i, ch in enumerate(f.read()):
        floor += 1 if ch == '(' else -1
        if floor < 0:
            print("First -1: ", i)
            break

print(floor)
