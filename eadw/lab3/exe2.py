from whoosh.index import open_dir
from whoosh.qparser import QueryParser, OrGroup
#from exe1 import index_toDir


#index_toDir()
def search_Word_in_Index(word):
    ixD = open_dir("indexDir")
    with ixD.searcher() as searcher:
        query = QueryParser("content", ixD.schema, group=OrGroup).parse(word.decode())
        #results = searcher.search(query, limit=None)
        results = searcher.search(query)
        returnList = list()
        for r in results:
            returnList.append(str(r.fields().values()[0]))
        return set(returnList)
    
print search_Word_in_Index("Are there abnormalities of taste in CF patients?")