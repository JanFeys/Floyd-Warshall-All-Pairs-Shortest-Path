#!/usr/bin/env python3

import time
from collections import defaultdict
import sys

class WeightedDirectedGraph():
    def __init__(self, nr_vs):
        self.nr_vs = nr_vs #number of vertices
        self.es = defaultdict(set) #dictionary of sets that, for every vertex, stores tails of edges leaving it
        self.ws = dict() #dictionary that stores weight of each edge

    def show_nr_vs(self):
        return self.nr_vs

    def show_nr_es(self):
        return self.nr_es

    def add_edge(self, t, h, w):
        (self.es[t]).add(h)
        self.ws[(t,h)] = w

    def get_edges(self, t):
        return self.es[t]
    
    def get_weight(self,t,h):
        return self.ws[(t,h)]

    def removeEdge(self, t, h):
        (self.es[t]).remove(h)
        del self.ws[(t,h)]

    def display(self):
        nr_es_present = 0
        for t in self.es:
            for h in self.es[t]:
                print("edge from %s to %s with weight %s" % (t, h, self.ws[(t,h)]))
                nr_es_present += 1
        print("there are %s edges in total" % nr_es_present)

    def run_Floyd_Warshall(self):
        self.A = [[[0 for k in range(self.nr_vs)] for i in range(self.nr_vs)] for j in range(self.nr_vs)]
    
        #set up the base case
        for t in range(self.nr_vs):
            for h in range(self.nr_vs):
                if (t == h):
                    pass
                else:
                    if (h in self.es[t]):
                        self.A[t][h][0] = self.ws[(t,h)]
                    else:
                        self.A[t][h][0] = sys.maxsize

        #now iterate
        for k in range(1,self.nr_vs):
            print("at present k= ", k, "of ", self.nr_vs)
            for t in range(self.nr_vs):
                for h in range(self.nr_vs):
                    self.A[t][h][k]=min(self.A[t][h][k-1],self.A[t][k][k-1]+self.A[k][h][k-1])

        for t in range(0,self.nr_vs):
            if (self.A[t][t][self.nr_vs-1] < 0):
                print("there is a negative cycle!")
                quit()

        return self.A[:][:][self.nr_vs-1]

if __name__ == "__main__":
    file_name =  'APSPsimpletest1.txt'
    
    start = time.time()

    with open(file_name, 'r') as f:
        nr_vs, nr_es = f.readline().strip().split()
        nr_vs, nr_es = int(nr_vs), int(nr_es)
        graph = WeightedDirectedGraph(nr_vs)

        for line in f:
            t, h, w = line.strip().split()
            t, h, w = int(t)-1, int(h)-1, int(w)
            graph.add_edge(t,h,w)

    shortest_paths = graph.run_Floyd_Warshall()

    for t in range(nr_vs):
        for h in range(nr_vs):
            print("from %s to %s shortest path is %s" % (t, h, shortest_paths[t][h]))

    end = time.time()
    print(end - start)
