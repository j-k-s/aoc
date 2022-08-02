import re

## read file
with open('input') as f:
    lines = f.readlines()

## create list of 4-item lists
## split by space and comma, and only taking number items
inputdata = []
def file_to_list():
    inputstemp = []
    for line in lines: inputstemp.append(re.split(',|\s->\s',line.strip()))
    for line in inputstemp:
        list_of_ints = []
        for a in range(4): list_of_ints.append(int(line[a]))
        inputdata.append(list_of_ints)

## initialise map - find largest X and Y numbers
## create a 2d list that size, filled with zero's

def find_largest(dataset):
    largest_x, largest_y = 0, 0
    for num in dataset:
        if num[0] > largest_x: largest_x = num[0]
        if num[2] > largest_x: largest_x = num[2]
        if num[1] > largest_y: largest_y = num[1]
        if num[3] > largest_y: largest_y = num[3]
    largest = [largest_x,largest_y]
    return largest

def initialise_map():
    largest_x, largest_y = find_largest(inputdata)
    map = []
    for row in range(largest_y + 1):
        map_row = []
        for n in range(largest_x + 1): map_row.append(0)
        map.append(map_row)
    return map


## for every line check if either x's or y's are equal
## if they are, figure out how to fill in the relevant map points with +1

def analyse_lines(inputs):
    doprint = False
    for line in inputs:
        #if line[1] == 990: doprint = True
        if line[0] == line[2]: #orient = vert
            if doprint: print("===vertical line===", line)
            if line[1] < line[3]:
                linestart = line[1]
                lineend = line[3]
            else:
                linestart = line[3]
                lineend = line[1]
            for vertpoint in range(linestart,lineend+1):
                mymap[vertpoint][line[0]] += 1
                if doprint: print("X is",line[0],"vertpoint is",vertpoint,"\n")
        elif line[1] == line[3]: #orient = "hor"
            if doprint: print("===horizonal line===", line)
            if line[0] < line[2]:
                linestart = line[0]
                lineend = line[2]
            else:
                linestart = line[2]
                lineend = line[0]
            for horpoint in range(linestart,lineend+1):
                if doprint: print("Y is",horpoint,"line[1] is",line[1],"\n",mymap[line[1]][horpoint])
                mymap[line[1]][horpoint] += 1

        else:
            ## NOTES --- error - turning all diagonals into positive gradiant
            if line[0] < line[2]:
                xdir = 1
                xstart = line[0]
                xend = line[2] + xdir
            else:
                xdir = -1
                xstart = line[0]
                xend = line[2] + xdir
            if line[1] < line[3]:
                ydir = 1
                ystart = line[1]
                yend = line[3] + ydir
            else:
                ydir = -1
                ystart = line[1]
                yend = line[3] + ydir
            yadj = 0
            for p in range(xstart,xend,xdir):
                xpos = p
                ypos = ystart + yadj
                yadj = yadj + ydir
                mymap[ypos][xpos] += 1

## then loop through the map and count the 2's
def count_overlaps(map):
    ones, twos, mores = 0, 0, 0
    for row in map:
        for col in row:
            if col == 1: ones += 1
            if col == 2: twos += 1
            if col > 2: mores +=1
    results = [ones, twos, mores]
    return results

## Main script

file_to_list()
mymap = initialise_map()
analyse_lines(inputdata)
results = count_overlaps(mymap)
#for y in mymap: print(*y)
ones, twos, mores = results[0], results[1], results[2]
print("Total ones:",ones,"\nTotal twos:",twos,"\nMore:",mores)
print("Twos or more:",twos + mores)
