# AOC - day4 - Squid Bingo

## load file
with open('input') as f:
    lines = f.readlines()
numlines = len(lines)


## function to print a board
def printboard(board,match=False,drawnum=000):
    toprint = boards
    for row in range(5):
        mystr = ""
        for col in range(5):
            mystr = mystr + " " + str(toprint[board][row][col]).rjust(2,"0")
        print(row,mystr)
    if match:
        toprint = matches
        print ("--- Matches ----")
        for row in range(5):
            mystr = ""
            for col in range(5):
                mystr = mystr + " " + str(toprint[board][row][col]).rjust(2,"0")
            print(mystr)

## check win, return win/nowin and winning drawnumber number if win

def checkwin(board,drawnum,maxmatch):
    #print("Running checkwin function now")
    #print("====max_match is",maxmatch,"====")
    #printboard(board,True,drawnum)
    rowtotals, coltotals = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]    #create lists
    outcome = "nowin"
    for row in range(5):
        for col in range(5):
            if matches[board][row][col] == 1:
                #print("1 at row",row+1,"column",col+1)
                rowtotals[row] += 1
                coltotals[col] += 1
                """if rowtotals[row] > maxmatch:
                    maxmatch = rowtotals[row]
                    #print("new max match:", maxmatch)
                if coltotals[col] > maxmatch:
                    maxmatch = coltotals[col]
                    #print("new max match:", maxmatch) """
                if rowtotals[row] == 5 or coltotals[col] == 5:
                    outcome = "win"
    return outcome
        #print("about to return",outcome, row, col, drawnum, maxmatch)
        #if board == 0: x = input()


    #print("board to analyse:")
    #print(boards[board])
    #print("-- rowtotals",rowtotals)
    #print("coltotals",coltotals)
    #x = input()


## create list of numbers drawn from first line
draw_nums_extracted = lines[0].strip('\n').split(',')

## create 3-d list of boards
## also create 1-d list of win/nowin per board
boards = []
boardwins = []

for l in range(len(lines)):
    if l < 2: continue ## ignore the draw numbers
    if (l - 2) % 6 == 0: #first row of any board
        board = int((l - 2) / 6)
        thisboard = []
        for row in range(5):
            thisrow = []
            line = lines[l+row].strip('\n')
            for col in range(5):
                thisnum = int(line[col*3:2+col*3])
                thisrow.append(thisnum)
            thisboard.append(thisrow)
        boards.append(thisboard)
        boardwins.append("nowin")

## create 3-d list of matches
# initiate matches list
matches = []
for b in range(len(boards)):
    matches.append([])
    for r in range(5):
        matches[b].append([])
        for c in range(5):
            matches[b][r].append(0)
#print("len(matches)",len(matches),"len(matches[0])",len(matches[0]),"len(matches[0][0])",len(matches[0][0]))
#x = input()

## for each number drawn, compare to every board position and write to results list.
 # Also run a check for any winning rows columns
def checkdraw(draw_nums):
    max_match = 0
    #print("====max_match is",max_match,"====")
    for d in draw_nums:
        for board in enumerate(boards):
            if boardwins[board[0]] == "nowin":
                for row in enumerate(board[1]):
                    for col in enumerate(row[1]):
                        thisnum = boards[board[0]][row[0]][col[0]]
                        if thisnum == int(d):
                            matches[board[0]][row[0]][col[0]] = 1
                            results = checkwin(board[0],d,max_match)
                            if results == "win":
                                #print("Win", results[1], results[2], "Drawnum =",results[3])
                                #printboard(board[0],True,d)
                                boardwins[board[0]] = "win"
                                #print(boardwins)
                                #print(board[0])
                                totalwins = countwins(boardwins)
                                nonwins = len(boardwins) - totalwins + 1
                                if nonwins == 1:
                                    status = [d,board[0]]
                                    print("About to return\nTotalwins =",totalwins)
                                    return status
    return "checkdraw error - shouldn't be here"


def countwins(boardwins):
    totalwins = 0
    for w in boardwins:
        if w == "win": totalwins +=1
    return totalwins

finaldrawnum, last_board = checkdraw(draw_nums_extracted)
printboard(last_board,True)
print("Final draw num: ", finaldrawnum)
## For a winning board, sum all the unmarked numbers, multiply by final number

print("last winning board is ",last_board)
remaining_total = 0
for r in enumerate(boards[last_board]):
    for c in enumerate(r[1]):
        if matches[last_board][r[0]][c[0]] == 0:
            remaining_total += c[1]
print("\"Remaining total\" is: ",remaining_total)
print("Final Score = last Draw-number * Remaining-total")
print("Final Score =", finaldrawnum,"*",remaining_total)
print("            =",int(finaldrawnum) * remaining_total)

#############
"""
create wins list
How many wins - count wins in win list
Check win on a board
If win, update wins list
 if only one left not winning, that's the last.
"""
