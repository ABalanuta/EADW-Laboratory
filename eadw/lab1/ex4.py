
def read_file(file_name):
    Rfile = open(file_name, "r")
    toReturn = []
    for line in Rfile:
        parsed = line.split()
        toReturn += parsed
    return toReturn
    
mySet1 = set(read_file("text1.txt"))
mySet2 = set(read_file("text2.txt"))

both = mySet1.intersection(mySet2)

print len(mySet1)
print len(mySet2)
print len(both)

print both