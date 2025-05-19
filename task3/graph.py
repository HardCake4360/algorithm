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
    
    S = [ 0 for _ in range(len(V))] #방문한 정점점
    P = [ None for _ in range(len(V))] #부모 리스트트
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
        heapq.heappush( Q, (W[i], i+1) ) #Q에 튜플 형식으로 (가중치, 정점번호) 삽입입
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
                W[v] = AdjM[u-1][v]
                heapq.heappush(Q, (W[v], v+1))
                P[v] = u
    print(W)
    print(P)
    
    
    
    
if __name__ == "__main__":
    V = [ i+1 for i in range(7)]
    print(V)

    E = [ ((1, 2), 8), ((2, 3), 10), ((1, 4), 9), ((4, 3),5), ((1, 5), 11), ((5, 4), 13), ((4,7), 12), ((5, 6), 8), ((6, 7), 7) ]
    
    Prim(V, E, 1)
    
    
    
    
