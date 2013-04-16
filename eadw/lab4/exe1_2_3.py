from PageRank import PageRank
from MyWoosh import MyWoosh
from collections import Counter

searchQuery = "red"
mixedResult = Counter()
pg = PageRank("aula04_links.txt", 0.1)
mw = MyWoosh("aula03_cfc.txt")

#mw.createIndex()
print "Converged in ", pg.runUntilConvergence(), "Iterations"

search = mw.searchWord(searchQuery)
for doc in search.viewkeys():
    mixedResult += Counter({doc : search[doc] * pg.getScoreOfDocument(doc)*pg.numVertices})

print mixedResult.most_common(5)