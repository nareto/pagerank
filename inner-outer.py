import numpy as np
import sys

def usage(name):
    print "Applies inner-outer iteration method to PageRank problem. You have to supply the P matrix as a .npy file and an outfile to write residues"
    print "USAGE: python {0} pmatrix.npy outfile".format(name)

def innerouter(P,outfile,alpha=0.85,beta=0.6,outtol=1.e-6,intol=1.e-3,maxiter=300):
    file = open(outfile,'w')
    n = float(P.shape[0])
    v = (1/n)*np.ones(n)
    b = (1-alpha)*v
    res = np.array([1.0])
    x = v
    z = x
    y = P.dot(x)
    iter = 0
    while res[-1] > outtol and iter < maxiter:
        f = (alpha - beta)*y + b
        x = f + beta*y
        y = P.dot(x)
        while np.linalg.norm(f + beta*y - x, 1) > intol:
            x = f + beta*y
            y = P.dot(x)
        res = np.append(res,np.linalg.norm(x-z))
        z = x
        iter += 1

    np.savetxt(file,res[1:])
    file.close()

if __name__ == "__main__":
    try:
        P = np.load(sys.argv[1])
        innerouter(P,sys.argv[2])
        exit
    except:
        usage(sys.argv[0])
