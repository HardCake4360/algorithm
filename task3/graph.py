import math
import heapq

def G(V, E): 
    AdjM = [ [ math.inf for _ in range(len(V))] for _ in range(len(V)) ]
    for (row, col), weight in E:    
        AdjM[row-1][col-1] = weight
        AdjM[col-1][row-1] = weight
    return AdjM

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
    
# Prim's algorithm
def Prim( V, E, r):
    AdjM = G(V, E)
    
    S = [ 0 for _ in range(len(V))] #방문한 정점
    P = [ None for _ in range(len(V))] #부모 리스트
    W = [ math.inf for _ in range(len(V))] #가중치
    W[r-1] = 0 #시작 지점이므로 가중치 0으로 설정
    Q = [] #최소 힙
    
    #준비 과정
    for col in range(len(W)): 
        if col != r-1 and AdjM[r-1][col] != math.inf: #현재 순회 정점이 시작 정점이 아님 && 시작 정점의 인접들의 가중치가 무한이 아님
            W[col] = AdjM[r-1][col] #인접 정점의 가중치 기록
            P[col] = r #부모 설정
    for i in range(len(W)):
        if i+1 == r: continue #시작지점은 스킵
        heapq.heappush( Q, (W[i], i+1) ) #Q에 튜플 형식으로 (가중치, 정점번호) 삽입
    S[r-1] = 1
    
    #탐색 시작
    while len(Q) > 0: #큐가 빌 떄까지 반복
        weight, u = heapq.heappop(Q) #가중치가 가장 작은 정점 POP 
        print(f"extract {u} with weight {weight}")
        S[u-1] = 1 #방문 정점에 추가
        for v in range(len(V)): #정점 수 만큼 순회
            if v == r-1: continue #시작 정점 스킵
            print(f"adj {v+1} with weight {AdjM[u-1][v]} comparing {W[v]}")
            if S[v] == 0 and AdjM[u-1][v] < W[v]:  #아직 방문하지 않음 && 인접 정점의 가중치가 순회 정점보다 작음
                Q.remove( (W[v], v+1)) #Q에서 순회 정점 제거
                W[v] = AdjM[u-1][v] #순회 정점의 가중치 정상화화
                heapq.heappush(Q, (W[v], v+1)) #정상화된 가중치로 재삽입
                P[v] = u #부모 설정정
    print(W)
    print(P)
    
#kruskal's Algorithm
"""
가중치가 낮은 엣지들을 n-1번 선택하겠다
그런데 엣지를 선택 했을때 같은 집합내의 요소끼리 연결되면 삭제하겠다 <- 이 과정의 복잡도가 문제
"""

def kruskal(V, E):
    adjM = G(V, E)
    T = []
    Q = [{w, e} for e,w in E]
    heapq.heapify(Q)
    
    while len(T) < len(V)-1:
        weight,(u,v) = heapq.heappop(Q)
        if True: #u, v가 다른 집합일때
            T.append((u,v)) #추가할 때 2차원 배열로 알맞는 집합에 추가해야할지도?
            #u, v가 속한 집합을 합친다

#Topological Sortig Algorithm
"""
어떤 그래프에 대해
진입간선이 없는 정점을 선택(u) <-이거 어떻게 찾을건데...?
    -진입간선 없는 정점 리스트를 따로 만들어두자 (교재 425p) FAT(file allocation table)과 유사
u의 진출간선과 자신을 제거한다
"""

def topological(V, E):
    lst = [] #위상정렬한 정점들의 리스트트
    noneIncomingV = V
    
    while len(lst)<len(V):
        #진입간선이 없는 정점 리스트 만드는 부분
        for u,v in E:
            if v in noneIncomingV:
                noneIncomingV.remove(v)
        #위에서 만든 리스트 이용해 pop하는 부분
        while noneIncomingV:
            u = noneIncomingV.pop()
            lst.append(u)
            V.pop(u)
            

#최단경로
"""
모든 노드를 방문하는 가장 짧은 경로들을 찾는다?
    하나의 시작점(소스)에서 하나의 목적지 -> 이건 자명한 이야기라 따로 다루지 않음
    하나의 시작점에서 다수의 목적지 -> 지금 할거
    모든 시작점에서 다수의 목적지 ->슈타이너 트리 문제(어려운거니까 지금은 안할거임) np완비문제
간선 가중치 조건이 다르다
가중치가 음수가 아닐때: 다익스트라
음수인 가중치가 있을때: 벨만-포드 (음의 사이클은 허용하지 않음)

음수 가중치가 가지는 의미
무조건 방문해야 할 노드가 있을때: 가중치가 음수이면 무조건 방문하게 된다
"""
#Dijstra's Shortest Path Algorithm

def dijstra(V, E, r): #r: 시작 정점
    adjM = G(V,E)
    
    

#Bellman-Ford Shortest Path Algorithm
"""
다익스트라에서 음의 사이클 확인하는 부분 추가만 한건가?
"""
def bellmanFord(V, E):
    pass
    
    
if __name__ == "__main__":
    V = [ i+1 for i in range(7)]
    print(V)

    E = [ ((1, 2), 8), ((2, 3), 10), ((1, 4), 9), ((4, 3),5), ((1, 5), 11), ((5, 4), 13), ((4,7), 12), ((5, 6), 8), ((6, 7), 7) ]
    
    Prim(V, E, 1)
    kruskal(V, E)
    
    
    
    
