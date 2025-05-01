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
"""
각 노드의 경로를 동적 배열로 표현하는 것
list[]
1: 2,3,4
2: 1,3
3: .......
위와 같이 표현함
"""

class ADLnode:
    def __init__(self, value):
        self.value = value
        self.path = []

class adjecencyList:
    def __init__(self):
        self.nodes = []

    def addNode(self, node: ADLnode):
        self.nodes.append(node)

    def addPath(self, here: ADLnode, there: ADLnode):
        for i in range(len(self.nodes)):
            if self.nodes[i] == here:
                self.nodes[i].path.append(there)
                return
        print("no such node")

    def printList(self):
        for i in range(len(self.nodes)):
            print(f"val: {self.nodes[i].value}")
            print("-paths")
            for j in range(len(self.nodes[i].path)):
                print(f"{self.nodes[i].path[j].value}")


if __name__ =="__main__":
    # lst = ["miku","teto","rin"]
    # vocaro = Graph(lst)
    # print(vocaro.nodes[1].value)

    # #미쿠에서 테토로 가는 길을 만들고 그 가중치를 1로 하겠다
    # vocaro.nodes[0].addPath(path(vocaro.nodes[1],1))
    # print(vocaro.nodes[0].path[0].weight)

    # fir = graphNode('서울')
    # sec = graphNode('대전')
    # thr = graphNode('세종')

    # fir.addPath(path(sec,1))
    # fir.addPath(path(thr,3))
    # sec.addPath(path(thr,2))

    # print(fir.path[0].weight)
    # print(fir.path[1].weight)
    # print(sec.path[0].weight)

    # ajg = adjecencyGraph(3)
    # ajg.addWeightedPath(1,2,1)
    # ajg.addWeightedPath(2,3,2)
    # ajg.addWeightedPath(1,3,3)

    adl = adjecencyList()

    miku = ADLnode("miku")
    teto = ADLnode("teto")
    rin = ADLnode("rin")

    adl.addNode(miku)
    adl.addNode(teto)
    adl.addNode(rin)

    adl.addPath(miku,teto)
    adl.addPath(teto,miku)
    adl.addPath(miku,rin)
    adl.printList()