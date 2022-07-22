with open('input') as f:
    lines = f.readlines()
bits = 12
numlines = len(lines)

def countbits(list_to_eval):
    # Initiate dictionary char pos & counts
    counts = {}
    for c in range(bits):
        key = c
        value = 0
        counts[key] = value

    # Count number of 1's in each character slot
    for l in list_to_eval:
        for c in range(bits):
            if int(l[0][c]) == 1 and l[1] == "keep":
                counts[c] += 1
    return counts

def decode(phase):
    # Initiate list with data and "keep" status - one time (per phase)
    lineskeep = []
    for l in lines:
        lineskeep.append([l.strip('\n'),"keep"])
    #print("=== Lineskeep initial status === ...")
    #for l in lineskeep: print(l[0],"--",l[1])
    #x = input()

    # Allocate a discard/keep status for each line; break if n-1 discards reached.
    discardcount = 0
    for c in range(bits):
        numkeeps = 0
        for l in lineskeep:
            if l[1] == "keep": numkeeps += 1

        counts = countbits(lineskeep)
        print("=================================")
        print("Bit:",c,"Counts:")
        print(counts)

        if counts[c] * 2 >= numkeeps:
            popchar = 1
        else: popchar = 0
        print("This time (counts[",c,"]=",counts[c],"numkeeps=",numkeeps,"popchar=",popchar)
        for l in lineskeep:
            if discardcount == len(lines) - 1:
                print("=== final ===")
                for l in lineskeep: print(l[0],"--",l[1])
                for l in lineskeep:
                    if l[1] == "keep":
                        return int(l[0],2)
            else:
                if l[1] != "discard":
                    if phase == "oxy":
                        if int(l[0][c]) == popchar:
                            l[1] = "keep"
                        else:
                            l[1] = "discard"
                            discardcount += 1
                    if phase == "co2":
                        if int(l[0][c]) != popchar:
                            l[1] = "keep"
                        else:
                            l[1] = "discard"
                            discardcount += 1
        for l in lineskeep: print(l[0],"--",l[1])
        #x = input()

    return("Error")


oxygen_generator_rating = decode("oxy")
#x = input()
co2scrub = decode("co2")



print("Oxygen generator rating is",oxygen_generator_rating)
print("Co2 Scrubber rating is",co2scrub)
print("product is", oxygen_generator_rating * co2scrub)
