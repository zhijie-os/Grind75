from collections import defaultdict
'''
    a topological sort algorithm returns a sequence of vertices 
    in which the vertices never come before their predecessors 
    on any paths
'''

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    # adjacency list implementation
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortHelper(self, v ,visited, stack):
        visited[v] = True

        # for every child, do topo sort on it
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortHelper(i, visited, stack)
        # Push current vertex to stack which stores result
        stack.insert(0, v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortHelper(i, visited, stack)
        
        print(stack)

 
g= Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1);

 
print("Following is a Topological Sort of the given graph")
g.topologicalSort()