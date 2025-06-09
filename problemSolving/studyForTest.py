#깊이우선 탐색 (재귀)
def dfs(node, visited, graph):
    visited.add(node)
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
            
if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [],
        5: []
    }
    
    dfs(node)