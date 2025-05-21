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
    W[r] = 0 #시작 지점이므로 가중치 0으로 설정
    Q = [] #최소 힙
    
    #준비 과정
    for col in range(len(W)): 
        if col != r and AdjM[r][col] != math.inf: #현재 순회 정점이 시작 정점이 아님 && 시작 정점의 인접들의 가중치가 무한이 아님
            W[col] = AdjM[r][col] #인접 정점의 가중치 기록
            P[col] = r #부모 설정
    for i in range(len(W)):
        if i == r: continue #시작지점은 스킵
        heapq.heappush( Q, (W[i], i) ) #Q에 튜플 형식으로 (가중치, 정점번호) 삽입
    S[r] = 1
    
    #탐색 시작
    while len(Q) > 0: #큐가 빌 떄까지 반복
        weight, u = heapq.heappop(Q) #가중치가 가장 작은 정점 POP 
        print(f"extract {u} with weight {weight}")
        S[u] = 1 #방문 정점에 추가
        for v in range(len(V)): #정점 수 만큼 순회
            if v == r: continue #시작 정점 스킵
            print(f"adj {v} with weight {AdjM[u][v]} comparing {W[v]}")
            if S[v] == 0 and AdjM[u][v] < W[v]:  #아직 방문하지 않음 && 인접 정점의 가중치가 순회 정점보다 작음
                Q.remove( (W[v], v)) #Q에서 순회 정점 제거
                W[v] = AdjM[u][v] #순회 정점의 가중치 정상화화
                heapq.heappush(Q, (W[v], v)) #정상화된 가중치로 재삽입
                P[v] = u #부모 설정정
    print(W)
    print(P)
    
#kruskal's Algorithm
"""
가중치가 낮은 엣지들을 n-1번 선택하겠다
그런데 엣지를 선택 했을때 같은 집합내의 요소끼리 연결되면 삭제하겠다 <- 이 과정의 복잡도가 문제
"""

def kruskal(V, E):
    T = [] #신장 트리
    S = [[v] for v in V] #하나의 정점으로 이루어진 n개의 집합
    
    #간선 가중치로 정렬
    Q = [(w, u, v) for (u,v), w in E]
    heapq.heapify(Q)
    
    while len(T) < len(V)-1:
        w, u, v = heapq.heappop(Q)
        uSet = findSet(S,u)
        vSet = findSet(S,v)
        if uSet != vSet: #u, v가 다른 집합일때
            T.append((u,v)) 
            #u에 v 집합을 합친다
            S[uSet].extend(S[vSet])
            S.pop(vSet)
    return T

def findSet(S: list, target): #target이 속한 집합의 인덱스를 반환한는 함수수
    for i, group in enumerate(S): # i, group: 집합의 인덱스, 집합
        if target in group:
            return i
    return None
        
#Topological Sortig Algorithm
"""
어떤 그래프에 대해
진입간선이 없는 정점을 선택(u) <-이거 어떻게 찾을건데...?
    -진입간선 없는 정점 리스트를 따로 만들어두자 (교재 425p) FAT(file allocation table)과 유사
u의 진출간선과 자신을 제거한다
"""

def topological(V, E):
    lst = [] #위상정렬한 정점들의 리스트트
    edge = [(True,(u,v)) for (u,v),w in E]
    visited = []
    
    while len(lst)<len(V):
        #진입간선이 없는 정점 리스트 만드는 부분
        noneIncomingV = []
        for u in V:
            if u in visited:
                continue
            hasIncoming = False
            
            for alive,(i,j) in edge:
                if alive and j == u:
                    hasIncoming = True
                    break
            if not hasIncoming:
                noneIncomingV.append(u)
        #사이클 감지: 진입 간선 없는 정점이 없으면 사이클 존재
        if not noneIncomingV:
            print("none solution: cycle detected")
            return None
        for u in noneIncomingV:
            lst.append(u)
            visited.append(u)
            #진출간선 삭제
            for idx,(alive,(i,j)) in enumerate(edge):
                if i == u:
                    edge[idx] = (False,(i,j))
    return lst

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
    dist = [math.inf for _ in V]
    dist[r] = 0
    P = [None for _ in V] #부모 설정
    visited = [False for _ in V]
    
    Q = [(0,r)] #가중치 큐
    
    for u in V:
        if u == r: continue
        Q.append((adjM[r][u],u)) #r에서 u까지 가는 비용 -> 정점 가중치
        if adjM[r][u] is not math.inf:
            P[u] = r
    heapq.heapify(Q)
    
    while Q:
        w,u = heapq.heappop(Q)
        if visited[u]: continue
        visited[u] = True
        
        for v in range(len(V)):
            if adjM[u][v] == math.inf: continue
            if not visited[v] and w + adjM[u][v] < dist[v]:
                dist[v] = w + adjM[u][v]
                P[v] = u
                heapq.heappush(Q,(dist[v],v))
    
    return P

#Bellman-Ford Shortest Path Algorithm
"""
다익스트라에서 음의 사이클 확인하는 부분 추가만 한건가?
"""
def bellmanFord(V, E, r):
    W = [math.inf for _ in V] #가중치 초기화
    W[r] = 0
    P = [None for _ in V]
    
    for _ in range(len(V)-1):
        for (u,v),weight in E:
            if W[u] + weight < W[v]:
                W[v] = W[u] + weight
                P[v] = u
    
    for (u,v),w in E:
        if W[u] + w < W[v]:
            print("none solution: negative cycle")
            return None
    return P
    
    
if __name__ == "__main__":
    V = [ i for i in range(7)]
    print(V)

    E = [ ((0, 1), 8), ((1, 2), 10), ((0, 3), 9), ((3, 2),5), ((0, 4), 11), ((4, 3), 13), ((3,6), 12), ((4, 5), 8), ((5, 6), 7) ]
    
    Prim(V, E, 0)
    
    kru = kruskal(V,E)
    print(f'\nkruskal:{kru}\n')
    
    tpV = [i for i in range(5)]
    tpE_withCycle = [
        ((0,1),0),
        ((1,2),0),
        ((1,4),0),
        ((2,4),0),
        ((2,0),0),
        ((3,2),0)
    ]
    
    topol = topological(V,E)
    print(f'topological Sorting: {topol}\n')
    topol = topological(tpV,tpE_withCycle)
    print(f'topological Sorting with cycle: {topol}\n')
    
    dj = dijstra(V,E,1)
    print(f'dijstra: {dj}\n')
    
    bfV = [ i for i in range(5)]
    bfE = [
    ((0, 1), 6),
    ((0, 3), 7),
    ((1, 2), 5),
    ((1, 3), 8),
    ((1, 4), -4),
    ((2, 1), -2),
    ((3, 2), -3),
    ((3, 4), 9),
    ((4, 0), 2),
    ((4, 2), 7),
    ]
    bfE_Ncycle = [
    ((0, 1), 6),
    ((0, 3), 7),
    ((1, 2), 5),
    ((1, 3), 8),
    ((1, 4), -4),
    ((2, 1), -2),
    ((3, 2), -3),
    ((3, 4), 9),
    ((4, 0), 2),
    ((4, 2), -1),
    ]
    bfP = bellmanFord(V,E,0)
    bfN = bellmanFord(bfV,bfE,0)
    bfNC = bellmanFord(bfV,bfE_Ncycle,0)
    print(f'bellmanFord only positive w: {bfP}\n')
    print(f'bellmanFord with negative w: {bfN}\n')
    print(f'bellmanFord with negative cycle: {bfNC}\n')
    
    
