from ex1 import qsort

readFile = open("list_of_numbers.txt", "r")

lista = []

for linha in readFile:
    lista.append(int(linha))  

print lista
qsort(lista, 0, len(lista)-1)
print lista