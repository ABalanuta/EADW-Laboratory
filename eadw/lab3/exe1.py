from whoosh.index import create_in
from whoosh.fields import Schema, NUMERIC, TEXT


nome_ficheiro = "aula03_cfc.txt";

def index_toDir():
    schema = Schema(id = NUMERIC(stored=True), content=TEXT)
    ix = create_in("indexDir", schema)
    writer = ix.writer()
    
    fileDesc = open(nome_ficheiro, "r")
    for Line in fileDesc:
        
        
        index = int(Line[0:5])
        text = str(Line[5:]).decode("Latin-1")
        writer.add_document(id=index, content=unicode(text))
        #print index, text
              
    #fecha FD
    fileDesc.close()
    writer.commit()
    print "Imported to Dir"
    
    
index_toDir()