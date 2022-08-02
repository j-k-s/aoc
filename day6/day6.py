## read file
with open('input') as f:
    lines = f.readlines()

## create list from input data
def initialise_list():
    fish = lines[0].strip().split(',')
    for f in enumerate(fish): fish[f[0]] = int(f[1])
    return fish

## For certain number of days/cycles,
def analyse_population(days,fish):
    print(f"Analysing fish population over {days} days")
    print("Initial state: ",*fish)
    for day in range(days):
        newfish = 0
        for f in enumerate(fish):
            if f[1] == 0:
                fish[f[0]] = 6
                newfish += 1
            else: fish[f[0]] -=1
        for x in range(newfish): fish.append(8)
        # print(f"Day {day + 1} - fish: {fish}")
        population = len(fish)
    return population

## For each list item, if 0 change to 6 and append an 8, decrement everything else.

## Total fish function - length of the list


days = int(input("How many days to analyse? "))
initialfish = initialise_list()
population = analyse_population(days,initialfish)
print(f"The population after {days} days is {population}.")
