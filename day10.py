
with open("day10.txt") as f:
    data = [int(i) for i in f.readlines()]

data.sort()

print (len(data))

diffs = [data[i] - data[i-1] for i in range(1,len(data))]

print(diffs)

print ((1+diffs.count(1)) * (1+diffs.count(3)))

# for 3, 1, 3
# There is 1 way
# ie 4,5,8

# for 3, 1, 1, 3 
# there are 2 ways to connect them together
# i.e. 4,5,6   4, 6

# for 3, 1, 1, 3
# there are 4 ways
# i.e. 3,4,5,6  (none missed)  3,4,6 3,5,6 (1 missed)  3,6 (2 missed)   

# for 3, 1,1, 1,3
# there are 7
# i.e. 2,3,4,5,6 (none missed) 3 x 1 missed  3 x 2 / 2 = 3 missed

# for 3,1,1,1,1,3  (4)
# there are 11
# i.e. 1,2,3,4,5,6 (none) + 4 x 1 missed + (4 choose 2) (4*3)/2 = 6 missed

# Find blocks
diffs.append(3)
blocks = []
length = 1
for d in diffs:
    if d == 1:
        length += 1
    if d == 3:
        if length:
            blocks.append(length)
        length = 0

print (blocks)

mapping = {0:1, 1:1, 2:2, 3:4, 4:7, 5:11}
total = 1
for b in blocks:
    total = total * mapping[b]

print (total)
