## read file
with open('input1') as f:
    lines = f.readlines()

def process_input():
    dots_list = []
    instructions = []
    for l in lines:
        n = l.strip().split(',')
        if len(n) == 2:
            coord = []
            for m in n: coord.append(int(m))
            dots_list.append(coord)
        if l[0:4] == "fold":
            axis = l.strip().split(" ")[2].split("=")[0]
            numb = int(l.strip().split(" ")[2].split("=")[1])
            instructions.append([axis,numb])
    print("===========\ndots list:",dots_list)
    print("===========\ninstructions:",instructions)



## Main program
process_input()
