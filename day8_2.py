import copy

with open("day8.txt") as f:
    data = f.readlines()



def nop(num):
    global line_num
    line_num += 1
    
def jmp(num):
    global line_num
    line_num += num

def acc(num):
    global total
    global line_num
    total += num
    line_num += 1

cmds = {'nop':nop,
        'jmp':jmp,
        'acc':acc}

line_num = 0
total = 0
visited = {}
data1 = copy.copy(data)
change = 0

while True:
    if line_num == len(data):
        break

    while True:
        line = data[change]
        cmd = line.split()[0]
        num = line.split()[1]
        if cmd == 'jmp':
            data1[change] = 'nop ' + num 
            print ("trying jmp to nop", change)
            change += 1 
            break
        if cmd == 'nop':
            print ("trying nop to jmp", change)
            data1[change] = 'jmp ' + num
            change += 1 
            break
        change += 1


    while True:
        if line_num == len(data):
            break
        if line_num in visited:
            visited = {}
            total = 0
            line_num = 0
            data1 = copy.copy(data)
            break

        visited[line_num] = 1

        line = data1[line_num]
        parts = line.split()
        cmd = parts[0]
        num = int(parts[1])

        cmds[cmd](num)

print(total)