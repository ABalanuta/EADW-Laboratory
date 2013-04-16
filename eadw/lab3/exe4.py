from exe3 import preRecF1
from exe2 import search_Word_in_Index

filename = "aula03_queries.txt"
fd = open(filename, "r")

lineNumber = 0
queryString = ""

sumPre = 0.0
sumRec = 0.0
sumF1 = 0.0



for line in fd:
    
    #filtras as preguntas 
    if lineNumber % 2 == 0:
        queryString = line.splitlines()[0]
    
    else:
        print queryString
        set_relevent_doc = set(line.split())
        set_of_docs = search_Word_in_Index(queryString)
        
        PRF = preRecF1(set_of_docs, set_relevent_doc)
        sumPre += PRF[0]
        sumRec += PRF[1]
        sumF1 += PRF[2]
        print "Precission:", PRF[0], " Recall: ", PRF[1]," F1:", PRF[2], "\n"
        
    
    lineNumber += 1
    
print "avgPrecission:", sumPre/((lineNumber-1)/2), " avgRecall: ", sumRec/((lineNumber-1)/2)," avgF1:", sumF1/((lineNumber-1)/2), "\n"
