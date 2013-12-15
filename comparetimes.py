#import numpy as np
import timeit
import sys

#matrix = "wiki-vote.npy"
matrix = sys.argv[1]
n = 10

setup_code="""
from pow import pow
from innerouter import innerouter
import numpy as np
P = np.load("%s")
""" % matrix

timepow = timeit.timeit('x,res = pow(P)', setup=setup_code, number=n)
timeinout = timeit.timeit('x,res = innerouter(P)', setup=setup_code, number=n)

print "Average time over %d trials, with matrix %s:" % (n,matrix)
print "%20s %7f" % ("Power Method", timepow/float(n))
print "%20s %7f" % ("Inner Outer", timeinout/float(n))
#print "%10s" % "Power Method"
