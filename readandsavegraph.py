import numpy as np
import sys
import scipy.sparse

def usage(name):
    print "This program reads a txt file rappresenting a graph in arch form, i.e. with lines"
    print "A  B"
    print "if there's an arch from node A to B, and outputs 3 files, basename-keys.npy basename-values.npy and basename-dvector.npy, where basename must be provided"
    print ""
    print "USAGE: python {0} graph.txt basename float64".format(name)

def load_graph(basename):
    dvec = np.load(basename+"-dvector.npy")
    indices = np.load(basename+"-indices.npy")
    indptr = np.load(basename+"-indptr.npy")
    data = np.load(basename+"-data.npy")
    n = len(dvec)
    P = scipy.sparse.csr_matrix((data, indices, indptr),shape = (n,n), dtype=data[0].dtype)
    return (P,dvec)

def save_graph(inpath, out_basename, type="float64"):
    infile = open(inpath,'r')
    line = "#"
    comments = 0
    while line[0] == "#": #ignore inital comments
        line = infile.readline()
        comments += 1
    #find largest index in the infile, which will be the number of nodes
    line = line.split()
    line = [int(line[0]), int(line[1])]
    for str_line in infile:
        str_line = str_line.split()
        line.append(int(str_line[0]))
        line.append(int(str_line[1]))
	
    n = float(max(line))
    N = int(len(line)/2)
    deg = np.zeros(n)
    row = np.zeros(N)
    col = np.zeros(N)
    data = np.zeros(N)
    #find out degree of every node and build row and col vector
    infile.seek(0)
    for i in range(comments - 1):
        infile.readline()
    iter = 0
    for str_line in infile:
        str_line = str_line.split()
        i = int(str_line[1]) - 1
        j = int(str_line[0]) - 1
        deg[j] += 1
        row[iter] = i
        col[iter] = j
        iter += 1

    #set matrix's element according to outdegree
    infile.seek(0)
    for iter in range(N):
        i = row[iter]
        j = col[iter]
        data[iter] = 1/deg[j]
    infile.close()
    
    P = scipy.sparse.csr_matrix((data,(row,col)),shape=(n,n),dtype=type)

    #the d vector has i component 0 if the i node has 0 outdegree, 1 otherwise
    #we will need the d vector to take care of dangling nodes
    d = [x for x in deg == 0]
    np.save(out_basename.rstrip('.npy')+"-dvector",d)
    np.save(out_basename.rstrip('.npy')+"-data",P.data)
    np.save(out_basename.rstrip('.npy')+"-indices",P.indices)
    np.save(out_basename.rstrip('.npy')+"-indptr",P.indptr)
    return (P,d)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage(sys.argv[0])
        sys.exit(1)
    else:
        save_graph(sys.argv[1], sys.argv[2], sys.argv[3])
