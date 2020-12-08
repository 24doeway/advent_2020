good = 0
good_2 = 0

with open("day2.txt") as f:
    for line in f.readlines():
        parts = line.strip().split()
        print(parts)
        cmin, cmax = [int(i) for i in parts[0].split('-')]
        letter = parts[1][0]
        pwd = parts[2]
        print(cmin, cmax, letter, pwd)
        count = pwd.count(letter)
        if count >= cmin and count <= cmax:
            good += 1

        if (pwd[cmin - 1] == letter or pwd[cmax - 1] == letter) and not (pwd[cmin - 1] == letter and pwd[cmax - 1] == letter):
            good_2 += 1

print(good, good_2)
