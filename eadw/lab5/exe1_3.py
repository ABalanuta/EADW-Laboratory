import numpy as np
from numpy import linalg
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import *
from whoosh.query import *
from whoosh import scoring

import string
import re
import sys
import whoosh

def lregression (X, y):
    l = len(y)
    A = np.vstack([np.array(X).T, np.ones(l)])
    return linalg.lstsq(A.T, y)[0]

X = [(0, 3), (2, 3), (2.5, 3.6), (4, 4.8)]
y = [7.3, 8.6, 8.5, 9.0]
w = lregression(X, y)

print w

def fregretion():
    X2 = []
    Y2 = []

    filename = "aula05_features.txt"
    fd = file(filename, "r")
    for line in fd:        
        split = line.split()
        tuplo = (float(split[0]), float(split[1]), float(split[2]))
        X2.append(tuplo)
        Y2 += split[3]
    
    w2 = lregression(X2, Y2)
    print w2

coefs = fregretion()
    


def isOdd(x):
    if x % 2 == 0:
        return False
    else:
        return True



#Criar o Index
schema = Schema(id = NUMERIC(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()
line=u""
 
f = open("aula05_features.txt", "r")
for line in f:
    docid = int(line[0:5])
    line = line [6:]
    writer.add_document(id=docid,content=u""+line)

writer.commit()

queries = open("aula03_queries.txt","r")

bm25 = {}
tf_idf = {}
pagerank = lab4_1.page_rank()

for key in pagerank.keys():
    bm25[key] = 0
    tf_idf[key] = 0

for i, line in enumerate(queries):
    if isOdd(i):
        from whoosh.qparser import QueryParser 
        with ix.searcher(weighting=whoosh.scoring.BM25F()) as searcher:
            doc = re.split('\W+', line)
            query = QueryParser("content", ix.schema,group=OrGroup).parse(u"" + line)
            results = searcher.search(query, limit=None)

            for i, value in enumerate(results):
                bm25[str(value['id'])] = results.score(i)

                
        from whoosh.qparser import QueryParser 
        with ix.searcher(weighting=whoosh.scoring.TF_IDF()) as searcher:
            #doc = re.split('\W+', line)
            query = QueryParser("content", ix.schema,group=OrGroup).parse(u"" + line)
            results = searcher.search(query, limit=None)
            for i, value in enumerate(results):
                tf_idf[str(value['id'])] = results.score(i)
                #print results.score(i) 

        results = {}
        #print bm25
        for key in pagerank.keys():
            results[key] = (bm25[key] * coefs[0] + tf_idf[key] * coefs[1] + pagerank[key] * coefs[2]) + coefs[3]
            
        aux = 0
        print "Results of query %d" % i
        for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse = True):
            print "%s:\t%s" % (key, value)
            aux += 1
            if aux == 10:
                break