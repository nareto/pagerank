PageRank 
======

For a University exam on numerical methods for Markov chains, I had to read and make an oral report on two articles on PageRank algorithms, on the [inner-outer iteration method](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.8204) and [fast sampling method](http://link.springer.com/article/10.1007%2Fs10115-013-0691-1). 

This repository contains my python implementation of some of those algorithms, which I made to make some quick tests. Unfortunately I was not able to get the sampling methods to work - the sampling function is not working as expected (so the `fastsample.py` file is to be considered broken). Also the Gauss-Seidel method (`gs.py`) is really slow: I used `scipy.sparse.csr_matrix` to store the matrixes, and it works very well for methods that require many matrix x vector products, but very poorly with the Gauss-Seidel method that needs to make lots of accesses to single matrix elements.

I tested the programs with the web graphs from  [http://snap.stanford.edu/data/index.html](http://snap.stanford.edu/data/index.html) and the much smaller [Harvard500 graph](http://www.cise.ufl.edu/research/sparse/matrices/MathWorks/Harvard500.html) (from which you have to manually remove the first lines) 

Example:

	python readandsavegraph.py wiki-Vote.txt wiki float64
	python pow.py wiki
	python innerouter.py wiki
	python plotresidues.py wiki


