# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:17:55 2020

@author: Grupo 26
"""

class Graph:
    def __init__(self):
        """Graph constructor, initializes numVertexes to 0 and vertexes as empty."""
        self.vertexes = {}
        self.numVertexes = 0
    
    def __iter__(self):
        """"Returns an iterable of the vertexes."""
        return iter(self.vertexes.values())
    
    def addVertex(self,node,coordinates,line):
        """Method that adds a given vertex to the graph."""
        newVertex = Vertex(node,coordinates,line)
        self.vertexes[node] = newVertex
        self.numVertexes = self.numVertexes +1
        return newVertex
    
    def getVertex (self, vertex):
        """Method that returns the node if it's in the list."""
        if vertex in self.vertexes:
            return self.vertexes[vertex]
        else:
            return None
    
    def addEdge(self,origin,destiny,cost):
        """Method that adds an edge between to nodes. The nodes should be neighbours."""
        self.vertexes[origin].addNeighbour(self.vertexes[destiny], cost) #If transfer = 0, not a transfer.
        self.vertexes[destiny].addNeighbour(self.vertexes[origin], cost) #If transfer = 1, a transfer.
        
        
class Vertex:
    def __init__(self,node,coordinates,line):
        """Vertex constructor, initializes the node id to the name, the 
        frequency to the given one and neighbours as empty."""
        self.id = node
        self.coordinates = coordinates
        self.neighbours = {}
        self.line = line
    
    def addNeighbour(self,neighbour,cost):
        """Methdo that adds a neighbour to the vertex with a cost. The nodes should be neighbours."""
        self.neighbours[neighbour] = cost
         
    def getNeighbours(self):
        """"Method that returns the neighbours of the vertex."""
        return self.neighbours.keys()
     
    def getCost(self,neighbour):
        """Method that returns the cost of a neighbour node."""
        return self.neighbours[neighbour]
    
    

