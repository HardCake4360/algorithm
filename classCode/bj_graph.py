import math
from collections import deque

# adjacenyMatrix

V = [ i+1 for i in range(8)]

E = [ (1, 2), (1, 3), (1, 4), (3, 5), (4, 6), (4, 7), (6, 8)]

#print(V)

AdjM = [ [ math.inf for _ in range(len(V))] for _ in range(len(V)) ]
for row, col in E:    
    AdjM[row-1][col-1] = 1
    AdjM[col-1][row-1] = 1
    
#print(AdjM)

# AdjacencyArray

AdjA = [ [] for _ in range(len(V))]
for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)

# print(AdjA)

# print(3 < math.inf)
# print(3 < -math.inf)

# buildPath
def buildPath(parent: list, dest):
    path = [dest]
    current = dest
    while parent[current-1] != -1:
        path.append(parent[current-1])
        current = parent[current-1]
    path.reverse()
    return path

#bfs 트리 생성: BFS알고리즘을 이용하여 그래프->트리 구성하기

queue = []
visited = []
parent = []

source = 1

queue.append(source)
visited.append(source)
while(queue):
    current = queue.pop(0)
    for i in range(len(AdjA[current])):
        if AdjA[current][i] not in visited:
            visited.append(AdjA[current][i])
            queue.append(AdjA[current][i])
        parent.append((AdjA[i],current))


#DFS
def DFS(V, AdjA, s, d: int = None):
    parent = [ -1 for _ in range(len(V))]
    Tree = [ [] for _ in range(len(V))]
    visited = [ False for _ in range(len(V))]
    S = [s]
    visited[s-1] = True
    while len(S) > 0:
        current = S.pop(-1)
        for neighbor in AdjA[current-1]:
            if visited[neighbor-1] == False:
                visited[neighbor-1] = True
                S.append(neighbor)
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
# def DFS_recursive(V, AdjA, current, d: int = None):
#     parent = [ -1 for _ in range(len(V))]
#     Tree = [ [] for _ in range(len(V))]
#     visited = [ False for _ in range(len(V))]
#     visited[current-1] = True
#     for neighbor in AdjA[current-1]:
#         if visited[neighbor-1] == False:
#             print(f"cur: {current}-> nei: {neighbor}")
#             DFS_recursive(V, AdjA, neighbor-1,d)

def DFS_recursive(V, AdjA, current, visited, parent, Tree):
    for neighbor in AdjA[current-1]:
        if not visited[neighbor-1]:
            print(f"cur: {current} -> nei: {neighbor}")
            visited[neighbor-1] = True
            parent[neighbor-1] = current
            Tree[current-1].append(neighbor)
            DFS_recursive(V, AdjA, neighbor, visited, parent, Tree)

def DFSR(V, AdjA, s, d: int = None):
    n = len(V)
    visited = [False] * n
    parent = [-1] * n
    Tree = [[] for _ in range(n)]
    DFS_recursive(V, AdjA, s, visited, parent, Tree)

if __name__ == "__main__":
    path = DFSR(V,AdjA,1,1)
    print(path)
