#!/usr/bin/env python3

import time
from collections import defaultdict
import sys

class WeightedDirectedGraph():
    def __init__(self, nr_vs):
        self.nr_vs = nr_vs #number of vertices
        self.es = defaultdict(set) #dictionary of sets that, for every vertex, stores head of edges leaving it
        self.ws = dict() #dictionary that stores weight of each edge

    def show_nr_vs(self):
        return self.nr_vs

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
        self.A = [[0 for t in range(self.nr_vs)] for h in range(self.nr_vs)]
    
        #set up the base case
        for t in range(self.nr_vs):
            for h in range(self.nr_vs):
                if (t == h):
                    pass
                else:
                    if (h in self.es[t]):
                        self.A[t][h] = self.ws[(t,h)]
                    else:
                        self.A[t][h] = sys.maxsize

        #now iterate
        for k in range(1,self.nr_vs):
            self.B = self.A[:][:]
            for t in range(self.nr_vs):
                for h in range(self.nr_vs):
                    self.A[t][h]=min(self.B[t][h],self.B[t][k]+self.B[k][h]) #idea: use numpy and broadcasting

        for t in range(0,self.nr_vs):
            if (self.A[t][t] < 0):
                print("there is a negative cycle!")
                quit()

        return self.A[:][:]

if __name__ == "__main__":
    file_name =  'APSPtest3.txt'

    start = time.time()

    with open(file_name, 'r') as f:
        nr_vs, _ = f.readline().strip().split()
        nr_vs = int(nr_vs)
        graph = WeightedDirectedGraph(nr_vs)

        for line in f:
            t, h, w = line.strip().split()
            t, h, w = int(t)-1, int(h)-1, int(w)
            graph.add_edge(t,h,w)

    shortest_paths = graph.run_Floyd_Warshall()

    for t in range(nr_vs):
        for h in range(nr_vs):
            print("from %s to %s shortest path is %s" % (t, h, shortest_paths[t][h]))

    print("minimum is", min(min(shortest_paths)))
    end = time.time()
    print(end - start)
