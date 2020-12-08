total = 0
everyone = None

with open("day6.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            total += len(everyone)
            everyone = None
        else:
            uniq = set()
            for c in line:
                uniq.add(c)    
            if everyone == None:
                everyone = uniq
            else:
                everyone = everyone & uniq


print(total)
