import numpy as np
import sys
from readandsavegraph import load_graph

def usage(name):
    print "Applies Gauss-Seidel method to PageRank problem; you have to supply the basename for the matrix files. Two outfiles will be produced, one for the residue (ASCII) and one for the approximated solution (.npy)"
    print "USAGE: python {0} basename".format(name)

def gs(P,d,alpha=0.85,tol=1.e-6,maxiter=50):
    n = float(P.shape[0])
    u = np.ones(n,dtype=P.dtype)/n #dangling node vector
    b = (1-alpha)*(1/n)*np.ones(n)
    x = np.ones(n)/n
    y = np.copy(x)
    res = np.array([1.0])
    iter = 0
    while res[-1] > tol and iter < maxiter:
        for i in range(int(n)):
            sum = 0
            for j in range(int(n)):
                if j != i:
                    sum += -y[j]*(alpha*P[i,j] + alpha*u[i]*d[j])
            y[i] = (b[i] - sum)/(1 - alpha*P[i,i] - alpha*u[i]*d[i])
        residue = np.linalg.norm(x-y,1)
        print residue
        res = np.append(res,residue)
        y = y/np.linalg.norm(y,1)
        x = np.copy(y)
        iter += 1
        np.savetxt(sys.argv[1]+"-gs-residues",res)
        np.save(sys.argv[1]+"-gs-solution",x)
    return x,res[1:]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage(sys.argv[0])
        sys.exit(1)
    else:
        P,dvec = load_graph(sys.argv[1])
        x,res = gs(P,dvec)
        #np.savetxt(sys.argv[1]+"-gs-residues",res)
        #np.save(sys.argv[1]+"-gs-solution",x)
