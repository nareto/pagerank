import numpy as np
import sys

def usage(name):
    print "Applies power method to PageRank problem. You have to supply the P matrix as a .npy file and two outfiles, one for the residue (ASCII) and one for the approximated solution (.npy)"
    print "USAGE: python {0} pmatrix.npy residue_file x_file.npy".format(name)

def pow(P,alpha=0.85,tol=1.e-7,maxiter=300):
    n = float(P.shape[0])
    b = (1-alpha)*(1/n)*np.ones(n)
    x = (np.ones(n)/n)
    res = np.array([1.0])
    iter = 0
    while res[-1] > tol and iter < maxiter:
        y = (alpha*P.dot(x)) + b
        #y = y/np.linalg.norm(y,1)
        res = np.append(res,np.linalg.norm(x-y))
        x = y
        iter += 1
    return x,res[1:]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage(sys.argv[0])
        exit
    else:
        P = np.load(sys.argv[1])
        x,res = pow(P)
        np.savetxt(sys.argv[2],res)
        np.save(sys.argv[3],x)

