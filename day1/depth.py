with open('input.txt') as f:
    lines = f.readlines()

decreased = 0
increased = 0

for i in range(len(lines)-3):
    #a = lines[i]
    #print(type(a),type(int(a)))
    this = int(lines[i])+int(lines[i+1])+int(lines[i+2])
    next = int(lines[i+1])+int(lines[i+2])+int(lines[i+3])
    if next > this: increased += 1
    if next < this: decreased += 1

print("Increased: ", increased, "; Decreased: ",decreased)
