with open('example_input') as f:
    lines = f.readlines()
bits = 5
numlines = len(lines)



def countbits(lineskeep):
    # Initiate dictionary char pos & counts
    counts = {}
    for c in range(bits):
        key = c
        value = 0
        counts[key] = value

    # Count number of 1's in each character slot
    for l in lineskeep:
        for c in range(bits):
            if int(l[0][c]) == 1 and l[1] == "keep":
                counts[c] += 1
    print("counts is",counts)
    return counts

def decode(phase):
    # Convert lines (input) into 2-d list with original line & discard status
    lineskeep = []
    for l in lines:
        lineskeep.append([l.strip('\n'),"keep"])

    # Allocate a discard/keep status for each line; break if n-1 discards reached.
    discardcount = 0
    for c in range(bits):
        counts = countbits(lineskeep)
        n = input()
        if counts[c] <= int(numlines /2 ):
            popchar = 0
        else: popchar = 1
        for l in lineskeep:
            if discardcount == len(lines) - 1:
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
    return("Error")


oxygen_generator_rating = decode("oxy")
x = input()
co2scrub = decode("co2")



print("Oxygen generator rating is",oxygen_generator_rating)
print("Co2 Scrubber rating is",co2scrub)
print("product is", oxygen_generator_rating * co2scrub)
