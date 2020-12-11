






def tick(data):
    new_data = []
    row_length = len(data[0])
    col_length = len(data)
    for i in range(len(data)):
        new_row = ""
        for j in range(row_length):
            adj = 0
            current = data[i][j]
            for new_j in range(max(0,j-1),min(j+2,row_length)):
                for new_i in range(max(0,i-1),min(i+2,col_length)):
                    if data[new_i][new_j] == "#":
                        adj += 1
            #if current == "#":
            #    adj -= 1
            if current == "L" and adj == 0:
                new_row = new_row + "#"
            elif current == "#" and adj >= 5: # 4 plus yourself
                new_row = new_row + 'L'
            else:
                new_row = new_row + current
        new_data.append(new_row)
    return new_data

def tick2(data, max_step=200, max_look=5):
    new_data = []
    row_length = len(data[0])
    col_length = len(data)
    for i in range(len(data)):
        new_row = ""
        for j in range(row_length):
            adj = 0
            current = data[i][j]

            for new_j in [-1,0,1]:
                for new_i in [-1,0,1]:
                    # new_i and new_j are now adj_directions
                    # look in direction until we see a seat
                    for step in range(1, max_step+1):
                        try:
                            i_index = i+new_i*step
                            j_index = j+new_j*step
                            if i_index >= 0 and j_index >= 0:
                                if data[i_index][j_index] == "#":
                                    if not(new_i == 0 and new_j == 0):
                                        adj += 1
                                    break
                                if data[i_index][j_index] == "L":
                                    break
                        except IndexError:
                            break

            if current == "L" and adj == 0:
                new_row = new_row + "#"
            elif current == "#" and adj >= max_look:
                new_row = new_row + 'L'
            else:
                new_row = new_row + current
        new_data.append(new_row)
    return new_data


with open("day11.txt") as f:
    data = [a.strip() for a in f.readlines()]
while True:    
    #print(data)
    new_data = tick(data)
    nd = ''.join(new_data)
    d = ''.join(data)
    if nd == d:
        print("Finished", nd.count('#'))
        break
    data = new_data


with open("day11.txt") as f:
    data = [a.strip() for a in f.readlines()]
while True:    
    #print(data)
    new_data = tick2(data, 1, 4)
    nd = ''.join(new_data)
    d = ''.join(data)
    if nd == d:
        print("Finished", nd.count('#'))
        break
    data = new_data



with open("day11.txt") as f:
    data = [a.strip() for a in f.readlines()]
while True:    
    #print(data)
    new_data = tick2(data)
    nd = ''.join(new_data)
    d = ''.join(data)
    if nd == d:
        print("Finished", nd.count('#'))
        break
    data = new_data


