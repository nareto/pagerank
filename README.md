PageRank 
======

For a University exam on numerical methods for Markov chains, I implemented some algorithms in python (with numpy) to compute the PageRank of a web graph. There's the classic power iteration method and the inner-outer iteration method proposed by [Gleich, Gray, Greif, Lau](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.8204)

I tested the programs with the  graphs from the "Social network" sections from  [http://snap.stanford.edu/data/index.html](http://snap.stanford.edu/data/index.html) and the [Harvard500 graph](http://www.cise.ufl.edu/research/sparse/matrices/MathWorks/Harvard500.html) (from which you have to manually remove the first lines) 

Example:

	python readandsavegraph.py wiki-Vote.txt wiki.npy float64
	python comparetimes.py wiki.npy
	python plotresidues.py wiki.npy


