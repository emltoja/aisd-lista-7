#Lista 7 Zadanie 2


from zad1 import Graph
from graphviz import Digraph

class DotGraph(Graph):

    def dot_repr(self):

        dot = Digraph('Graph DOT representation')

        for vert_key in self.get_verticies():
            dot.node(str(vert_key))

        for vert in self:
            for edge in vert.get_edges():
                dot.edge(str(vert.get_name()), *map(str, edge))

        return dot

if __name__ == '__main__':
    
    graph = DotGraph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(1, 4)
    graph.add_edge(6, 7)
    graph.add_edge(5, 8)
    graph.add_edge(6, 8)
    graph.add_edge(8, 9)
    graph.add_edge(2, 9)

    print(graph.dot_repr())