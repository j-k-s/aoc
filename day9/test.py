mydict = {"b3" : "to check", "b2" : "basin", "c2" : "basin"}


print("Mydict is ",mydict)

for a in ["b2", "a2", "f2"]:
    if a in mydict:
        print("\n",a,"in mydict is",mydict[a])
    else:
        print(a,"is not in mydict. ...adding")
        mydict[a] = "basin"
        print("Mydict is ",mydict)


mytuple = (234,212,"basin")

myset = {mytuple}

print(mytuple)
print(myset)

newtuple = (234,212,"toassess")
