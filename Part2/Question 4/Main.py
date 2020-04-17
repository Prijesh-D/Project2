#Prijesh Dholaria
# CS 435 Section 6
# Question 4

from DirectedGraph import DirectedGraph
import random

class Main
    def createRandomDAGIter(n)
        g = DirectedGraph()
        d = {}
        for num in range (n)
            g.addNode(num)
        
        nodes = g.getAllNodes()
        for node in nodes
            numofNodes = random.randint()
            numsinList= [];
            while len(numsinList)!= numofNodes
                num = random.randint(1, nn)
                if num not in numsinList
                    numsinList.append(num)
                    graph.addDirectedEdge(node, num)
        return g;
                    
        