class AthensMetro:
    def __init__(self):
        """Graph constructor, initializes numVertexes to 0 and vertexes as empty."""
        self.metro = Graph()
        self.createMetro()
        
    def createMetro(self):
        """Method that adds the metro stations to the metro graph and links them."""
        
        """Creation."""
        """Line 1."""
        """Line 1."""
        Kifissia = self.metro.addVertex("Kifissia", [1, 24], 1)
        Kat = self.metro.addVertex("KAT", [3, 23], 1)
        Marousi = self.metro.addVertex("Maroussi", [5, 22], 1)
        Neratziotissa = self.metro.addVertex("Neratziotissa", [8, 20], 1)
        Irini = self.metro.addVertex("Irini", [8, 18], 1)
        Irakleio = self.metro.addVertex("Iraklio", [8, 16], 1)
        NeaIonia = self.metro.addVertex("Nea Ionia", [9, 15], 1)
        Pefkakia = self.metro.addVertex("Pefkakia", [10, 14], 1)
        Perissos = self.metro.addVertex("Perissos", [11, 13], 1)
        AnoPatissia = self.metro.addVertex("Ano Patissia", [12, 12], 1)
        AgiosEleftherios = self.metro.addVertex("Agios Eleftherios", [12, 11], 1)
        KatoPatissia = self.metro.addVertex("Kato Patissia", [13, 10], 1)
        AghnosNikoloos = self.metro.addVertex("Agios Nikolaos", [14, 9], 1)
        Attiki1 = self.metro.addVertex("Attiki1", [15, 9], 1)
        Victoria = self.metro.addVertex("Victoria", [19, 12], 1)
        Omonia1 = self.metro.addVertex("Omonia1", [22, 12], 1)
        Monastiraki1 = self.metro.addVertex("Monastiraki1", [25, 12], 1)
        Thissio = self.metro.addVertex("Thissio", [28, 12], 1)
        Petrolona = self.metro.addVertex("Petralona", [31, 12], 1)
        Tavros = self.metro.addVertex("Tavros", [33, 10], 1)
        Kollithea = self.metro.addVertex("Kallithea", [35, 8], 1)
        Moschato = self.metro.addVertex("Moschato", [37, 6], 1)
        Farilo = self.metro.addVertex("Farilo", [39, 4], 1)
        Piraeus = self.metro.addVertex("Piraeus", [39, 1], 1)
        
        """Line 2."""
        AgiosAntonios = self.metro.addVertex("Agios Antonios", [10, 4], 2)
        Sepolia = self.metro.addVertex("Sepolia", [13, 6], 2)
        Attiki2 = self.metro.addVertex("Attiki2", [16, 9], 2)
        LarissaStation = self.metro.addVertex("Larissa Station", [19, 9], 2)
        Metaxourghio = self.metro.addVertex("Metaxourghio", [22, 9], 2)
        Omonia2 = self.metro.addVertex("Omonia2", [22, 12], 2)
        Panepistimio = self.metro.addVertex("Panepistimio", [23, 13], 2)
        Syntagma2 = self.metro.addVertex("Syntagma2", [25, 14], 2)
        Akropoli = self.metro.addVertex("Akropoli", [28, 14], 2)
        SyngrouFix = self.metro.addVertex("Sygrou - Fix", [31, 13], 2)
        NeosKosmos = self.metro.addVertex("Neos Kosmos", [34, 13], 2)
        AgiosIoannis = self.metro.addVertex("Agios Ioannis", [37, 13], 2)
        Dafni = self.metro.addVertex("Dafni", [40, 13], 2)
        AgiosDimitrios = self.metro.addVertex("Agios Dimitrios", [43, 13], 2)
        
        """Line 3."""
        Egaleo = self.metro.addVertex("Egaleo", [25, 1], 3)
        Eleonas = self.metro.addVertex("Eleonas", [21, 3], 3)
        Keramiekos = self.metro.addVertex("Kerameikos", [24, 6], 3)
        Evangelismos = self.metro.addVertex("Evangelismos", [25, 18], 3)
        MegaroMoussikis = self.metro.addVertex("Megaro Moussikis", [24, 22], 3)
        Ambelokipi = self.metro.addVertex("Ambelokipi", [23, 23], 3)
        Panormou = self.metro.addVertex("Panormou", [22, 24], 3)
        Katehaki = self.metro.addVertex("Katehaki", [21, 25], 3)
        EthnikiAmyna = self.metro.addVertex("Ethniki Amyna", [20, 26], 3)
        Holargos = self.metro.addVertex("Holargos", [19, 27], 3)
        Nomismatokopio = self.metro.addVertex("Nomismatokopio", [18, 28], 3)
        AghiaParaskevi = self.metro.addVertex("Aghia Paraskevi", [17, 29], 3)
        Halandri = self.metro.addVertex("Halandri", [16, 30], 3)
        DoukissisPlakentias = self.metro.addVertex("Doukissis Plakentias", [15, 31], 3)
        Pallini = self.metro.addVertex("Pallini", [18, 32], 3)
        PalaniaKantza = self.metro.addVertex("Palania - Kantza", [22, 32], 3)
        Koropi = self.metro.addVertex("Koropi", [26, 32], 3)
        Airport = self.metro.addVertex("Airport", [27, 25], 3)
        Syntagma3 = self.metro.addVertex("Syntagma3", [25, 14], 3)
        Monastiraki3 = self.metro.addVertex("Monastiraki3", [25, 12], 3)

        
        """Linking."""
        """Line 1."""
        self.metro.addEdge(Kifissia.id, Kat.id, 120)
        self.metro.addEdge(Kat.id,Kifissia.id, 120)
        
        self.metro.addEdge(Kat.id, Marousi.id, 120)
        self.metro.addEdge(Marousi.id, Kat.id,  120)
        
        self.metro.addEdge(Marousi.id, Neratziotissa.id, 180)
        self.metro.addEdge(Neratziotissa.id,Marousi.id, 180)
        
        self.metro.addEdge(Neratziotissa.id, Irini.id, 120)
        self.metro.addEdge(Irini.id, Neratziotissa.id, 120)
        
        self.metro.addEdge(Irini.id, Irakleio.id, 180)
        self.metro.addEdge(Irakleio.id, Irini.id,  180)
        
        self.metro.addEdge(Irakleio.id, NeaIonia.id, 120)
        self.metro.addEdge(NeaIonia.id, Irakleio.id,  120)
        
        self.metro.addEdge(NeaIonia.id, Pefkakia.id, 120)
        self.metro.addEdge(Pefkakia.id, NeaIonia.id,  120)
        
        self.metro.addEdge(Pefkakia.id, Perissos.id, 60)
        self.metro.addEdge(Perissos.id, Pefkakia.id,  60)
        
        self.metro.addEdge(Perissos.id, AnoPatissia.id, 180)
        self.metro.addEdge(AnoPatissia.id, Perissos.id,  180)

        self.metro.addEdge(AnoPatissia.id, AgiosEleftherios.id, 60)
        self.metro.addEdge(AgiosEleftherios.id, AnoPatissia.id,  60)
        
        self.metro.addEdge(AgiosEleftherios.id, KatoPatissia.id, 120)
        self.metro.addEdge(KatoPatissia.id, AgiosEleftherios.id, 120)
        
        self.metro.addEdge(KatoPatissia.id, AghnosNikoloos.id, 120)
        self.metro.addEdge(AghnosNikoloos.id, KatoPatissia.id, 120)
        
        self.metro.addEdge(AghnosNikoloos.id, Attiki1.id, 120)
        self.metro.addEdge(Attiki1.id, AghnosNikoloos.id,  120)
        
        self.metro.addEdge(Attiki1.id, Victoria.id, 180)
        self.metro.addEdge(Victoria.id, Attiki1.id,  180)
        
        self.metro.addEdge(Victoria.id, Omonia1.id, 120)
        self.metro.addEdge(Omonia1.id, Victoria.id, 120)
        
        self.metro.addEdge(Omonia1.id, Monastiraki1.id, 120)
        self.metro.addEdge(Monastiraki1.id, Omonia1.id,  120)
        
        self.metro.addEdge(Monastiraki1.id, Thissio.id, 120)
        self.metro.addEdge(Thissio.id, Monastiraki1.id,  120)
        
        self.metro.addEdge(Thissio.id, Petrolona.id, 120)
        self.metro.addEdge(Petrolona.id, Thissio.id, 120)
        
        self.metro.addEdge(Petrolona.id, Tavros.id, 120)
        self.metro.addEdge(Tavros.id, Petrolona.id, 120)
        
        self.metro.addEdge(Tavros.id, Kollithea.id, 120)
        self.metro.addEdge(Kollithea.id, Tavros.id,  120)
        
        self.metro.addEdge(Kollithea.id, Moschato.id, 120)
        self.metro.addEdge(Moschato.id, Kollithea.id,  120)
        
        self.metro.addEdge(Moschato.id, Farilo.id, 180)
        self.metro.addEdge(Farilo.id, Moschato.id, 180)
        
        self.metro.addEdge(Farilo.id, Piraeus.id, 240)
        self.metro.addEdge(Piraeus.id, Farilo.id,  240)
        
        
        """Line 2."""
        self.metro.addEdge(AgiosAntonios.id, Sepolia.id, 60)
        self.metro.addEdge(Sepolia.id,AgiosAntonios.id, 60)
        
        self.metro.addEdge(Sepolia.id, Attiki2.id, 60)
        self.metro.addEdge(Attiki2.id,Sepolia.id, 60)
        
        self.metro.addEdge(Attiki2.id, LarissaStation.id, 60)
        self.metro.addEdge(LarissaStation.id,Attiki2.id, 60)
        
        self.metro.addEdge(LarissaStation.id, Metaxourghio.id, 60)
        self.metro.addEdge(Metaxourghio.id,LarissaStation.id, 60)
        
        self.metro.addEdge(Metaxourghio.id, Omonia2.id, 60)
        self.metro.addEdge(Omonia2.id,Metaxourghio.id, 60)
        
        self.metro.addEdge(Omonia2.id, Panepistimio.id, 60)
        self.metro.addEdge(Panepistimio.id,Omonia2.id, 60)
        
        self.metro.addEdge(Panepistimio.id, Syntagma2.id, 60)
        self.metro.addEdge(Syntagma2.id,Panepistimio.id, 60)
        
        self.metro.addEdge(Syntagma2.id, Akropoli.id, 60)
        self.metro.addEdge(Akropoli.id,Syntagma2.id, 60)
        
        self.metro.addEdge(Akropoli.id, SyngrouFix.id, 60)
        self.metro.addEdge(SyngrouFix.id,Akropoli.id, 60)
        
        self.metro.addEdge(SyngrouFix.id, NeosKosmos.id, 60)
        self.metro.addEdge(NeosKosmos.id,SyngrouFix.id, 60)
        
        self.metro.addEdge(NeosKosmos.id, AgiosIoannis.id, 60)
        self.metro.addEdge(AgiosIoannis.id,NeosKosmos.id, 60)
        
        self.metro.addEdge(AgiosIoannis.id, Dafni.id, 60)
        self.metro.addEdge(Dafni.id,AgiosIoannis.id, 60)
        
        self.metro.addEdge(Dafni.id, AgiosDimitrios.id, 60)
        self.metro.addEdge(AgiosDimitrios.id,Dafni.id, 60)

        
        """Line 3."""
        self.metro.addEdge(Egaleo.id, Eleonas.id, 180)
        self.metro.addEdge(Eleonas.id, Egaleo.id, 180)
        
        self.metro.addEdge(Eleonas.id, Keramiekos.id, 120)
        self.metro.addEdge(Keramiekos.id, Eleonas.id, 120)
        
        self.metro.addEdge(Keramiekos.id, Monastiraki3.id, 180)
        self.metro.addEdge(Monastiraki3.id, Keramiekos.id, 180)
        
        self.metro.addEdge(Monastiraki3.id, Syntagma3.id, 120)
        self.metro.addEdge(Syntagma3.id, Monastiraki3.id, 120)
        
        self.metro.addEdge(Syntagma3.id, Evangelismos.id, 120)
        self.metro.addEdge(Evangelismos.id, Syntagma3.id, 120)
        
        self.metro.addEdge(Evangelismos.id, MegaroMoussikis.id, 60)
        self.metro.addEdge(MegaroMoussikis.id, Evangelismos.id, 60)
        
        self.metro.addEdge(MegaroMoussikis.id, Ambelokipi.id, 60)
        self.metro.addEdge(Ambelokipi.id, MegaroMoussikis.id, 60)
        
        self.metro.addEdge(Ambelokipi.id, Panormou.id, 60)
        self.metro.addEdge(Panormou.id, Ambelokipi.id, 60)
        
        self.metro.addEdge(Panormou.id, Katehaki.id, 60)
        self.metro.addEdge(Katehaki.id, Panormou.id, 60)
        
        self.metro.addEdge(Katehaki.id, EthnikiAmyna.id, 120)
        self.metro.addEdge(EthnikiAmyna.id, Katehaki.id, 120)
        
        self.metro.addEdge(EthnikiAmyna.id, Holargos.id, 60)
        self.metro.addEdge(Holargos.id, EthnikiAmyna.id, 60)

        self.metro.addEdge(Holargos.id, Nomismatokopio.id, 60)
        self.metro.addEdge(Nomismatokopio.id, Holargos.id, 60)
        
        self.metro.addEdge(Nomismatokopio.id, AghiaParaskevi.id, 60)
        self.metro.addEdge(AghiaParaskevi.id, Nomismatokopio.id, 60)
        
        self.metro.addEdge(AghiaParaskevi.id, Halandri.id, 60)
        self.metro.addEdge(Halandri.id, AghiaParaskevi.id, 60)
        
        self.metro.addEdge(Halandri.id, DoukissisPlakentias.id, 60)
        self.metro.addEdge(DoukissisPlakentias.id, Halandri.id, 60)
        
        self.metro.addEdge(DoukissisPlakentias.id, Pallini.id, 180)
        self.metro.addEdge(Pallini.id, DoukissisPlakentias.id, 180)
        
        self.metro.addEdge(Pallini.id, PalaniaKantza.id, 180)
        self.metro.addEdge(PalaniaKantza.id, Pallini.id, 180)
        
        self.metro.addEdge(PalaniaKantza.id, Koropi.id, 360)
        self.metro.addEdge(Koropi.id, PalaniaKantza.id, 360)
        
        self.metro.addEdge(Koropi.id, Airport.id, 360)
        self.metro.addEdge(Airport.id, Koropi.id, 360)

        
        """Transfers."""
        self.metro.addEdge(Omonia1.id,Omonia2.id,120)
        self.metro.addEdge(Omonia2.id,Omonia1.id,180)
        
        self.metro.addEdge(Attiki1.id,Attiki2.id,120)
        self.metro.addEdge(Attiki2.id,Attiki1.id,240)
        
        self.metro.addEdge(Syntagma2.id,Syntagma3.id,180)
        self.metro.addEdge(Syntagma3.id,Syntagma2.id,180)
        
        self.metro.addEdge(Monastiraki1.id,Monastiraki3.id,180)
        self.metro.addEdge(Monastiraki3.id,Monastiraki1.id,180)
    