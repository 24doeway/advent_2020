passports = []
passport = {}
valid = 0

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

valid_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def check_ecl(value):
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if value not in valid:
        return False
    return True

def check_hgt(value):
    if value.endswith('in'):
        value = int(value.split('in')[0])
        min = 59
        max = 76
        if value >= min and value <= max:
            return True
        else:
            return False
    if value.endswith('cm'):
        value = int(value.split('cm')[0])
        min = 150
        max = 193
        if value >= min and value <= max:
            return True
    return False

def check_hcl(value):
    if value.startswith('#'):
        value = value[1:]
        if len(value) == 6:
            check = set([i for i in value])
            valid = set([i for i in "0123456789abcdef"])
            if not (check - valid):
                return True
    return False

def check_pid(value):
    if True:
        if len(value) == 9:
            check = set([i for i in value])
            valid = set([i for i in "0123456789"])
            if not (check - valid):
                return True
    return False

def check_byr(value):
    value = int(value)
    min = 1920
    max = 2002
    if value >= min and value <= max:
        return True
    return False

def check_iyr(value):
    value = int(value)
    min = 2010
    max = 2020
    if value >= min and value <= max:
        return True
    return False

def check_eyr(value):
    value = int(value)
    min = 2020
    max = 2030
    if value >= min and value <= max:
        return True
    return False


def check_true(value):
    return True

validators = {'byr': check_byr,
              "iyr": check_iyr,
              "eyr": check_eyr,
              "hgt": check_hgt,
              "hcl": check_hcl,
              "ecl": check_ecl,
              "pid": check_pid,
              "cid": check_true}


with open("day4.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            passports.append(passport)
            pkeys = set(passport.keys())
            bad = False
            if not (valid_keys - pkeys):
                for field, value in passport.items():
                    fn = validators[field]
                    if not fn(value):
                        bad = True

                if not bad:
                    valid += 1
                #print(passport, "valid")
            else:
                pass
            passport = {}

        bits = line.split()
        for bit in bits:
            key, value = bit.split(':')
            passport[key] = value


print(valid)
