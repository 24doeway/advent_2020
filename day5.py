seats = []

with open("day5.txt") as f:
    for line in f.readlines():
        code = line.strip()
        m = 1
        seat_num = 0
        for c in code[::-1]:
            if c in "BR":
            	seat_num += m
            m = m*2
        seats.append(seat_num)

print (max(seats))

for i in range(1024):
	if i not in seats:
		print(i)