class Node(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self.name)


class Edge(object):
    def __init__(self, src: Node, dest: Node):
        self.src = src
        self.dest = dest

    def __repr__(self):
        return self.src.name + "=>" + self.dest.name


class Graph(object):

    def __init__(self):
        self.edge_list = []
        self.nodes_list = []
        self.adjacency_list = {}
        self.visited = {}

    def add_edge(self, edge):
        self.edge_list.append(edge)
        src = edge.src
        dest = edge.dest
        self.adjacency_list[src].append(dest)
        return edge

    def add_node(self, node):
        self.nodes_list.append(node)
        self.adjacency_list[node] = []
        self.visited[node] = False
        return node

    def dfs(self, node):
        self.visited[node] = True
        for adjacent in self.adjacency_list[node]:
            if not self.visited[adjacent]:
                self.dfs(adjacent)
        print(node)

    def perform_topological_sort(self):
        for current_node in self.nodes_list:
            if not self.visited[current_node]:
                self.dfs(current_node)

    # noinspection PyMethodMayBeStatic
    def topological_sort(self):
        print("performing topological sort on graph")
        self.perform_topological_sort()


g = Graph()
A = g.add_node(Node('A'))
B = g.add_node(Node('B'))
C = g.add_node(Node('C'))
D = g.add_node(Node('D'))
E = g.add_node(Node('E'))

g.add_edge(Edge(A, C))
g.add_edge(Edge(A, B))
g.add_edge(Edge(B, D))
g.add_edge(Edge(C, D))
g.add_edge(Edge(D, E))

g.topological_sort()

print(g.nodes_list)
print(g.edge_list)
print(g.adjacency_list)

