from sys import stdin
def dfs(grafo, nodo, visitados):
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
    return grafo

def componentes_conexos(N, arcos):
    grafo = {i: set() for i in range(1, 2*N+1)}
    for a, b in arcos:
        grafo[a].add(b)
        grafo[b].add(a)
    visitados = set()
    tamanos = []
    for nodo in range(1, 2*N+1):
        if nodo not in visitados:
            componente = set()
            dfs(grafo, nodo, componente)
            tamanos.append(len(componente))
            visitados |= componente
    return min(tamanos), max(tamanos)
def main():
    N = int(stdin.readline().strip())
    arcos = [tuple(map(int, stdin.readline().strip().split())) for _ in range(N)]
    minimo, maximo = componentes_conexos(N, arcos)
    print(minimo, maximo)
if __name__ == '__main__':
    main()