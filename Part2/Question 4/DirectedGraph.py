# Prijesh Dholaria
# CS 435 Section 6
# Question 4


class Node:
    def _init_(self, name):
        self.nodeName = name
        self.partners = []

class DirectedGraph:
    def _init_(self):
        self.nodeList = [];
    
    def addNode(self, nodeVal):
        if nodeVal not in nodeList:
            self.nodeList.append(Node(nodeVal))
    
    def addDirectedEdge(self, first, second):
        if first not in second.partners:
            first.partners.append(second)
        else
            return
    
    def removeDirectedEdge(self, first,second):
        if first not in second.partners or second not in first.partners:
            return -1
        first.partners.remove(second);
    
    def getAllNodes():
        return self.nodeList