line_num = 0
total = 0
visited = {}

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

while True:
    if line_num in visited:
        break

    visited[line_num] = 1

    line = data[line_num]
    parts = line.split()
    cmd = parts[0]
    num = int(parts[1])

    cmds[cmd](num)
    print (cmd, num, total)

print(total)