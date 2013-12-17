import numpy as np
import sys
import Queue
import scipy.sparse
import pow
from readandsavegraph import load_graph

def usage(name):
    print "Applies adaptive sampling to PageRank problem; you have to supply the basename for the matrix files. Two outfiles will be produced, one for the residue (ASCII) and one for the approximated solution (.npy)"
    print "USAGE: python {0} basename".format(name)

def direct_c(a,K):
    ret = 0
    for i in range(K):
        ret += a**i
    return ret/float(K)

def normalize_columns(A):
    n = float(A.shape[0])
    deg = np.zeros(n)
    ret = A
    for key in A.keys():
        deg[key[1]] += A[key]
    for j in range(len(deg)):
        if deg[j] > 0:
            for i in range(int(n)):
                ret[i,j] *= 1/deg[j]
    return ret

def sample1(A,c):#,theta):
    q = Queue.PriorityQueue()
    z = 0
    n = float(A.shape[0])
    theta = ((8*np.log(n))**2)/np.sqrt(n)
    N = len(A.nonzero()[0])
    s = N/(c**2)
    for key in A.keys():
        i,j = key
        z += (A[i,j])**2
        r = np.random.uniform()
        k = np.max([s*((A[i,j])**2)/r,s*((A[i,j])**2)/((theta*r)**2)])
        q.put((k,key))
        g = q.get()
        while g[0] <= z:
            g = q.get()
        if g[0] > z:
            q.put(g)

    ret = scipy.sparse.dok_matrix((n,n),dtype=A.dtype)
    while q.empty() == False:
        g = q.get()
        key = g[1]
        ret[key] = A[key]
    return ret

def sample2(A,c):
    n = float(A.shape[0])
    N = len(A.nonzero()[0])
    s = N/(c**2)
    theta = 1e-3
    #theta = ((8*np.log(n))**2)/np.sqrt(n)
    ret = scipy.sparse.dok_matrix((n,n),dtype=A.dtype)
    fnorm = 0
    for key in A.keys():
        fnorm += (A[key])**2
    eps = (theta*fnorm)/np.sqrt(s)
    for key in A.keys():
        if A[key] > eps:
            p = np.min([1,(s*(A[key]**2))/(fnorm**2)])
        else:
            p = np.min([1,A[key]/eps])
        rand = np.random.binomial(1,p)
        ret[key] = rand*A[key]/p
    #ret = normalize_columns(ret)
    return ret

def direct_sample(P,d,c=direct_c(np.sqrt(2),50),alpha=0.85,tol=1.e-3,maxiter=300):
    P = sample2(P,c)
    x,res = pow.pow(P,d,alpha,tol,maxiter)
    return x,res

#def adap
if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage(sys.argv[0])
        sys.exit(1)
    else:
        P,dvec = load_graph(sys.argv[1])
        x,res = direct_sample(P,dvec)
        np.savetxt(sys.argv[1]+"-dirsample-residues",res)
        np.save(sys.argv[1]+"-dirsample-solution",x)

