#!/usr/bin/env python3

import time
from collections import defaultdict

class AnEdge():
	def __init__(self, tail, head, weight):
		self.t = tail
		self.h = head
		self.w = weight

	def __lt__(self, other):
		return self.weight() < other.weight()

	def __repr__(self):
		return "edge from %s to %s with weight %s" % (self.t, self.h, self.w)
    
	def get_tail(self):
		return self.t

	def get_head(self):
		return self.h

	def get_weight(self):
		return self.w

class WeightedDirectedGraph():
    def __init__(self, nr_vs):
        self.nr_vs = nr_vs #number of vertices
        self.nr_es = 0 #number of edges
        self.es = defaultdict(set) #dictionary of sets that, for every vertex, stores edges leaving it

    def show_nr_vs(self):
        return self.nr_vs

    def show_nr_es(self):
        return self.nr_es

    def add_edge(self, e):
        v = e.get_tail()
        (self.es[v]).add(e)
        self.nr_es += 1

    def get_edges(self, v):
        return self.es[v]

    def removeEdge(self, e):
        v = e.get_tail()
        (self.es[v]).remove(e)
        self.nr_es -= 1

    def display_graph(self):
        for t in self.es:
            for e in self.es[t]:
                print(e)

#def run_Floyd_Warshall(graph):
    #set up the base case

if __name__ == "__main__":
    file_name =  'APSPtest1.txt'
    
    start = time.time()

    with open(file_name, 'r') as f:
        nr_vs, nr_es = f.readline().strip().split()
        nr_vs, nr_es = int(nr_vs), int(nr_es)
        graph = WeightedDirectedGraph(nr_vs)

        for line in f:
            t, h, w = line.strip().split()
            t, h, w = int(t)-1, int(h)-1, int(w)
            e = AnEdge(t,h,w)
            graph.add_edge(e)

    end = time.time()
    print(end - start)
