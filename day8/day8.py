## read file
with open('input') as f:
    lines = f.readlines()
all_data = []

## Split each line of input data into 2 lists of strings
## List of lines (all data, l lines)
##   -- List containing Signal Patterns and Output Value (2 entries)
##      -- list of strings (SP = 10?, OV = 4)
##         -- string

def prepare_data():
    for l in lines:
        line_data = []
        x = (l.strip().split('|'))
        for n in enumerate(x): line_data.append(n[1].split())
        all_data.append(line_data)

## For every line, OV only, count how many 1,4,7 and 8 segment numbers appear
def eval_digits():
    digit_tally = [0,0,0,0,0,0,0,0]
    for a in all_data:
        for string in a[1]:
            digit_tally[len(string)] += 1
    ## total of 1, 4, 7 and 8 is:
    total_1478 = 0
    for t in [2,3,4,7]: total_1478 += digit_tally[t]
    print(f"Digit tally is {digit_tally}")
    print(f"total_1478 is {total_1478}")

def checkforchar(thischar,thisstring):
    for s in thisstring:
        if thischar == s: return True
    return False

def find_digits():
    total = 0
    for a in all_data:
        _2seg, _3seg, _4seg, _7set = "", "", "", ""
        all5segs, all6segs = [], []
        for s in a[0]:
            if len(s) == 2: _2seg = ''.join(sorted(s))
            if len(s) == 3: _3seg = ''.join(sorted(s))
            if len(s) == 4: _4seg = ''.join(sorted(s))
            if len(s) == 7: _7seg = ''.join(sorted(s))
            if len(s) == 5: all5segs.append(''.join(sorted(s)))
            if len(s) == 6: all6segs.append(''.join(sorted(s)))
        num1 = _2seg
        num7 = _3seg
        num4 = _4seg
        num8 = _7seg
        print("2, 3, 4 and 7 segs = ",_2seg, _3seg, _4seg, _7seg)
        print("5 segs are =",*all5segs)
        ## Find Segment A ##
        for char in _3seg:
            if checkforchar(char,_2seg) == False: segA = char
        print("SegA is",segA)
        ## Find Segment D ##
        find_middle = all5segs[0] + all5segs[1] + all5segs[2] + _4seg
        counts = [0,0,0,0,0,0,0]
        print(f"find_middle (segD) string is: {find_middle}")
        for x in enumerate(['a','b','c','d','e','f','g']):
            for char in find_middle:
                if char == x[1]: counts[x[0]] += 1
        for x in enumerate(counts):
            if x[1] == 4:
                segs = 'abcdefg'
                segD = segs[x[0]]
        print("SegD is",segD)
        ## Find segment B (top left)
        _4segminus_2seg = ""
        for char in _4seg:
            if checkforchar(char,_2seg) == False: _4segminus_2seg = _4segminus_2seg + char
        print(f"_4seg is {_4seg}, 2seg is {_2seg}, 4seg-2seg is {_4segminus_2seg}")
        for char in _4segminus_2seg:
            if char != segD: segB = char
        print("SegB is",segB)
        ## Get number 0
        num0 = ""
        for char in _7seg:
            if char != segD: num0 = num0 + char
        print("num0 is ",num0)
        ## Get Number 6
        print("all 6 segs is ",all6segs)
        for asix in all6segs:
            if asix != num0:
                if checkforchar(segD,asix) == True and checkforchar(_2seg[0],asix) == True and checkforchar(_2seg[1],asix) == True:
                    num9 = asix
        print("num9 then, is",num9)
        for asix in all6segs:
            if asix != num9 and asix != num0:
                num6 = asix
        print("num6 then, is",num6)
        ## Find Number 3
        print("all 5 segs is ",all5segs)
        for afive in all5segs:
            if checkforchar(_2seg[0],afive) == True and checkforchar(_2seg[1],afive): num3 = afive
        print("num3 is",num3)
        ## Find Number 5
        for afive in all5segs:
            if afive != 3 and checkforchar(segB,afive) == True: num5 = afive
        print("num5 is",num5)
        for afive in all5segs:
            if afive != num3 and afive != num5: num2 = afive
        print("num2 is",num2)
        allnums = {num0 : 0, num1 : 1, num2 : 2, num3 : 3, num4 : 4 , num5 : 5, num6 : 6, num7 : 7, num8 : 8, num9: 9}
        readout = ""
        for n in a[1]:
            nsorted = ''.join(sorted(n))
            readout = readout + str(allnums[nsorted])
        total += int(readout)
    return total



## Main program

prepare_data()
eval_digits()
total = find_digits()
print("=== total is ===",total)


"""
2-seg : 1
3-seg : 7
4-seg : 4
5-seg : 2 , 3 , 5
6-seg : 6 , 9 , 0
7-seg : 8

Rules:
3-seg minus 2-seg = seg-A (top)
common to all 5 dig  & 4-seg = seg-D (middle)
4-seg minus 2-seg and seg-D = seg-B (top-left)
7-seg minus seg-D = number 0
6-seg, includes seg-D (middle) and 2-seg = number 9
6-seg, not number 0 and not number 9 = number 6
5-seg, includes 2-seg = number 3
5-seg, not no-3, includes seg-B = number 5
5-seg, not no-3 or no-5 = number 2

"""
