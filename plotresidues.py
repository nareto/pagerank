import matplotlib.pyplot as plt
import numpy as np
from pow import pow
from innerouter import innerouter
import sys

matrix = sys.argv[1]
a = 0.85
P=np.load(matrix)
xpow,respow = pow(P, alpha=a)
xinout,resinout = innerouter(P, alpha = a)

plt.plot(respow,'.g', resinout, '.r')
plt.yscale('log')
plt.legend(('power method','inner-outer'))
#plt.text(20.0,-1.0,'Residues',fontsize=24)#, bbox=dict(edgecolor = 'black', facecolor='white'))
plt.suptitle(r'Residues for $\alpha = %.2f$' % a,y=0.8,fontsize=24)
plt.show()
