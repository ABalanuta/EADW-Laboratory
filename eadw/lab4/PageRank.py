from collections import defaultdict, Counter

class PageRank:
    
    graphFilePath = ""
    damping_factor = 0.1
    inverseGraph = defaultdict(list)
    verticePointsAt = defaultdict(list)
    numVertices = 0
    prValues = Counter()
    
    #Inicializa o objecto
    def __init__(self, graphFilePath, dampingFactor):
        self.graphFilePath = graphFilePath
        self.damping_factor = dampingFactor
        self.__createInvertedGraph()
        self.numVertices = len(self.inverseGraph.keys())
        self.__initPageRank()
    
    #Cria o Grfo Inverso    
    def __createInvertedGraph(self):
        fd = open(self.graphFilePath, "r")
        for line in fd:
            subline = line.split()
            
            vertice = subline[0]
            subline = subline[1:]
            
            # referencia para quantos documentos que aponta
            self.verticePointsAt[vertice].append(len(subline))
            #print vertice, "point at ", len(subline), "because subline is ", subline   
            
            if len(subline) > 0:
                for v in subline:
                    self.inverseGraph[v].append(vertice)
        fd.close()
    
    def __initPageRank(self):
        for k in self.inverseGraph.keys():
            self.prValues[k] = 1.0 / self.numVertices
    
    def runOnce(self):
        
        # os novos valores de PR
        rPRValues = Counter()
        
        for doc in self.prValues.keys():
            
            #print "For Node", doc
            #o novo score deste documento
            newDocScore = 0.0
            
            # somar as pars partes dos docs que apontam para este
            for pointer in self.inverseGraph[doc]:
                pointerPointsAtNdocs = self.verticePointsAt[pointer][0]
                #print "pointer", pointer, "points at ", verticePointsAt[pointer][0], "files"
                newDocScore += float(self.prValues[pointer]) / float(pointerPointsAtNdocs)
                #print "newdocScore=",newDocScore
                
            #print "New RAW score is", newDocScore
            # acrescendando o damping factor
            rPRValues[doc] = float(1 - self.damping_factor)/len(self.verticePointsAt) + float(self.damping_factor * newDocScore)
        return rPRValues

    def setPR(self, prValues):
        self.prValues = prValues
    
    def getPR(self):
        return self.prValues

    def __equal(self, CountA, CountB):
        for key in CountA:
            if(not(CountA.get(key) == CountB.get(key))):
                return -1
        return 0

    def runUntilConvergence(self):
        
        pr1 = self.prValues
        pr2 = self.runOnce()
        iteration = 1
        
        while self.__equal(pr1, pr2) == -1:
            self.setPR(pr2)
            pr1 = pr2
            pr2 = self.runOnce()
            iteration += 1
        return iteration
    
    def getScoreOfDocument(self, docNumber):
        return self.prValues[docNumber]



