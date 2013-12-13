PageRank 
======

I implemented some algorithms in python (with numpy) to compute the PageRank of a web graph. There's the classic power iteration method and the inner-outer iteration method proposed by [Gleich, Gray, Greif, Lau](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.8204)

I tested the programs with graphs from the "Social network" and "Web graphs" sections from  [http://snap.stanford.edu/data/index.html](http://snap.stanford.edu/data/index.html)

Example:

	python readandsavegraph.py wiki-Vote.txt wiki.npy float64
	python pow.py wiki.npy residues


