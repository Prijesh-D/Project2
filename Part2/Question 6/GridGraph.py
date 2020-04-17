#Prijesh Dholaria
# CS 435 Section 6
# Question 6

class GridGraph:
    gridVertex = []
    adjacentList = []
    #define node
    def Node(self, x, y, nodeValue):
        val = nodeValue
        self.x = x
        self.y = y
    #create node and add to grid vertex
    def addGridNode(self, x, y, nodeValue):
        node = self.Node(x, y, nodeValue)
        self.gridVertex.append(node)
    #check if the nodes can be made neighbors by getting their abs value of the coordinates
    def addUndirectedEdge(self, first, second):
        if abs(first.y - second.y) <=1:
            if abs(second.x - first.x) <=1:
                firstlist = []
                secondList = []
                firstList.append(first.val)
                firstList.append(first.x)
                firstList.append(first.y)
                secondList.append(second.val)
                secondList.append(second.x)
                secondList.append(second.y)
                self.adjacentList[second.val].append(firstList)
                self.adjacentList[first.val].append(secondList)
    #check if neighbors, if they are then remove them
    def removeUndirectedEdge(self, first, second):
        if abs(first.y - second.y) <=1:
            if abs(second.x - first.x) <=1:
                self.adjacentList[second.val].remove(firstList)
                self.adjacentList[first.val].remove(secondList)
    #return list of Grids;
    def getAllNodes(self):
        return self.gridVertex