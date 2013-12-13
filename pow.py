import numpy as np
import matplotlib.pyplot as plt
import sys

def usage(name):
    print "Applies power method to PageRank problem. You have to supply the P matrix as a .npy file and an outfile to write residues"
    print "USAGE: python {0} pmatrix.npy outfile".format(name)

def pow(P,outfile,alpha=0.85,tol=1.e-5,maxiter=300):
    file = open(outfile,'w')
    n = float(P.shape[0])
    b = (1-alpha)*(1/n)*np.ones(n)
    x = (np.ones(n)/n)
    res = np.array([1.0])
    iter = 0
    while res[-1] > tol and iter < maxiter:
        dot = P.dot(x)
        y = alpha*dot

        y = y + b
        y = y/np.linalg.norm(y)
        res = np.append(res,np.linalg.norm(x-y))
        x = y
        iter += 1
        
    np.savetxt(file,res)
    file.close()

if __name__ == "__main__":
    try:
        P = np.load(sys.argv[1])
        pow(P,sys.argv[2])
        exit
    except:
        usage(sys.argv[0])
