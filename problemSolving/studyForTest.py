import sys
sys.setrecursionlimit(10 ** 4)

#깊이우선 탐색 (재귀)
def dfs(node, visited, graph):
    visited.append(node)
    print(node, end = ' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited,graph)
     
#깊이우선 탐색 (스택)
def dfs_stack(start, graph):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            # 나중에 방문할 노드를 먼저 넣기 위해 reversed
            stack.extend(reversed(graph[node]))
            
#섬의 개수
def island(map,w,h):
    cnt = 0
    visited = [[False for _ in range(h)] for _ in range(w)]
    for x in range(len(map)):
        for y in range(len(map[x])):
            print(f"({x},{y}): {map[x][y]}")
            if map[x][y] == 1:
                if visited[x][y]: continue
                checkIsland(map,x,y,visited)
                cnt += 1
            visited[x][y] = True
    return cnt
            
def checkIsland(map: list, w, h, visited: list):
    visited[w][h] = True
    near = [-1, 0, 1]
    for i in near:
        if w+i < 0 or w+i >= len(map): continue #범위를 초과했을때
        for j in near:
            if h+j < 0 or h+j >= len(map[w]): continue #범위를 초과했을때
            if map[w+i][h+j] == 1 and not visited[w+i][h+j]:
                checkIsland(map,w+i,h+j,visited)
                    
def BFS(maze: list, w, h, visited: list):
    Q = [(w,h)]
    visited[w][h] = 1
    print(f"start from {w},{h}")
    nx = [0, -1, 1, 0]
    ny = [-1, 0, 0, 1]
    while Q:
        x,y = Q.pop(0)
        for i in range(4):
            dx = x+nx[i]
            dy = y+ny[i]
            if not(0 <= dx < len(maze) and 0 <= dy < len(maze[0])): continue
            
            if maze[dx][dy] == 1 and visited[dx][dy] == -1:
                Q.append((dx,dy))
                visited[dx][dy] = visited[x][y]+1
                print(f"visited: {dx},{dy}({visited[dx][dy]})")

#인접 리스트 연결 요소 개수 문제       
def makeGraph(V:list,E:list): #무향 인접 리스트
    for a,b in E:
        V[a-1].append(b-1)
        V[b-1].append(a-1)
    return V
                
def conection(graph:list):
    visited = [False]*len(graph)
    cnt = 0
    for i in range(len(graph)):
        if visited[i]: continue
        dfs_graph(graph,visited,i)
        cnt += 1
    print(cnt)
    
def dfs_graph(graph:list, visited:list, v):
    visited[v] = True
    print(f"visited: {v}")
    for i in graph[v]:
        if visited[i]: continue
        dfs_graph(graph,visited,i)
        
def cantor(length):
    if length == 1:
        return '-'
    left    = ""
    midle   = ""
    center = length//3
    for i in range(center):
        midle += ' '
    left += cantor(center)
    return left + midle + left
    
    
    
if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [],
        5: []
    }
    
    dfs(1,[],graph)
    
    map1 = [
        [0,0,0],
        [0,1,0],
        [0,0,0],
    ]
    map2 = [
        [0,0,0,0],
        [0,0,0,0],
        [0,1,0,1],
        [0,0,0,1],
    ]
    map3 = [
        [1,0,0,1],
        [0,0,0,0],
        [0,0,0,0],
        [1,0,0,1],
    ]
    print(island(map1,3,3))
    print(island(map2,4,4))
    print(island(map3,4,4))
    
    maze = [
        [1,1,1,1],
        [0,0,0,1],
        [1,1,1,1],
        [1,0,0,0],
        [1,1,1,1],
        [1,0,1,1],
    ]
    BFS(maze,0,0,[[-1 for _ in range(len(maze[0]))]for _ in range(len(maze))])
    
    V = [[] for _ in range(6)]
    E = [
        (1,2),
        (2,5),
        (5,1),
        (3,4),
        (4,6)
    ]
    
    graph = makeGraph(V,E)
    conection(graph)
    
    print(cantor(27))