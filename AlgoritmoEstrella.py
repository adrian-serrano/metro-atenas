 # -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:11:39 2020

@author: Grupo 26
"""

import Atenas as atn
import operator


class AlgoritmoEstrella:
    def __init__(self, origin, destiny):
        """Constructor of the algorithm."""
        self.grafo = atn.AthensMetro()
        
        self.transfers = 0
        
        self.opened = []   #List that contains the opened vertexes.
        self.closed =  []   #List that contains the closed vertexes.
        self.origin = self.grafo.metro.getVertex(origin)
        self.destiny = self.grafo.metro.getVertex(destiny)
        
        
    def apply(self):
        """Method that applies the A* algorithm."""
        first = NodeInfo(self.origin,-1,0)
        self.opened.append((0,first)) #It's a tuple the checkPosition and the NodeInfo.
        
        """While there are elements to be iterated:"""
        while self.opened:
            """The first element is taken and removed from the opened list."""
            actual = self.opened.pop(0)
            actualV = actual[1].vertex
            actual= actual[1]
            
            """If it's the objective, it's added to the closed list and it's finished."""
            if actualV is self.destiny or self.stopTransfers(actualV) :
                self.closed.append(actual)
                break
            
            """It iterates over the neighbours of the actual node."""
            for neighbour in actualV.getNeighbours():
                newCost = actual.cost + actualV.getCost(neighbour) #The new cost is calculated (Acumulated cost + edgeCost).
                
                
                """It's checked if it's already in closed or opened."""
                isInsideC,index = self.isInside(neighbour,1)
                isInsideO,index = self.isInside(neighbour,0)
                
                """If it's not inside closed and it's not inside opened or it's inside opened but the cost is better."""
                if (not isInsideO  or newCost < self.opened[index][1].cost) and not isInsideC:
                    
                    """The cost + the heuristic determines how the nodes will be checked."""
                    checkPosition = newCost + self.calculateH(actualV,neighbour)
                    
                    """It it's already in nodes, it just modifies the existing element."""
                    if isInsideO:
                        neighbour = self.modifyNode(self.opened,index, self.opened[index][1], actualV, newCost)
                        self.opened.pop(index) #The previous node is removed.
                        
                    else:
                        neighbour = NodeInfo(neighbour,actualV,newCost)
                        
                    self.opened.append((checkPosition,neighbour))
                    
                    "The list it's sorted so the lower the checkPosition the sooner they will be analyzed."
                    self.opened.sort(key = operator.itemgetter(0))
                    
            self.closed.append(actual)
        
        return self.closed
    
    
    def calculateH(self,actual,candidate):
        """Method that gets the h(n) parameter."""
        x = candidate.coordinates[0]-self.destiny.coordinates[0] #X coordinates difference.
        y = candidate.coordinates[1]-self.destiny.coordinates[1] #Y coordinates difference.       
        return (abs(x) + abs(y))
    
    
    def isInside(self,node,indicator):
        """Checks if the node belongs to opened (0) or to closed (1) and returns the index."""
        encontrado = False
        indexI = -1
        if indicator == 0:
            for key in (self.opened): 
                index = self.opened.index(key)
                if node is self.opened[index][1].vertex :
                    encontrado =  True
                    indexI = index
                    break
        else:
            for key in (self.closed): 
                index = self.closed.index(key)
                if node is self.closed[index].vertex :
                    encontrado =  True
                    indexI = index
                    break

        return (encontrado,indexI)
    
        
    def modifyNode(self,array,index,node,comesFrom,cost):
        """Method that modifies the node in the list."""
        node.modify(node.vertex,comesFrom,cost)
        return node
       
    def stopTransfers(self,actual):
        """Method that stops if the destiny is a transfer and the actual is the other part of the same transfer."""
        if self.destiny.id == "Attiki1" or self.destiny.id == "Attiki2":
            if actual.id == "Attiki1" or actual.id == "Attiki2":
                return True;
            
        if self.destiny.id == "Omonia1" or self.destiny.id == "Omonia2":
            if actual.id == "Omonia1" or actual.id == "Omonia2":
                return True;
            
        if self.destiny.id == "Syntagma2" or self.destiny.id == "Syntagma3":
            if actual.id == "Syntagma2" or actual.id == "Syntagma3":
                return True;
            
        if self.destiny.id == "Monastiraki1" or self.destiny.id == "Monastiraki3":
            if actual.id == "Monastiraki1" or actual.id == "Monastiraki3":
                return True;
            
    def getSolution(self):
        """Method that gives the path of the solution."""
        path = []
        time = 0
        transfers = 0
        
        current = self.closed[len(self.closed)-1]
        
        path.insert(0, current.vertex)
        time = current.cost

        while current.comesFrom != -1:
            parent = current.comesFrom
            
            """If the actual line is not the same as the previous line."""
            if current.vertex.line != parent.line:
                    transfers = transfers + 1
                    
            index = self.getSolutionIndex(parent)
            current = self.closed[index]
            path.insert(0, parent)
        return path,time,transfers
    
    def getSolutionIndex(self,previous):
        """It returns the index of the NodeInfo in closed whose node is the comesFrom of the actual one."""
        index = 0
        for node in self.closed:
            if previous is node.vertex:
                break
            index = index + 1
        return index
                
        
    def convertSolution(self):
        """Conversion of the solution to readeble format."""
        solution,time,transfers = self.getSolution()
        path = ""        
        for i in range (len(solution)):
            estacion = "   • Parada " + str(i+1) + ": " + str(solution[i].id)
            path = path + estacion + "\n"
        
        return path,transfers,time
        
        
"""Auxiliar class. It contains all the necessary information
    for the algorithm to work properly."""
class NodeInfo:
    def __init__(self,node,comesFrom,cost):
        """Constructor of the nodes."""
        self.vertex = node
        self.comesFrom = comesFrom
        self.cost = cost
        
    def modify(self,node,comesFrom,cost):
        """Method that modifies a node."""
        self.vertex = node
        self.comesFrom = comesFrom
        self.cost = cost