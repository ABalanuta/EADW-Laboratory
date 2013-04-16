
from collections import Counter

mySet = set()
myCounter = Counter()
readFile = open("just_text.txt","r")

for linha in readFile:
    string = str(linha)
    parsed = string.split()
    
    # Se array vazio continua para a proxima linha
    if parsed == []:
        continue
    
    cnt = Counter()
    for palavra in parsed:
        cnt[palavra.lower()] += 1
    myCounter += cnt
    #print cnt

print myCounter.most_common(10)
            