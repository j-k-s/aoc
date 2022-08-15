## read file
with open('input') as f:
    lines = f.readlines()

basin_map = set()

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
    lows = set()
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
                lows.add((row[0],col[0]))
                risk_total += int(col[1]) + 1
    results = [risk_total, lows]
    return results


##################### Part 2 - tricky ######################

## function to take in coordinates, and return its 2, 3 or 4 neighbours in a list
def get_neighbours(loc):
    results = []
    if loc[0] != 0: results.append((loc[0]-1,loc[1])) ## row before
    if loc[0] != len(mapdata) -1 : results.append((loc[0]+1,loc[1])) ## next row down
    if loc[1] != 0: results.append((loc[0],loc[1]-1)) ## column before
    if loc[1] != len(mapdata[0]) -1: results.append((loc[0],loc[1] + 1)) ## column after
    return results

def value_at(coords):
    return int(mapdata[coords[0]][coords[1]])


def evaluate_basins(lows):
    basin_sizes = {}        ## initialise basin size tracker
    for low in lows: basin_sizes[low] = 1
    #print("basin sizes dictionary:",basin_sizes)
    basin_map.update(lows)    ## add lows (tuples) to basins_map (set)
    for basin in lows:
        to_check = set()
        to_check.add(basin)
        #print("to check is:",to_check)
        #x = input()
        while len(to_check) > 0:
            ## create new work list to iterate through:
            work_list = []
            for c in to_check: work_list.append(c)
            #print("\n ==== work list is:",work_list, "====\n")
            for point_to_check in work_list:
                ## for each neighbour
                ##   if higher than value at location N and not 9:
                ##   add this location to basin set
                ##   add this location to the check set
                ##   increment counter for basin size
                neighbours = get_neighbours(point_to_check)
                #print(f"point is {point_to_check}, neighbours: {neighbours}")
                for n in neighbours:
                    #n_value = mapdata[n[0]][n[1]]
                    #print(f"Neighbour {n} with value {n_value}")
                    if value_at(n) > value_at(point_to_check) and value_at(n) < 9 and n not in basin_map:
                        #print("Basin point! Value at",n,"is",value_at(n))
                        basin_map.add(n)  ## found new point in a basin
                        to_check.add(n)
                        basin_sizes[basin] += 1
                        #print(f"Basin_map is {basin_map}")
                #print("here's to_check", to_check)
                #print("about to remove", point_to_check,"from to_check.")
                to_check.remove(point_to_check) # check complete
                #print("here's to_check", to_check)
                #x = input()
        #print("------Finished on basin",basin,"------")
    #print("run out of items in to_check!")
    #print("Here's basin_sizes:",basin_sizes)
    #print("-------------------------")
    size_list, top3 = [], []
    for v in basin_sizes.values(): size_list.append(v)
    size_list.sort(reverse=True)
    for a in range(3): top3.append(size_list[a])
    return top3



## add lows to check(set)

## take first item, N (coordinates tuple) in check set while check set is not empty
## get all N's neighbours' coordinates

## function to cycle through neighbours



## Main program
mapdata = load_data(lines)
risk_total,lowsdata = find_lows(mapdata)      ## process mapdata and record lows
print(f"lows data is {lowsdata}\n")
top3 = evaluate_basins(lowsdata)

print(f"Risk Total is {risk_total}")
print(f"Top 3 values are {top3[0]}, {top3[1]} and {top3[2]}")
print(f"{top3[0]} * {top3[1]} * {top3[2]} = {top3[0] * top3[1] * top3[2]}")

## notes -- go to the for n in neighbours loop
