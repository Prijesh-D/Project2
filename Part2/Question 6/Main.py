#Prijesh Dholaria
# CS 435 Section 6
# Question 6
from GridGraph import GridGraph
import random

class Main:
    def createRandomGridGraph(n):
        graph = GridGraph()
        node = 0;
        for newX in range(n):
            for newY in range(n):
                graph.addGridNode(newX,newY,node);
                node= node+1
        
        nodelist = graph.getAllNodes()
        for x in nodelist:
            for y in nodelist:
                if random.randint(0,1) is 0:
                    graph.addUndirectedEdge(x, y)
        
        return graph