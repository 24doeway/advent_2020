import copy

index = 25
check = 25


with open("day9.txt") as f:
    data = [int(i) for i in f.readlines()]

def check_is_sum_of(num, num_set):
    for i in num_set:
        check_set = copy.copy(num_set)
        check_set.remove(i)
        if (num - i) in num_set:
            return True
    return False

for i in range(index, len(data)):
    num = data[i]
    check_list = data[i-check:i]
    if not check_is_sum_of(num, check_list):
        print (num)
        break

target_num = num



finish = False
for i in range(0, len(data)):
    if finish:
        break
    trial = []
    total = 0
    for j in range(i, 0,-1):
        trial.append(data[j])
        total += data[j]
        if total == target_num:
            print(trial)
            finish = True
            break
        if total > target_num:
            break

print (min(trial))
print (max(trial))

print (min(trial) + max(trial))