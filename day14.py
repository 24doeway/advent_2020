


class Part1:
    def __init__(self):
        with open("day14.txt") as f:
            self.data =  f.readlines()
        self.registers = {}

    def run_reg(self, reg, val):
        bin_val = bin(val)[2:]   # Remove 0b at start
        res = 0
        for i in range(1, min(len(self.mask), len(bin_val))+1):
            #print(i, self.mask[-i])
            m = self.mask[-i]
            v = bin_val[-i]
            if (m == '1' or (m == 'X' and v == "1")): 
                res += 2**(i-1)
        for i in range(min(len(self.mask), len(bin_val))+1, len(self.mask)+1):
            #print(i, self.mask[-i])
            m = self.mask[-i]
            if (m == '1'): 
                res += 2**(i-1)

        self.registers[reg] = res

    def run_mask(self, val):
        self.mask = val

    def parse_line(self, line):
        parts = line.split('=')
        cmd = parts[0].strip()
        val = parts[1].strip()
        if cmd == "mask":
            self.run_mask(val)
        else:
            reg = int(cmd.split('[')[1].split(']')[0])
            val = int(val)
            self.run_reg(reg, val)


    def run(self):
        for line in self.data:
            self.parse_line(line)

    def result(self):
        print (sum(self.registers.values()))


class Part2(Part1):
    def run_reg(self, reg, val):
        bin_reg = bin(reg)[2:]   # Remove 0b at start
        reg = {}
        for i in range(1,len(bin_reg)+1):
            v = bin_reg[-i]
            if v == '1':
                reg[i-1] = '1'

        for i in range(1,len(self.mask)+1):
            m = self.mask[-i]
            if (m == 'X'): 
                reg[i-1] = "X"
            if (m == '1'): 
                reg[i-1] = "1"

        start = 0
        for i in range(len(self.mask)+1):
            num = 2 ** i
            if reg.get(i,0) == '1':
                start += num
        registers = [start]
        for i in range(len(self.mask)+1):
            num = 2 ** i
            if reg.get(i,0) == 'X':
                new_registers = [i+num for i in registers]
                registers.extend(new_registers)

        #print (registers)

        for i in registers:
            self.registers[i] = val    



p = Part1()
p.run()
p.result()
p = Part2()
p.run()
p.result()