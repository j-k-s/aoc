## read file
with open('input1') as f:
    lines = f.readlines()

## split lines into one list
positions = lines[0].strip().split(',')
for p in enumerate(positions):
    positions[p[0]] = int(p[1])

evaluated = {}

## find max min and avg of positions

## calculate total distance when beginning at avg - this equals "best"

## move to avg + 1 if total is lower, keep going until total goes up; keep best

## ...but if total is higher above avg, go to avg-1 and keep going until total goes up

def find_min_max_avg(inputdata):
    ttl, avg, min, max, cnt = 0, 0, 0, 0, 0
    for i in inputdata:
        cnt +=1
        ttl += i
        if i > max: max = i
        if i < min: min = i
    avg = int(ttl / cnt)
    results = [min, max, avg]
    return results

def evaluate_distance(startpos):
    inputdata = positions
    total_distance = 0
    for i in inputdata:
        adder = 0
        diff = abs(i - startpos)
        for d in range(diff):
            adder += 1
            total_distance += adder
    evaluated[startpos] = total_distance
    #print(f"evaluated position {startpos} to distance {total_distance}")
    return total_distance

def optimise(minmaxavg,inputdata):
    min, max, avg = minmaxavg
    for a in range(min,max+1,1): evaluated[a] = -1 # initialise tracker
    #print(evaluated)
    ## while searching = True, creep upward until worse
    this_start_pos = avg
    best_position = this_start_pos
    lowest_distance = evaluate_distance(this_start_pos)
    ## try one to the right
    ## if better, keep trying one to the right
    this_start_pos +=1
    this_distance = evaluate_distance(this_start_pos)
    while this_distance < lowest_distance:  # i.e. found a new lowest
        lowest_distance = this_distance     # update lowest
        best_position = this_start_pos
        this_start_pos +=1                  # move to the right + evaluate
        this_distance = evaluate_distance(this_start_pos)
    this_start_pos = avg -1
    this_distance = evaluate_distance(this_start_pos)
    while this_distance < lowest_distance:  # i.e. found a new lowest
        lowest_distance = this_distance     # update lowest
        best_position = this_start_pos
        this_start_pos -=1                  # move to the right + evaluate
        this_distance = evaluate_distance(this_start_pos)
    print(f"lowest distance is {lowest_distance} in position {best_position}")

minmaxavg = find_min_max_avg(positions)
optimise(minmaxavg,positions)
#print(total_distance)
