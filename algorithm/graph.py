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
"""
0515 수업
"""

#prim's Algorithm
"""
시작점 설정
인접 노드들 방문, 이외의 노드 가중치는 무한
"""

def prim(G, V):
    pass

#kruskal's Algorithm
"""
가중치가 낮은 엣지들을 n-1번 선택하겠다
그런데 엣지를 선택 했을때 같은 집합내의 요소끼리 연결되면 삭제하겠다 <- 이 과정의 복잡도가 문제
"""
#Topological Sortig Algorithm
"""
어떤 그래프에 대해
진입간선이 없는 정점을 선택(u) <-이거 어떻게 찾을건데...?
    -진입간선 없는 정점 리스트를 따로 만들어두자 (교재 425p) FAT(file allocation table)과 유사
u의 진출간선과 자신을 제거한다
"""
#최단경로
"""
모든 노드를 방문하는 가장 짧은 경로들을 찾는다?
    하나의 시작점(소스)에서 하나의 목적지 -> 이건 자명한 이야기라 따로 다루지 않음
    하나의 시작점에서 다수의 목적지 -> 지금 할거
    모든 시작점에서 다수의 목적지 ->슈타이너 트리 문제(그냥 ㅈㄴ 어려운거니까 지금은 안할거임) np완비문제
간선 가중치 조건이 다르다
가중치가 음수가 아닐때: 다익스트라
음수인 가중치가 있을때: 벨만-포드 (음의 사이클은 허용하지 않음)

음수 가중치가 가지는 의미
무조건 방문해야 할 노드가 있을때: 가중치가 음수이면 무조건 방문하게 된다
"""
#Dijstra's Shortest Path Algorithm

#Bellman-Ford Shortest Path Algorithm
"""
다익스트라에서 음의 사이클 확인하는 부분 추가만 한건가?
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