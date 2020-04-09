# Prijesh Dholaria
# CS 435 Section 6
# Question 3



from Graph import Graph
from queue import Queue

class GraphSearch:
    def _init_(self):
        pass
    
    def DFSRec(self, nodeStart, nodeEnd):
        visitedListNode=[];
        
        if nodeStart!=nodeEnd:
            HelperDFSRec(nodeStart, nodeEnd, visitedListNode)
            
        return visitedListNode;
        
    def HelperDFSRec(self, nodeStart, nodeEnd, visitedListNode):
        visitedListNode.append(nodeStart)
        if nodeStart==nodeEnd
            return visitedListNode;
            neighbors = nodeStart.partners
            while neighbors:
                nodesLeft=[]
                for node in neighbors:
                    if node not in visitedListNode:
                        nodesLeft.append(node)
                if nodesLeft:
                    visitedListNode=self.HelperDFSRec(nodesLeft[0], nodeEnd, visitedListNode)
                
                else: 
                    return visited
    
    def DFSIter(self, startNode, endNode):
        stackList = []
        visitedListNode = []
        
        stackList.append(startNode)
        visitedListNode.append(startNode)
        stackLength = len(stackList)
        while stackLength > 0:
            currentNode = stackList.pop()
            
            if currentNode == endNode:
                return visitedListNode
            
            for neighbor in currentNode.partners:
                if neighbor not in visitedListNode:
                    stackList.append(neighbor)
                    visitedListNode.append(neighbor);
        
        return None
        
    def HelperBFSRec(self, currentNode, visitedListpath):
        currentneighbors = currentNode.partners
        for node in  currentneighbors:
            if node not in visitedListpath:
                visitedListpath.append(node)
                visitedListpath=self.HelperBFSRec(node, visitedListpath)
        return path
        
    def BFSRec(self, graph):
        visitedListpath = []
        nodelist = graph.getAllNodes()
        for node in nodelist:
            if node not in visitedListpath:
                visitedListpath=self.HelperBFSRec(node, visitedListpath)
        return visitedListpath
        
    def BFSIter(self, graph):
        queueList = []
        visitedListNode = []
        nodelist = graph.getAllNodes()
        for node in nodelist:
            if node not in visited:
                visitedListNode.append(node)
                queueList.append(node)
            queueLength = len(queueList)
            while queueLength > 0:
                currentNode = queueList.pop(0)
                neighbors = currentNode.partners
                for neighborNode in neighbors:
                    if neighborNode not in visitedListNode:
                        queueList.append(neighborNode)
                        visitedListNode.append(neighborNode)
        return visitedListNode

        
        
                    