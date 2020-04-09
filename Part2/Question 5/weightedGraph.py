# Prijesh Dholaria
# CS 435 Section 6
# Question 5


class Node:
    def _init_(self, val):
        self.nodeValue = val
        self.adjacentList = {}
        
class WeightedGraph:
    def _init_(self):
        self.nodeList = [] 
    
    def addNode(self, value):
        node = Node(value)
        self.nodeList.append(node)
    
    def addWeightedEdge(self, first, second, weight):
        if first in self.nodeList or second in sel.nodeList:
            first.adjacentList[second] = weight
            
    def removeWeightedEdge(self, first, second):
        try:
		del first.adjacentList[second]
	except:
		return
    
    def getAllNodes(self):
        return self.nodeList