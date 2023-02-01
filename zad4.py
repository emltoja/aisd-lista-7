# Lista 7 Zadanie 4

from zad3 import TraversableGraph


class SortedGraph(TraversableGraph):

    def depth_first_search(self):
        super().depth_first_search()

        return sorted(self, key=lambda x: x.get_ftime(), reverse=True)




if __name__ == '__main__':
    g = SortedGraph()

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('A', 'E')
    g.add_edge('E', 'B')
    g.add_edge('D', 'C')

    for vert in g.depth_first_search():
        print(vert)