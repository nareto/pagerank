#import numpy as np
import timeit
import sys

basename = sys.argv[1]
n = 10

setup_code="""
from pow import pow
from innerouter import innerouter
import numpy as np
from readandsavegraph import load_graph
P,d = load_graph("%s")
""" % basename

timepow = timeit.timeit('x,res = pow(P,d)', setup=setup_code, number=n)
timeinout = timeit.timeit('x,res = innerouter(P,d)', setup=setup_code, number=n)

print "Average time over %d trials, with matrix %s:" % (n,basename)
print "%20s %7f" % ("Power Method", timepow/float(n))
print "%20s %7f" % ("Inner Outer", timeinout/float(n))
#print "%10s" % "Power Method"
