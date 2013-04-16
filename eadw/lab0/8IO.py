

f = open("text.txt", "r")
lista = []

for line in f:
    lista.append(line.split()[0])
f.close()
print lista


print "-------"

f = open("test.txt", "w")
f.write("Sapos")
f.close()



print "--------"

print " THis is  A BEOUTIFUL NUMBER %0.10f" %33620.332
