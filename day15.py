


class Part1:
    def __init__(self):
        #with open("day15.txt") as f:
        #    self.data =  f.readlines()
        self.input = [14,1,17,0,3,20]
        self.game = {}



    def run(self):
        for turn,num in enumerate(self.input):
        	self.game[num] = turn+1
        	self.last = num

        del self.game[num]
            
        for i in range(len(self.input)+1, 30000001):
            # print ("turn", i, self.last, self.game)
            if self.last in self.game:
            	age = i - self.game[self.last] - 1
            	self.game[self.last] = i -1
            	self.last = age
            else: 
            	# New number
            	self.game[self.last] = i -1
            	self.last = 0

            # print (i, self.last)




p = Part1()
p.run()
print (p.last)