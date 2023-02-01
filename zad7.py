# Lista 7 Zadanie 7

from zad3 import TraversableGraph
from zad5 import shortest_path

# Niech:
#
# x - aktualna objętość w wiaderku 3 litrowym
# y - aktualna objętość w wiaderku 4 litrowym
#
# W każdej chwili mamy możliwych 6 decyzji do podjęcia
#
# 1. Nalać do wiaderka 3 litrowego (x = 3)
#
# 2. Nalać do wiaderka 4 litrowego (y = 4)
#
# 3. Wylać z wiaderka 3 litrowego (x = 0)
#
# 4. Wylać z wiaderka 4 litrowego (y = 0)
#
# 5. Przelać z 3 litrowego do 4 litrowego (new_x = max(x + y - 4, 0)
#                                          new_y = min(x + y, 4))
#
# 6. Przelać z 4 litrowego do 3 litrowego (new_x = min(x + y, 3)
#                                          new_y = max(x + y - 3, 0))
#
# Jako, że stan początkowy objętości w wiaderkach wyraża się przez liczby naturalne (x = 0, y = 0),
# każda z decyzji parę liczb natrualnych przekstałca w również parę liczb naturalnych oraz z racji, że 
# w obu wiaderkach może się znajdować nie więcej niż 7 litrów (x + y <= 7), to dochodzimy do wniosku, że istnieje
# skończona ilość konfiguracji stanu ilości wody w obu wiaderkach. 
#
# Tym samym możemy utworzyć graf w, którym wierzchołkami będą pary (x, y) reprezentujące poszczególne stany, a 
# krawędziami przejścia pomiędzy tymi stanami
#
# Zadanie rozwiążemy poprzez wpierw utworzenie wszystkich możliwych wierzchołków (x, y). 
# Wtedy graf przeszukamy wszerz i korzystając z algorytmu z zadania 5
# znajdziemy najkrótsze ścieżki do dowolnych wierzchołków z dwójką i wybierzemy najmniejszą. 


# Zbiór przechowujący wszystkie już utworzone do tej pory krawędzie
used_edges = set()


# Zwraca wszystkie unikatowe przejścia, które jeszcze się nie pojawiły w grafie
def possible_pairs(current_pair):
    
    x, y = current_pair[0], current_pair[1]

    # Zbiór zawierający wszystkie możliwe stany, do których jesteśmy w stanie przejść z aktualnego
    possibilities = {(x, 4),
                     (3, y),
                     (x, 0),
                     (0, y),
                     (max(x + y - 4, 0), min(x + y, 4)),
                     (min(x + y, 3), max(x + y - 3, 0))}

    # Odrzucamy decyzje, który nie zmieniają aktualnego stanu, bądź te, które już kiedyś podjęliśmy
    edge_already_used = lambda option: (current_pair, option) in used_edges or (option, current_pair) in used_edges or current_pair == option

    result = [option for option in possibilities if not edge_already_used(option)]
    used_edges.update(set((current_pair, option) for option in possibilities))
    return result


# Rekurencyjna funkcja podejmująca decyzje (1. - 6.) 
def add_edges(g: TraversableGraph, current_pair):

    options = possible_pairs(current_pair)
 
    for option in options:
        g.add_edge(current_pair, option)

        if 2 in options:
            # Osiągnęliśmy pożądany stan, nie musimy podejmować dalszych decyzji
            return 

        add_edges(g, option)

            
# Utworzenie grafu
def create_graph(starting_values):

    g = TraversableGraph()
    g.add_vertex(starting_values)
    current_pair = (0, 0)

    add_edges(g, current_pair)

    return g


def find_solution(starting_values: tuple[int, int]):

    g = create_graph(starting_values)

    # Wszystkie możliwe stany, w których w dowolnym wiaderku znajdują się 2 litry wody
    two_litre_options = [key for key in g.get_verticies() if 2 in key]
    paths = [shortest_path(g, (0, 0), key) for key in two_litre_options]

    # Wybranie najkrótszej ścieżki 
    result = paths[0]
    for path in paths:
        if len(path) < len(result):
            result = path
    return result

if __name__ == "__main__":
    print(find_solution((0, 0)))
