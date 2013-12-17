PageRank 
======

For a University exam on numerical methods for Markov chains, I had to read and make an oral report on two articles on PageRank algorithms, on the [inner-outer iteration method](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.8204) and [fast sampling method](http://link.springer.com/article/10.1007%2Fs10115-013-0691-1)

This repository contains my python implementation of some of those algorithms, which I made to make some quick tests.

I tested the programs with the  graphs from the "Social network" sections from  [http://snap.stanford.edu/data/index.html](http://snap.stanford.edu/data/index.html) and the [Harvard500 graph](http://www.cise.ufl.edu/research/sparse/matrices/MathWorks/Harvard500.html) (from which you have to manually remove the first lines) 

Example:

	python readandsavegraph.py wiki-Vote.txt wiki float64
	python comparetimes.py wiki
	python plotresidues.py wiki


