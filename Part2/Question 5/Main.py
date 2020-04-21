# Prijesh Dholaria
# CS 435 Section 6
# Question 5



import random
from WeightedGraph import WeightedGraph

class Main:
    def createRandomCompleteWeightedGraph(n):
        graph = WeightedGraph()
        lst = []
        for num in range(n):
            randomNum = random.randint(0, n);
            if randomNum not in lst:
                lst.append(randomNum)
                graph.addNode(num)
        nodelist = graph.getAllNodes()
        for node in nodelist:
            for node2 in range(n):
                if node != node2:
                    randomWeight = random.randint(1, (n*n))
                    graph.addWeightedEdge(node, node2, randomWeight)
        
        return graph
        
    def createLinkedList(n):
        graph = WeightedGraph()
        for newNode in range(0, n)
            graph.addNode(newNode)
        nodelist = graph.getAllNodes()
        nodelistlength = len(nodelist)
        for num in range(nodelistlength-1):
            graph.addWeightedEdge(nodelist[num], nodelist[num+1], 1)
        return graph
    
    def dijkstras(start):
        startnode = start
        distanceDict = dict()
        distanceDict[startnode] = 0
        visited = list()
        values=[]
        while startnode is not None and startnode in distanceDict:
            visited.append(startnode)
            for adjNode in startnode.adjacentList:
                if adjNode in visited:
                    continue
                m[adjNode] = min([distanceDict[startnode]+startnode.adjacentList[adjNode], distanceDict[adjNode])
            
            for node in distanceDict:
                if node in visited:
                    continue
                distance=500
                if distanceDict < distance:
                    distance = distanceDict[node]
                    startnode = node
        for node in distanceDict:
                values[node.nodeValue] = distanceDict[node]
        return values;
                    
        
        
            
            
