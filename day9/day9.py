## read file
with open('input1') as f:
    lines = f.readlines()


## load data into list
def load_data(mydata):
    mapdata = []
    for m in mydata:
        row = []
        n = m.strip()
        for point in n: row.append(point)
        mapdata.append(row)
    #print(mapdata)
    return mapdata

## for every row evaluate each entry
## for each entry check whether neighbours in the row or in the column are greater
## need to handle special cases for first and last row and column

def low_check(row,col,N,S,E,W):
    Nhigher, Shigher, Ehigher, Whigher = True, True, True, True
    if N == True:
        if mapdata[row - 1][col] <= mapdata[row][col]: Nhigher = False
    if S == True:
        if mapdata[row + 1][col] <= mapdata[row][col]: Shigher = False
    if E == True:
        if mapdata[row][col + 1] <= mapdata[row][col]: Ehigher = False
    if W == True:
        if mapdata[row][col - 1] <= mapdata[row][col]: Whigher = False
    is_this_low = Nhigher and Shigher and Ehigher and Whigher
    return is_this_low

def find_lows(map):
    risk_total = 0
    for row in enumerate(map):
        #print(f"row {row[0] + 1}")
        for col in enumerate(row[1]):
            N = False if row[0] == 0 else True
            S = False if row[0] == len(map) -1 else True
            E = False if col[0] == len(row[1]) -1 else True
            W = False if col[0] == 0 else True
            if low_check(row[0],col[0],N,S,E,W) == True:
                #print(f"low at row {row[0]} col {col[0]}, number {col[1]}")
                risk_total += int(col[1]) + 1
    print(f"Risk total = {risk_total}")
        #print("len map is ", len(map))


##################### Part 2 - tricky ######################

## add lows (tuples) to basins_map (set)
## add lows to check(set)

## take first item, N (coordinates tuple) in check set while check set is not empty
## get all N's neighbours' coordinates
## for each neighbour
##   if higher than value at location N and not 9:
##   add this location to basin set
##   add this location to the check set
##   increment counter for basin size


## function to take in coordinates, and return its 2, 3 or 4 neighbours in a list
def get_neighbours(location):
    results = []
    if location[0] != 0: results.append((location[0]-1,location[1])) ## row before
    if location[0] != len(mapdata): results.append((location[0]+1,location[1])) ## next row down
    if location[1] != 0: results.append((location[0],location[1]-1)) ## column before
    if location[1] != len(mapdata[0]): results.append((location[0],location[1] + 1)) ## column after
    return results

## function to cycle through 2, 3 or 4 neighbours and



## Main program
mapdata = load_data(lines)
find_lows(mapdata)

print("neighbours",get_neighbours(testA))
