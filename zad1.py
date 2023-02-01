# Lista 7 Zadanie 1


from typing import Self
from random import randint

class Graph:

    class _Vertex:

        def __init__(self, name) -> None:
            self._name = name
            self._neighbors = {}

        def get_name(self):
            return self._name

        def get_neighbors(self):
            return self._neighbors.keys()

        def get_edges(self):
            return self._neighbors.items()

        def add_neighbor(self, nbr: Self, weight=0) -> None:
            if not isinstance(nbr, self.__class__):
                raise TypeError(f'Neighbor must be of {self.__class__.__name__} type')
            self._neighbors[nbr.get_name()] = weight

        def __eq__(self, __o: Self) -> bool:
            return self._name == __o._name and self._neighbors == __o._neighbors

        def __ne__(self, __o: Self) -> bool:
            return not self == __o

        # Metoda zaimplementowana w taki sposób, aby móc łatwiej rozszerzać funkcjonalność w podklasach
        def _to_string(self) -> str:
            return f'Vertex: {str(self.get_name())} | Neighbors : {[edge for edge in self.get_edges()]}'

        def __str__(self) -> str:
            return '(' + self._to_string() + ')'

    def __init__(self) -> None:
        self.verticies = {}
        self.size = 0

    def add_vertex(self, key) -> _Vertex:
        self.size += 1
        self.verticies[key] = Graph._Vertex(key)
        return self.verticies[key]

    def get_vertex(self, key) -> (_Vertex | None):
        return self.verticies.get(key, None)

    def __contains__(self, key) -> bool:
        return key in self.verticies

    def __getitem__(self, key) -> _Vertex:
        if key not in self:
            raise IndexError(f'There is no vertex with name {key}')
        return self.get_vertex(key)


    def add_edge(self, from_key, to_key, weight=0) -> None:

        if from_key not in self:
            self.add_vertex(from_key)

        if to_key not in self:
            self.add_vertex(to_key)

        self[from_key].add_neighbor(self[to_key], weight)

    def get_verticies(self):
        return self.verticies.keys()

    def __iter__(self):
        return iter(self.verticies.values())

    def __str__(self):
        return '\n'.join(str(vert) for vert in self)
            
# Funkcja testująca klasę Graph. Użyto modułu pytest        
def test_graph():

        sample = [randint(0, 100) for _ in range(100)]
        g = Graph()
        for val in sample:
            vert = Graph._Vertex(val)
            assert g.add_vertex(val) == vert
            nbr = Graph._Vertex(randint(0, 100))
            weight = randint(0, 100)
            g.add_edge(val, nbr.get_name(), weight)
            vert.add_neighbor(nbr, weight)
            assert g.get_vertex(val) == vert
