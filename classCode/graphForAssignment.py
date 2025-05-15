import math
import heapq

# adjacenyMatrix

V = [ i+1 for i in range(8)]

E = [ (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (3, 5), (4, 6), (4, 7), (6,7), (6, 8), (7, 8)]

print(V)

AdjM = [ [ math.inf for _ in range(len(V))] for _ in range(len(V)) ]
for row, col in E:    
    AdjM[row-1][col-1] = 1
    AdjM[col-1][row-1] = 1
    
print(AdjM)

# AdjacencyArray

AdjA = [ [] for _ in range(len(V))]
for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)

print(AdjA)

# buildPath
def buildPath(parent: list, dest):
    path = [dest]
    current = dest
    while parent[current-1] != -1:
        path.append(parent[current-1])
        current = parent[current-1]
    path.reverse()
    return path

# BFS
def BFS(V, AdjA, s, d: int = None):
    parent = [ -1 for _ in range(len(V))]
    Tree = [ [] for _ in range(len(V))]
    visited = [ False for _ in range(len(V))]
    Q = [s]
    visited[s-1] = True
    while len(Q) > 0:
        current = Q.pop(0)
        for neighbor in AdjA[current-1]:
            if visited[neighbor-1] == False:
                visited[neighbor-1] = True
                Q.append(neighbor)
                if d: 
                    parent[neighbor-1] = current
                print(f"visited {current}->{neighbor}")
                Tree[current-1].append(neighbor)
            if neighbor == d:
                path = buildPath(parent, d)
                return path
    if d:
        return None
    return Tree


# DFS
def DFS(visited, AdjA, node, source):
    if visited[node-1] == False:
        print(f"visiting {node} from {source}")
        visited[node-1] = True
        for neighbor in AdjA[node-1]:
            DFS(visited, AdjA, neighbor, node)
    else:
        #print(f"visited already {node} from {source}")
        pass

# DFSMain
def DFSMain(V, AdjA, s):
    visited = [ False for _ in range(len(V))]
    DFS(visited, AdjA, s, None)
    
#############################################################################
#prim's Algorithm

def prim(G, s, E): #입력: 그래프(인접 행렬), 시작 정점, 간선
    MST = [] #최소신장트리를 위한 간선들의 리스트
    minQ = [] #가중치 비교를 위한 최소힙
    visited = [] #방문정점

    visited.append(s)
    current = s
    #s와 인접한 간선을 큐에 추가
    for i in range(len(G[current])):
        if G[current][i] == math.inf: continue
        minQ.append((G[current][i],(current,i)))
    heapq.heapify(minQ)
    
    while minQ and len(visited) < len(G):
        minEdge = heapq.heappop(minQ)
        w ,(u,v) = minEdge #w: 가중치, u: 시작정점, v: 도착정점(필요한 것)
        
        if v in visited: continue
        



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

if __name__ == "__main__":
    print(AdjA)
    path = DFSMain(V, AdjA, 1)
    print(path)
    
    prim(AdjM, 1, E)
    
