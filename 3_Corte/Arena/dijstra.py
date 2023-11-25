import heapq
from collections import defaultdict
from sys import stdin
INF = 1e9

def dijkstra(graph, start):
    dist = defaultdict(lambda: INF)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def solve():
    cases = int(stdin.readline().strip())
    for _ in range(cases):
        input()
        n = int(stdin.readline().strip())
        e = int(stdin.readline().strip())
        t = int(stdin.readline().strip())
        m = int(stdin.readline().strip())
        graph = defaultdict(list)
        for _ in range(m):
            a, b, w = map(int, stdin.readline().strip().split())
            graph[b].append((a, w))
        dist = dijkstra(graph, e)
        ans = sum(1 for i in range(1, n + 1) if dist[i] <= t)
        print(ans)
        if _ < cases - 1:
            print()

solve()
