import numpy as np
import sys
from readandsavegraph import load_graph

def usage(name):
    print "Applies power method to PageRank problem; you have to supply the basename for the matrix files. Two outfiles will be produced, one for the residue (ASCII) and one for the approximated solution (.npy)"
    print "USAGE: python {0} basename".format(name)

def pow(P,d,alpha=0.85,tol=1.e-3,maxiter=300):
    n = float(P.shape[0])
    u = np.ones(n,dtype=P.dtype)/n #dangling node vector
    b = (1-alpha)*(1/n)*np.ones(n)
    x = np.ones(n)/n
    res = np.array([1.0])
    iter = 0
    while res[-1] > tol and iter < maxiter:
        y = (alpha*(P.dot(x) + (d.dot(x)*u))) + b
        y = y/np.linalg.norm(y,1)
        res = np.append(res,np.linalg.norm(x-y,1))
        x = np.copy(y)
        iter += 1
        
    return x,res[1:]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage(sys.argv[0])
        sys.exit(1)
    else:
        P,dvec = load_graph(sys.argv[1])
        x,res = pow(P,dvec)
        np.savetxt(sys.argv[1]+"-pow-residues",res)
        np.save(sys.argv[1]+"-pow-solution",x)

