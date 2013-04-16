import numpy as np
from numpy import linalg

def lregression (X,y):
    l = len(y)
    A = np.vstack([np.array(X).T, np.ones(l)])
    return linalg.lstsq(A.T, y)[0]

X = [(0,3), (2,3), (2.5,3.6), (4,4.8)]
y = [7.3, 8.6, 8.5, 9.0]
w = lregression(X,y)
print w

X2 = []
Y2 = []

print X

filename = "aula05_features.txt"
fd = file(filename, "r")
for line in fd:
    split = line.split()
    tuplo = (float(split[0]), float(split[1]), float(split[2]))
    X2.append(tuplo)
    Y2 += split[3]

w2 = lregression(X2,Y2)
print w2
    
