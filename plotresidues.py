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
#resdirsample = np.loadtxt(basename+"-dirsample-residues")
plt.plot(respow,'.g', resinout, '.r')
plt.yscale('log')
plt.legend(('power method','inner-outer', 'direct sampling'))
#plt.text(20.0,-1.0,'Residues',fontsize=24)#, bbox=dict(edgecolor = 'black', facecolor='white'))
plt.suptitle(r'Residues for $\alpha = %.2f$' % a,y=0.8,fontsize=24)
plt.show()
