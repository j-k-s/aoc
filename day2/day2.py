with open('input') as f:
    lines = f.readlines()

position = 0
depth = 0
aim = 0

for i in lines:
    inst = i.split()
    dir = inst[0]
    dst = int(inst[1])
    if dir == "forward":
        position = position + dst
        depth = depth + (aim * dst)
    if dir == "down": aim = aim + dst
    if dir == "up": aim = aim - dst

print("Position: ",position)
print("Depth: ",depth)
print("Product: ", position * depth)
