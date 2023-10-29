def dls(node, graph, depth, visited, component):
    if depth == 0:
        return
    component.append(node)
    visited[node] = True  
    for child in graph[node]:
        if not visited[child]:
            dls(child, graph, depth - 1, visited, component)

def iddfs(graph, start_node, max_depth):
    for depth in range(max_depth + 1):
        visited = [False] * len(graph)
        component = []
        dls(start_node, graph, depth, visited, component)
        print(f"Depth {depth}: {component}")

if __name__ == "__main__":
    graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    start_node = 0
    max_depth = 3

    iddfs(graph, start_node, max_depth)
