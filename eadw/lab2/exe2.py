from exe1 import createInvertedIndex, read_file
from collections import Counter

doc_name = "aula02_documents.txt"
tuplo = read_file(doc_name)
invertedIndex, inverted_set = createInvertedIndex(tuplo)


total_number_of_documents = len(tuplo)
print "The total number of documents is " + str(total_number_of_documents)

totalCounter = Counter()
for value in tuplo:
    totalCounter += value[1]
print "The total number of terms is "+ str(len(totalCounter))

individualTerms = 0
for item in totalCounter.items():
    if item[1] == 1:
        individualTerms += 1;
print "The total number of individual terms is " + str(individualTerms)

print "Search Word? :"
search_word =  raw_input()
relevant_doc = Counter()
if search_word in inverted_set:
    for values in invertedIndex:
        if values[0] == search_word:
            relevant_doc = values[1]
print "Document frequency (DF) of word " + "[" + search_word + "] is : "
for doc, times in relevant_doc.items():
    print "In ", doc, " apears ", times, "times"
    
