


 

class Ship:

    def __init__(self):
        self.location = [0,0]
        self.direction_index = 0
        self.direction_list = ([1,0], [0,-1], [-1,0], [0,1])
        self.cmds = {
        'N':self.cmd_N,
'S':self.cmd_S,
'E':self.cmd_E,
'W':self.cmd_W,
'L':self.cmd_L,
'R':self.cmd_R,
'F':self.cmd_F,
        }

    def cmd_N(self, num):
        self.location[1] = self.location[1] + num

    def cmd_S(self, num):
        self.location[1] = self.location[1] - num
    
    def cmd_E(self, num):
        self.location[0] = self.location[0] + num

    def cmd_W(self, num):
        self.location[0] = self.location[0] - num

    def cmd_F(self, num):
        direction = self.direction_list[self.direction_index]
        self.location[0] = self.location[0] + direction[0] * num
        self.location[1] = self.location[1] + direction[1] * num

    def cmd_L(self, num):
        turn = int(num / 90)
        self.direction_index = (self.direction_index - turn) % 4

    def cmd_R(self, num):
        turn = int(num / 90)
        self.direction_index = (self.direction_index + turn) % 4

    def run(self, cmd, num):
        self.cmds[cmd](num)

class Ship2:

    def __init__(self):
        self.location = [0,0]
        self.waypoint = [10,1]
        self.cmds = {
        'N':self.cmd_N,
'S':self.cmd_S,
'E':self.cmd_E,
'W':self.cmd_W,
'L':self.cmd_L,
'R':self.cmd_R,
'F':self.cmd_F,
        }

    def cmd_N(self, num):
        self.waypoint[1] = self.waypoint[1] + num

    def cmd_S(self, num):
        self.waypoint[1] = self.waypoint[1] - num
    
    def cmd_E(self, num):
        self.waypoint[0] = self.waypoint[0] + num

    def cmd_W(self, num):
        self.waypoint[0] = self.waypoint[0] - num

    def cmd_F(self, num):
        self.location[0] = self.location[0] + self.waypoint[0] * num
        self.location[1] = self.location[1] + self.waypoint[1] * num

    def turn_R(self):
        tmp = self.waypoint[0]
        self.waypoint[0] = self.waypoint[1]
        self.waypoint[1] = -tmp

    def cmd_L(self, num):
        turn = int(num / 90)
        for i in range(3*turn):
            self.turn_R()

    def cmd_R(self, num):
        turn = int(num / 90)
        for i in range(turn):
            self.turn_R()

    def run(self, cmd, num):
        self.cmds[cmd](num)
        print (self.waypoint)
        print (self.location)

s = Ship2()

with open("day12.txt") as f:
    data = [a.strip() for a in f.readlines()]
for line in data:
    cmd = line[0]
    num = int(line[1:])
    s.run(cmd,num)

print (s.location)
print (sum([abs(i) for i in s.location]))