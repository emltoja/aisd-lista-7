# Lista 7 Zadanie 5

from zad3 import TraversableGraph

def shortest_path(g: TraversableGraph, from_key, to_key):

    if from_key not in g or to_key not in g:
        raise ValueError('Podane wierzchołki nie należą do grafu')

    # Przeszukanie grafu wszerz
    g.breadth_first_search(from_key)

    # Zaczynamy od docelowego wierzchołka i będziemy się poruszać
    # do tyłu przez jego poprzedników 
    result = [g[to_key]]

    # Poruszanie się po poprzednich wierzchołków aż dotrzemy do
    # wierzchołka bez poprzednika
    while result[-1].get_pred() is not None:
        result.append(result[-1].get_pred())

    # Jeśli nie dotarliśmy do wierzchołka początkowego, to znaczy, że 
    # te wierzchołki nie są ze sobą połączone
    if result[-1] != g[from_key]:
        return 'Brak ścieżki między dwoma wierzchołkami'

    return list(map(lambda x: x.get_name(), reversed(result)))


if __name__ == "__main__":
    
    g = TraversableGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(1, 4)
    g.add_edge(6, 7)
    g.add_edge(5, 8)
    g.add_edge(6, 8)
    g.add_edge(8, 9)
    g.add_edge(2, 9)


    print(shortest_path(g, 2, 9))


