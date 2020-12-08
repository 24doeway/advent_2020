hit = 0

location = 0
right = 1
skip = False

with open("day3.txt") as f:
    for line in f.readlines():
        if skip:
            skip = False
            continue

        trees = line.strip()
        print(location, trees)
        if trees[location] == '#':
            hit += 1
        location += right
        location = location % len(trees)
        skip = True

print(hit)
