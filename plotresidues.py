import matplotlib.pyplot as plt
import numpy as np
from pow import pow
from innerouter import innerouter
from readandsavegraph import load_graph
import sys

basename = sys.argv[1]
a = 0.85

##compute everytime the methods
#P,d=load_graph(basename)
#xpow,respow = pow(P,d,alpha=a)
#xinout,resinout = innerouter(P,d,alpha = a)

#or better load residue vector from previous computtation
respow = np.loadtxt(basename+"-pow-residues")
resinout = np.loadtxt(basename+"-inout-residues")
resio2pi = np.loadtxt(basename+"-inoutpi-residues")
resgs = np.loadtxt(basename+"-gs-residues")
plt.plot(respow,'-g.', resinout, '-r.', resgs, '-b.', resio2pi, '-k.')
#plt.plot(respow,'.g-', resinout, '-r.', resio2pi, '-k.')
#plt.legend(('power method','inner-outer', 'inner-outer switch to pi'))
plt.legend(('power method','inner-outer', 'Gauss-Seidel', 'inner-outer switch to pi'))
plt.yscale('log')
#plt.text(20.0,-1.0,'Residues',fontsize=24)#, bbox=dict(edgecolor = 'black', facecolor='white'))
#plt.suptitle(r'Residues for $\alpha = %.2f$' % a,y=0.8,fontsize=24)
#plt.show()
plt.savefig(basename+"-plot.png", format='png')
