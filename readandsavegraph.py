import numpy as np
import sys

def usage(name):
    print "This program reads a txt file rappresenting a graph in arch form, i.e. with lines"
    print "A  B"
    print "if there's an arch from node A to B, and saves the associated matrix as a numpy array with type as datatype"
    print ""
    print "USAGE: python {0} graph.txt matrix.npy float64".format(name)

def read_graph(inpath, outpath, type="float64"):
    infile = open(inpath,'r')
    outfile = open(outpath, 'w')
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
    P = np.zeros((n,n)).astype(type)
    infile.seek(0)
    for i in range(comments - 1):
        infile.readline()
    for str_line in infile:
        str_line = str_line.split()
        P[int(str_line[1]) - 1][int(str_line[0]) - 1] = 1.0
    infile.close()

    deg = np.zeros(n)
    for j in range(int(n)):
        deg[j] = P[:,j].sum()
        if deg[j] == 0:
            P[:,j] = (1/n)*np.ones(n)
        else:
            P[:,j] = (1/deg[j])*P[:,j]
    
    np.save(outfile,P)
    outfile.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage(sys.argv[0])
        exit        
    else:
        read_graph(sys.argv[1], sys.argv[2], sys.argv[3])
