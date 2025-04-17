class Graph:
    def __init__(self,lst: list):
        self.nodes= []
        for i in range(len(lst)):
            self.nodes.append(graphNode(lst[i]))
    

class graphNode:
    def __init__(self, value):
        self.value = value
        self.path = []
        self.weight = []

    def addPath(self,node: 'path'):
        self.path.append(node)

class path:
    def __init__(self,node: graphNode, wei):
        self.wayTo = node
        self.weight = wei

class adjecencyGraph:
    def __init__(self, nodes):
        self.matrix = [["infinite" for _ in range(nodes)] for _ in range(nodes)]

    def addWeightedPath(self,col,row,weight):
        self.matrix[col][row]=weight
    def printMat(self):
        for idx in enumerate(self.matrix):



            print(f"{idx}")

#다음시간 -> 인접리스트

if __name__ =="__main__":
    lst = ["miku","teto","rin"]
    vocaro = Graph(lst)
    print(vocaro.nodes[1].value)

    #미쿠에서 테토로 가는 길을 만들고 그 가중치를 1로 하겠다
    vocaro.nodes[0].addPath(path(vocaro.nodes[1],1))
    print(vocaro.nodes[0].path[0].weight)

    fir = graphNode('서울')
    sec = graphNode('대전')
    thr = graphNode('세종')

    fir.addPath(path(sec,1))
    fir.addPath(path(thr,3))
    sec.addPath(path(thr,2))

    print(fir.path[0].weight)
    print(fir.path[1].weight)
    print(sec.path[0].weight)

    ajg = adjecencyGraph(3)
    ajg.addWeightedPath(1,2,1)
    ajg.addWeightedPath(2,3,2)
    ajg.addWeightedPath(1,3,3)
