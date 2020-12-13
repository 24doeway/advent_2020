import math

with open("day13.txt") as f:
    data = f.readlines()
    print (data[0])
    num = int(data[0])
    input = [int(i.strip()) for i in data[1].split(',') if i != 'x']

min_wait = 1000000

for x in input:
	wait = x - (num % x)
	if wait < min_wait:
		print (x, wait, x*wait)
		min_wait = wait


with open("day13.txt") as f:
	data = f.readlines()[1].split(',')

max_num = 0
constraints = []
for index in range(len(data)):
    num = data[index]
    if num != 'x':
        num = int(num)
        constraints.append([num, (num - index) % num])
        if num > max_num:
        	max_num = num
        	max_remainder = index

def check(num, constraints):
    for a, b in constraints:
        if not (num % a == b):
            return False
    return True


print (constraints)


step = 1
index = 1
num = constraints[-1][1]
for mod, remainder in reversed(constraints):
    print(num, mod, remainder, step)
    print(constraints[-index:])
    while True:

        if check(num, constraints[-index:]):
            print(num, mod)
            index += 1
            step = step * mod
            break
        else:
    	    num += step

