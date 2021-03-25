import numpy as np

#logical operation

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5])
    b = .7
    if np.sum(w*x) + b > 0:
        return 1
    else:
        return 0

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-.5, -.5])
    b = .7
    if np.sum(w*x) + b > 0:
        return 1
    else:
        return 0

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5])
    b = -.2
    if np.sum(w*x) + b > 0:
        return 1
    else:
        return 0

#non-linear
def XOR(x1, x2):
    return AND(NAND(x1,x2), OR(x1,x2))

for x1 in range(2):
    for x2 in range(2):
        print("AND (",x1,",",x2,") :",AND(x1,x2))
        print("NAND (",x1,",",x2,") :",NAND(x1,x2))
        print("OR (",x1,",",x2,") :",OR(x1,x2))
        print("XOR (",x1,",",x2,") :",XOR(x1,x2))