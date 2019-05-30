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

    def __init__(self, make_transpose_graph=False):
        self.edge_list = []
        self.nodes_list = []
        self.adjacency_list = {}
        self.visited = {}
        self.stack = []
        if make_transpose_graph:
            self.transpose_graph = Graph()

    def add_edge(self, edge):
        self.edge_list.append(edge)
        src = edge.src
        dest = edge.dest
        self.adjacency_list[src].append(dest)

        self.transpose_graph.edge_list.append(Edge(dest, src))
        self.transpose_graph.adjacency_list[dest].append(src)

        return edge

    def add_node(self, node):
        self.nodes_list.append(node)
        self.adjacency_list[node] = []
        self.visited[node] = False

        self.transpose_graph.nodes_list.append(node)
        self.transpose_graph.adjacency_list[node] = []
        self.transpose_graph.visited[node] = False

        return node

    def dfs(self, node):
        self.visited[node] = True
        for adjacent in self.adjacency_list[node]:
            if not self.visited[adjacent]:
                self.dfs(adjacent)
        self.stack.append(node)

    def dfs2(self, node, my_stack):
        self.visited[node] = True
        for adjacent in self.adjacency_list[node]:
            if not self.visited[adjacent]:
                self.dfs2(adjacent, my_stack)
        my_stack.append(node)
        return my_stack

    def perform_topological_sort(self):
        for current_node in self.nodes_list:
            if not self.visited[current_node]:
                self.dfs(current_node)

    def topological_sort(self):
        print("performing topological sort on graph")
        self.perform_topological_sort()


g = Graph(make_transpose_graph=True)
A = g.add_node(Node('0'))
B = g.add_node(Node('1'))
C = g.add_node(Node('2'))
D = g.add_node(Node('3'))
E = g.add_node(Node('4'))
F = g.add_node(Node('5'))
G = g.add_node(Node('6'))
H = g.add_node(Node('7'))
I = g.add_node(Node('8'))

g.add_edge(Edge(D, A))
g.add_edge(Edge(A, B))
g.add_edge(Edge(B, C))
g.add_edge(Edge(C, D))


g.add_edge(Edge(C, E))

g.add_edge(Edge(E, F))
g.add_edge(Edge(G, E))
g.add_edge(Edge(F, G))

g.add_edge(Edge(H, G))
g.add_edge(Edge(H, I))


g.topological_sort()

print(g.nodes_list)
print(g.edge_list)
print(g.adjacency_list)

transpose_graph = g.transpose_graph
topological_sort_stack = g.stack.copy()
while len(topological_sort_stack) != 0:
    popped_node = topological_sort_stack.pop()
    if not transpose_graph.visited[popped_node]:
        print(transpose_graph.dfs2(popped_node, []))

