# Prijesh Dholaria
# CS 435 Section 6
# Question 3

class Node:
    def _init_(self, name):
        self.nodeName = name
        self.partners = []

class Graph:
    def _init_(self):
        self.nodeList = []
    
    def addNode(self, nodeName):
        self.nodeList.append(self.Node(nodeName))
    
    def addUndirectedEdge(self, first, second):
        first.partners.append(second)
        second.partners.append(first)
        
    def removeUndirectedEdge(self, first,second):
        first.partners.remove(second)
        second.partners.remove(first)
    
    def getAllNodes(self):
        return self.nodeList