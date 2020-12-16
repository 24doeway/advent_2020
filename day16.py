


class Part1:
    def __init__(self):
        with open("day16.txt") as f:
            self.data =  [i.strip() for i in f.readlines()]
        self.constraints = {}
        self.valid = {}
        for line in self.data:
            if "your ticket" in line:
                break
            parts = line.split(':')
            if len(parts) == 2:
                #print(parts)
                key = parts[0].strip()
                valid = set()
                valids = parts[1].split('or')
                for v in valids:
                    bits = [int(i) for i in v.split('-')]
                    for i in range(bits[0], bits[1]+1):
                        valid.add(i)
                        self.valid[i] = 1
                self.constraints[key] = valid

        section = 1
        self.tickets = []
        for line in self.data:
            if not line:
            	continue
            if "your ticket" in line:
                section = 2
                continue
            if "nearby tickets" in line:
                section = 3
                continue   
            if section == 2:
                bits = line.split(',')         
                self.your_ticket = [int(i) for i in line.split(',')]
            if section == 3:         
                t = [int(i) for i in line.split(',')]
                self.tickets.append(t)

    def run(self):
        total = 0
        #print (self.valid)
        #print(self.tickets)
        for t in self.tickets:
            for n in t:
                if n not in self.valid:
                    total += n

        print(total)

    def run2(self):
        self.valid_tickets = []
        for t in self.tickets:
            is_valid = True
            for n in t:
                if n not in self.valid:
                    is_valid = False
            if is_valid:
            	self.valid_tickets.append(t)

        # Look at each field
        ranges = []
        for i in range(len(self.tickets[0])):
            nums = set()
            for t in self.valid_tickets:
                nums.add(t[i])
            ranges.append(nums)

        print(ranges)

        candidates = []
        for nums in ranges:
        	candidate = []
        	for k, v in self.constraints.items():
        		if not (nums - v):
        			candidate.append(k)
        	candidates.append(candidate)

        print(candidates)

        while True:
            removed = False
            for c in candidates:
            	if len(c) == 1:
            		remove = c[0]
            		for d in candidates:
            			if remove in d:
            				if len(d) > 1:
            					d.remove(remove)
            					removed = True
            if not removed:
                break

        print(candidates)
        for c in candidates:
        	print(len(c))
        print (len(self.tickets[0]))
        print (len(self.valid_tickets))

        dep_fields = []
        for i, c in enumerate(candidates):
        	print (i,c)
        	if "departure" in c[0]:
        		dep_fields.append(i)
        print(dep_fields)

        prod = 1
        for i in dep_fields:
            prod *= self.your_ticket[i]
        print(prod)




p = Part1()
p.run()
p.run2()