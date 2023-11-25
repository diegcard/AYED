class DisjointSets:
    def __init__(self, data=[]):
        self.data = []
        for e in data:
            self.makeSet(e)
    # Encontrar el conjunto al cual pertenece el elemento e
    def findSet(self, e):
        for conjunto in self.data:
            if e in conjunto:
                return conjunto
        return None
    # Crear un conjunto dado un elemento cáracteristico,
    # siempre que no exista un conjunto con ese elemento en la estructura
    def makeSet(self, e):
        conjunto = self.findSet(e)
        if conjunto is None:
            self.data.append(set([e]))
            return self.data[-1]
        return conjunto
    def union(self, a, b):
        st1 = self.makeSet(a)
        st2 = self.makeSet(b)
        if st1 != st2:
            st3 = st1.union(st2)
            self.data.remove(st1)
            self.data.remove(st2)
            self.data.append(st3)
    def __str__(self):
        return str(self.data)
def connectedComponents(graph):
    vertexes, arcs = graph[0], graph[1]
    disjointSets = DisjointSets(vertexes)
    print(disjointSets)
    for e in arcs:
        disjointSets.union(e[0], e[1])
        print(e, ' : ', disjointSets)
    return disjointSets
def main():
    arcs = [(0,1), (1,2), (2,0), (3,5),
            (5,4), (4,7), (6,8), (8,9),
            (9,6)
           ]
    vertexes = [ x for x in range(10)]
    graph = (vertexes, arcs)
    print(connectedComponents(graph))
main()