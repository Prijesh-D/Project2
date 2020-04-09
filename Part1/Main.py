# Prijesh Dholaria
# CS 435 Section 6
# Question 3

import random
from Graph import Graph
from GraphSearch import GraphSearch
class Main:
        def createRandomUnweightedGraph(n):
            graph = Graph()
            numbers = list(range(n))
            for number in numbers:
                graph.addNode(num)
            nodelist = graph.getAllNodes():
            for node in nodelist:
                indexatnode=nodelist.index(node)
                randomNum = random.randInt(0, indexatnode)
                randomNum2 =random.randInt(1, n//2)
                randomNumUse = randomNum // randomNum2
                for num in randomNumUse:
                    graph.addUndirectedEdge(node, num)
            
            return graph
        
        def createLinkedList(n):
            graph = Graph()
            numbers = list(range(n))
            lengthNumbers = len(numbers) -1;
            for number in numbers:
                graph.addNode(num)
            
            for number in range(0, lengthNumbers):
                graph.addUndirectedEdge(numbers[number], numbers[number+1])
            
            return graph
        
        def BFTRecLinkedList(graph):
            return GraphSearch.BFTRec(graph)
        
        def BFTIterLinkedList(graph):
            return GraphSearch.BFTIter(graph)
            
            