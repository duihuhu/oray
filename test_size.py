import numpy as np
def dircle():
    return np.zeros(10000000)
    #return np.zeros(100000)

a = dircle
with open("buffer.txt", 'r') as fd:
    fd.write(a);