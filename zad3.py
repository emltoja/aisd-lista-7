# Lista 7 Zadanie 3 

from zad1 import Graph
from typing import Self
from queue import Queue


class TraversableGraph(Graph):

    class _TraversableVertex(Graph._Vertex):

        
        def __init__(self, name) -> None:
            super().__init__(name)
            self._color = 'W'       # Kolor wierzechołka: W - nieodwiedzony
                                    #                     G - odwiedzony, niesprawdzony
                                    #                     B - odwiedzony, sprawdzony
            
            self._dist = -1         # odległość od początku 
            self._pred = None       # poprzedni wierzchołek w ścieżce
            self._dtime = 0         # czas dotarcia do wierzchołka (do zmiany na G)
            self._ftime = 0         # czas sprawdzenia wierzchołka (do zmiany na B)

        ############# SETTERS ###########################################################

        def set_color(self, c: str) -> None:
            if c not in 'WGB':
                raise ValueError('Podano niepoprawną wartość koloru wierzchołka')
            self._color = c

        def set_pred(self, p: Self) -> None:
            if not (isinstance(p, self.__class__) or p is None):
                raise TypeError('Poprzednik musi być wierzchołkiem')
            self._pred = p

        def set_dist(self, d: int) -> None:
            self._dist = d
        
        def set_dtime(self, dtime: int | float) -> None:
            self._dtime = dtime

        def set_ftime(self, ftime: int | float) -> None:
            self._ftime = ftime


        ############# GETTERS ###########################################################

        def get_color(self) -> str:
            return self._color

        def get_pred(self) -> Self:
            return self._pred

        def get_dist(self) -> int:
            return self._dist

        def get_dtime(self) -> int | float:
            return self._dtime

        def get_ftime(self) -> int | float:
            return self._ftime

        def get_weight(self, key) -> int | float:
            return self._neighbors[key]


        #################################################################################

        def _to_string(self) -> str:
            return super()._to_string() + '\n' +  f' | Color: {self._color} | Dist: {self._dist} | Dtime: {self._dtime} | Ftime: {self._ftime} | Pred: {self._pred.get_name() if self._pred else None}'

        def __str__(self) -> str:
            return '(' + self._to_string() + ')'

    #####################################################################################
    def __init__(self) -> None:
        super().__init__()
        self.search_queue = Queue(self.size)    # Kolejka przeszukiwań dla przeszukiwania wszerz
        self.time = 0


    def add_vertex(self, key) -> _TraversableVertex:
        self.size += 1
        self.verticies[key] = TraversableGraph._TraversableVertex(key)
        return

    def __getitem__(self, key) -> _TraversableVertex:
        return super().__getitem__(key)


    # Wyczyszczenie informacji o wierzchołkach ustalonych po przeszukiwaniu 
    def clear(self):
        self.time = 0
        for vert in self:
            vert.set_color('W')
            vert.set_dist(0)
            vert.set_pred(None)
            vert.set_dtime(0)
            vert.set_ftime(0)


    # Przeszukanie grafu wzdłuż 
    def breadth_first_search(self, start_key):

        self.clear()
        start = self[start_key]
        start.set_dist(0)

        self.search_queue.put(start)

        while not self.search_queue.empty():
            current = self.search_queue.get()
            for nbr in current.get_neighbors():
                self.time += 1
                nbr_vert = self[nbr]
                if nbr_vert.get_color() == 'W':
                    nbr_vert.set_color('G')
                    nbr_vert.set_dtime(self.time)
                    nbr_vert.set_dist(current.get_dist() + 1)
                    nbr_vert.set_pred(current)
                    self.search_queue.put(nbr_vert)
            current.set_ftime(self.time)
            self.time += 1
            current.set_color('B')


    # Przeszukanie grafu w głąb
    def depth_first_search(self):
        self.clear()
        for vert in self:
            if vert.get_color() == 'W':
                self.visit_vertex(vert)

    def visit_vertex(self, start_vert: _TraversableVertex):
        start_vert.set_color('G')
        self.time += 1
        start_vert.set_dtime(self.time)
        for nbr in start_vert.get_neighbors():
            next_vert = self[nbr]
            if next_vert.get_color() == 'W':
                next_vert.set_pred(start_vert)
                next_vert.set_dist(start_vert.get_dist() + 1)
                self.visit_vertex(next_vert)
        start_vert.set_color('B')
        self.time += 1
        start_vert.set_ftime(self.time)


if __name__ == '__main__':

    g = TraversableGraph()

    g.add_edge('A', 'B')
    g.add_edge('A', 'D')
    g.add_edge('B', 'D')
    g.add_edge('D', 'E')
    g.add_edge('E', 'B')
    g.add_edge('B', 'C')
    g.add_edge('E', 'F')
    g.add_edge('F', 'C')

    print(g)
    g.depth_first_search()
    print('\n\n\n')
    print(g)
