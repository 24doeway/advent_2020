

with open("day7.txt") as f:
    for line in f.readlines():
        line = line.strip()
        parts = line.split('contain')
        outer = parts[0].split('bags')[0].strip()

        inner = {}
        print(parts[1])
        if parts[1].strip() != "no other bags.":
            right = parts[1].split('bag')
            for i in right[:-1]:
                bits = i.split()
                print(bits)
                col = ' '.join(bits[-2:])
                num = int(bits[-3])
                inner[col] = num
                print (num, col)
        customs[outer] = inner
 

def contains_colour(check_list, colour_list):
    ret = {}
    for c in colour_list:
        ret[c] = 1
        for k, v in check_list.items():
            if c in v:
                ret[k] = 1
    return ret.keys()    

check_list = contains_colour(customs, ["shiny gold"])
while True:
    new_list = contains_colour(customs, check_list)
    print (len(new_list))
    if len(new_list) == len(check_list):
        break
    else:
        check_list = new_list
print (len(check_list)-1)


known_counts = {}
def expand_bags(bag_list):
    for col,contents in bag_list.items():
        if not contents:
            known_counts[col] = 1
        if not set(contents.keys()) - set(known_counts.keys()):
            # We know all the bag contents
            bag_count = 1
            for c, count in contents.items():
                bag_count += count * known_counts[c]
            known_counts[col] = bag_count

while "shiny gold" not in known_counts:
    expand_bags(customs)
    print(known_counts)

print (known_counts["shiny gold"] - 1)



