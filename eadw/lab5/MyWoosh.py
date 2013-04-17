from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, NUMERIC, TEXT
from whoosh.qparser import QueryParser, OrGroup
from collections import Counter
import os


class MyWoosh:
    
    fileToIntex = ""
    indexDir = "indexDir"
    
    def __init__(self, fileToIndex):
        self.fileToIntex = fileToIndex


    def __createIndexDir(self):
        if not os.path.exists(self.indexDir):
            os.makedirs(self.indexDir)
            print "Directory Created"
              
                
    def createIndex(self):
        self.__createIndexDir()
        schema = Schema(id=NUMERIC(stored=True), content=TEXT)
        ix = create_in(self.indexDir, schema)
        writer = ix.writer()
        
        fileDesc = open(self.fileToIntex, "r")
        for Line in fileDesc:
            
            index = int(Line[0:5])
            text = str(Line[5:]).decode("Latin-1")
            writer.add_document(id=index, content=unicode(text))
            # print index, text
                  
        # fecha FD
        fileDesc.close()
        writer.commit()
        print "Imported to Dir"
        
        
    def searchWord(self, word):
        ixD = open_dir(self.indexDir)
        with ixD.searcher() as searcher:
            query = QueryParser("content", ixD.schema, group=OrGroup).parse(word.decode())
            # results = searcher.search(query, limit=None)
            results = searcher.search(query, limit=100)
            returnList = Counter()
            for i, r in enumerate(results):
                returnList += Counter({str(r.fields().values()[0]) : results.score(i)})
            return returnList



