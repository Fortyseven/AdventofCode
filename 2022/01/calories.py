elves = []

# making a list...
with open("input.txt") as f:
    # checking it...
    cals = 0
    for line in f.readlines():
        if line.strip().isnumeric():
            # more calories keeps santa plump...
            cals += int(line)
        else:
            # end-of-list, next elf...
            elves.append(cals)
            cals = 0

    # good to the last drop...
    if cals > 0:
        elves.append(cals)

# sprinkle the magic sauce...
elves.sort()

# and the winner is...
print(elves[-1])