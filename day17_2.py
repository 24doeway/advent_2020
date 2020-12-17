


class Part1:
    def __init__(self):
        with open("day17.txt") as f:
            self.data =  [i.strip() for i in f.readlines()]
        self.grid = [[self.data]]

    def is_active(self, x, y, z, w):
        len_x = len(self.grid)
        len_y = len(self.grid[0])
        len_z = len(self.grid[0][0])
        len_w = len(self.grid[0][0][0])
        if x < 0 or x > len_x-1:
        	#print ('x range', x)
        	return 0
        if y < 0 or y > len_y-1:
            #print ('y range', y)
            return 0
        if z < 0 or z > len_z-1:
        	#print ('z range', z)
        	return 0
        if w < 0 or w > len_w-1:
        	#print ('z range', z)
        	return 0
        if self.grid[x][y][z][w] == "#":
        	return 1
        return 0

    def total(self):

        count = 0
        for x1 in self.grid:
            for y1 in x1:
                for z1 in y1:
                    count += z1.count('#')
        return count    	

    def count_81(self, x,y,z, w):
        count = 0
        for x1 in range(x-1, x+2):
            for y1 in range(y-1, y+2):
                for z1 in range(z-1, z+2):
                    for w1 in range(w-1, w+2):
                    #print(x1,y1,z1, self.is_active(x1,y1,z1))
                        count += self.is_active(x1,y1,z1,w1)
        return count

    def count_grid(self):
        len_x = len(self.grid)
        len_y = len(self.grid[0])
        len_z = len(self.grid[0][0])
        len_w = len(self.grid[0][0][0])
        count = []
        for x in range(-1,len_x+1):
            count_square = []
            for y in range(-1,len_y+1):
                count_line = []
                for z in range(-1,len_z+1):
                    count_space = []
                    for w in range(-1,len_w+1):
                        count_space.append(self.count_81(x,y,z,w))
                    count_line.append(count_space)
                count_square.append(count_line)
            count.append(count_square)
        return count

    def change(self):
        count = self.count_grid()
        # print (count)
        new_grid = []
        for x, square in enumerate(count):
            new_square = []
            for y, line in enumerate(square):
                new_line = []
                for z, space in enumerate(line):
                    new_space = ''
                    for w, c in enumerate(space):
                        if c == 3 or (c == 4 and self.is_active(x-1,y-1,z-1,w-1)):
                            new_space += '#'
                        else:
                            new_space += '.'
                    new_line.append(new_space)
                new_square.append(new_line)
            new_grid.append(new_square)
        self.grid = new_grid
        print(self.grid)
        return self.grid

    def run(self):
    	print(self.grid, self.total())
    	print(self.count_grid())
 
    	for i in range(6):
        	print (self.change(), self.total())






p = Part1()
p.run()
