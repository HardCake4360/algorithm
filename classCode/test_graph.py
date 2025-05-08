import math
"""
        서울 -> 세종, 용인
        용인 -> 세종, 청주
        세종 -> 대전, 서울
        청주 -> 용인, 대전
        대전 -> 서울
"""
INF = float('inf')

class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.link = None
        
    def addNeighbor(self, neighbor : 'City', weight: int):
        self.neighbors.append( {"neighbor":neighbor, "weight": weight} )
        return self
        
    def getNeighbors(self):
        return self.neighbors
    
    def __str__(self):
        return f"{self.name} -> " + ','.join( [ f"{nw['neighbor'].name, nw['weight']}" for nw in self.neighbors ])

if __name__ == "__main__":

    cities = [City("서울"), City("용인"), City("세종"), City("청주"), City("대전")]
    [seoul, yongin, sejong, chungju, daejeon] = cities
    
    seoul.addNeighbor(sejong, 15).addNeighbor(yongin, 10 )
    yongin.addNeighbor(sejong, 7).addNeighbor(chungju, 5)
    sejong.addNeighbor(daejeon, 8).addNeighbor(seoul, 15)
    chungju.addNeighbor(yongin, 6).addNeighbor(daejeon, 3)
    daejeon.addNeighbor(seoul, 30)
    
    for city in cities:
        print(city)
        
    rows, cols = len(cities), len(cities)
    adjancencyMatrix = [ [ 0 for _ in range(cols)] for _ in range(rows)]
    for i, city in enumerate(cities):
        neighbors = city.getNeighbors()
        for neighbor in neighbors:
            adjancencyMatrix[i][cities.index(neighbor["neighbor"])] = neighbor["weight"]
    
    print(adjancencyMatrix)
    

    
    
    
    
    
    