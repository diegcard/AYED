from sys import stdin
def dfs(node, graph, visited):
    count = 1
    stack = [node]
    visited[node] = True
    while stack:
        current_node = stack.pop()
        neighbors = graph[current_node]

        for neighbor in neighbors:
            if not visited[neighbor]:
                count += 1
                stack.append(neighbor)
                visited[neighbor] = True
    return count


def buscar_compo(N, edges):
    graph = {i: [] for i in range(1, 2 * N + 1)}
    visited = {i: False for i in range(1, 2 * N + 1)}

    for edge in edges:
        A, B = edge
        graph[A].append(B)
        graph[B].append(A)

    smallest = float('inf')
    largest = 0

    for node in range(1, 2 * N + 1):
        if not visited[node]:
            component_size = dfs(node, graph, visited)
            smallest = min(smallest, component_size)
            largest = max(largest, component_size)

    return smallest, largest

def main():
    N = int(stdin.readline().strip())
    edges = []
    for _ in range(N):
        A, B = map(int, stdin.readline().strip().split())
        edges.append((A, B))
    min_size, max_size = buscar_compo(N, edges)
    print(min_size, max_size)
main()