## read file
with open('input') as f:
    lines = f.readlines()

## create list from input data
def initialise_list():
    fish = lines[0].strip().split(',')
    fish_counts = [0,0,0,0,0,0,0,0,0]
    for f in enumerate(fish):
        fish_counts[int(f[1])] += 1

    return fish_counts

## For certain number of days/cycles,
def analyse_population(days,fishcounts):
    for d in range(days):
        zeros = fishcounts[0]
        for x in range(8): fishcounts[x] = fishcounts[x+1]
        fishcounts[6] += zeros
        fishcounts[8] = zeros
    population = 0
    for c in fishcounts: population += c
    return population


## For each list item, if 0 change to 6 and append an 8, decrement everything else.

## Total fish function - length of the list


days = int(input("How many days to analyse? "))
fish_counts = initialise_list()
population = analyse_population(days,fish_counts)
print(f"The population after {days} days is {population}.")
