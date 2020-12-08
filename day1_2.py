with open("day1.txt") as f:
    input = [int(i.strip()) for i in f.readlines()]

for i in input:
    for j in input:
        for k in input:
            if i + j + k == 2020:
                print(i, j, k, i * j * k)
