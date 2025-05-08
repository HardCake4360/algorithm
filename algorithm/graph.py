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
경로를 링크드 리스트로 표현하느냐 배열로 표현하느냐에 따라 갈림
인접배열에서는 또 해시테이블을 이용하여 탐색시간 개선 가능
"""
############인접배열 구현############
class ADLnode:
    def __init__(self, value):
        self.value = value
        self.path = []

class adjecencyList:
    def __init__(self,lst: list):
        self.nodes = lst

    def addNode(self, node: ADLnode):
        self.nodes.append(node)

    def addPath(self, here, there: ADLnode):
        for i in range(len(self.nodes)):
            if self.nodes[i].value == here:
                self.nodes[i].path.append(there)
                return
        print("no such node")

    def printList(self):
        for i in range(len(self.nodes)):
            print(f"val: {self.nodes[i].value}")
            print("-paths")
            for j in range(len(self.nodes[i].path)):
                print(f"{self.nodes[i].path[j].value}")

#####################################

"""
0501수업 서문
다이나믹 프로그래밍 알면 좋겠다
알고리즘 응용까지 알면 좋은데 시간이 없어서 방법론적인 부분만 짚고 넘어가겠다
하반기에는 다양한 문제의 풀이 방법과 그 근간이 되는 원리에 대해 배워볼 것
"""

"""
0508 수업내용
실습 진행: 만들면서 발생하는 문제들에 집중할 것
-무향 인접 행렬
-
"""

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

    adl = adjecencyList([ADLnode("0"),ADLnode("1"),ADLnode("2"),ADLnode("3"),ADLnode("4"),ADLnode("5")])

    adl.addPath("0","1")
    adl.addPath("0","2")
    adl.addPath("1","2")
    adl.printList()