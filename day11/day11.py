
## read file
with open('input1') as f:
    lines = f.readlines()

alldata = []
for row in lines:
    thisrow = []
    for col in row.strip(): thisrow.append(int(col))
    alldata.append(thisrow)
workingdata = alldata

def dataprint(lol):
    print("===========")
    for row in lol:
        print(*row)

def get_neighbours(loc):
    row = loc[0]
    col = loc[1]
    rowmax = len(workingdata) - 1
    colmax = len(workingdata[0]) - 1
    results = [] ## list of tuples (coords)
    if row != 0:  ## row before
        results.append((row-1,col))
        if col != 0: results.append((row-1,col-1))
        if col < colmax: results.append((row-1,col+1))
    if col != 0: results.append((row,col-1)) ## left neighbour
    if col < colmax: results.append((row,col+1)) ## right neighbour
    if row < rowmax: ## row after
        results.append((row+1,col))
        if col != 0: results.append((row+1,col-1))
        if col < colmax: results.append((row+1,col+1))
    return results


def increasethis(input):
    if input == 9 or input == -1: return -1
    elif input == -2: return -2
    else: return input + 1

## increase all - turn 9s into -1 (for flash)
## then get all adjacents of each F and increase them

def process_step():
    flashing = set() ## track coords
    flashes = 0
    for r in enumerate(workingdata):
        for c in enumerate(r[1]):
            workingdata[r[0]][c[0]] = increasethis(c[1]) ## increment everything
            if increasethis(c[1]) == -1:                 ## and check for Flash
                flashes += 1
                flashing.add((r[0],c[0]))
                workingdata[r[0]][c[0]] = -2
    while len(flashing) > 0:
        worklist = []                   ## create new worklist
        for f in flashing:              ## and empty flashing set
            worklist.append(f)
        flashing = set()
        for w in worklist:
            row, col = w[0], w[1]
            coords = (row,col)
            neighbours = get_neighbours(coords)
            for n in neighbours:
                nrow, ncol = n[0], n[1]
                ncoords = (nrow,ncol)
                newval = increasethis(workingdata[nrow][ncol])
                workingdata[nrow][ncol] = newval
                if newval == -1:
                    flashes += 1
                    flashing.add(ncoords)
                    workingdata[nrow][ncol] = -2
    for r in enumerate(workingdata): ## step finished, rotate -1s to 0
        for c in enumerate(r[1]):
            if workingdata[r[0]][c[0]] == -2: workingdata[r[0]][c[0]] = 0
    return flashes

def checksyncd():
    for a in workingdata:
        for b in a:
            if b !=0: return False
    return True


dataprint(workingdata)
total_flashes = 0
syncd = False
step = 0
while syncd == False:
    step += 1
    flashes = process_step()
    syncd = checksyncd()
    if syncd == True:
        print("syncd is True. Step is:",step)
    total_flashes += flashes
    dataprint(workingdata)
    print("-- step processed")
    #x = input()
    print("Total flashes:",total_flashes)
