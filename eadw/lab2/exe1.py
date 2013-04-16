from collections import Counter
import re

 
def read_file(nome_ficheiro):

    #Cria FD
    fileDesc = open(nome_ficheiro, "r")
    tuplo = []
    bookTitle = 0
    
    for book in fileDesc:
        parsed = re.split('\W+', book)
        counter = Counter()
    
        for word in parsed:
            if not word is '':
                counter[word.lower()] += 1
        
        campo = ["Document"+str(bookTitle), counter]
        #print campo
        tuplo.append(campo)
        bookTitle += 1
    #fecha FD
    fileDesc.close()
    return tuplo


def createInvertedIndex(tuplo):
    
    index = []
    processed = set()
    
    for campo in tuplo:
        book_name = campo[0]
        
        for word, times in campo[1].items():
            
            if word in processed:# ja existe
                for index_tmp in index:
                    if index_tmp[0] == word:
                        index_tmp[1] += Counter({book_name: times})
                        
            else: # ainda nao existe
                campo_de_Index = [word, Counter({book_name: times})]
                index.append(campo_de_Index)
                processed.add(word)         
    return index, processed



#doc_name = "aula02_documents.txt"
#tuplo = read_file(doc_name)
#index = createInvertedIndex(tuplo)
#print index

