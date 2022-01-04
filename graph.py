class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, crnt, next):
        if crnt not in self.graph:
            self.graph[crnt] = [next]
        else:
            self.graph[crnt].append(next)

# BFS implementation    
    def BFS(self, start):
        q = [start]
        visited = [False]*len(self.graph)
        visited[start] = True
        while(len(q) != 0):
            start = q.pop(0)
            print(start)
            for node in self.graph[start]:
                if visited[node] == False:
                    q.append(node)
                    visited[node] = True

# DFS implementation        
    def DFS(self, start):
        s = [start]
        visited = [False]*len(self.graph)
        visited[start] = True
        while(len(s) != 0):
            start = s.pop()
            print(start)
            for node in self.graph[start]:
                if visited[node] == False:
                    s.append(node)
                    visited[node] = True

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,0)
g.addEdge(5,2)
g.DFS(0)


# recursive implementation (DFS)
myGraph = {
    0: [1,2,3],
    1: [0,3],
    2: [0,3],
    3: [0,1,2,4],
    4: [3]
}
visited = [False]*len(myGraph)
def DFS(graph, u):
    print(u)
    visited[u] = True
    for v in myGraph[u]:
        if not visited[v]:
            DFS(graph, v)

DFS(myGraph, 0)














