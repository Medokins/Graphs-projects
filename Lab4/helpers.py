import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Ad. 1
def makeRandomDigraf(num_of_vertexes, edge_probability):
    adj_matrix = np.zeros((num_of_vertexes, num_of_vertexes))
    for i in range(num_of_vertexes):
        for j in range(i+1, num_of_vertexes):
            if np.random.random() < edge_probability:
                if np.random.randint(2) == 0:
                    adj_matrix[i][j] = 1
                else:
                    adj_matrix[j][i] = 1

    return adj_matrix

def showDigraf(adj_matrix, weights = None):
    G = nx.DiGraph()

    # Dodanie wierzchołków do grafu
    for i in range(len(adj_matrix)):
        G.add_node(i)

    # Dodanie krawędzi i wag do grafu
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                if weights == None:
                    G.add_edge(i, j)
                else:
                    G.add_edge(i, j, weight=weights[i][j])

    # Ustawienie pozycji wierzchołków
    pos = nx.circular_layout(G)

    # Rysowanie grafu
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    # Dodanie wag do krawędzi
    if weights != None:
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # Wyświetlenie grafu
    plt.show()


# Ad. 2
def transpose_graph(G):
    n = len(G)
    transposed_graph = [[] for _ in range(n)]
    for v in range(n):
        for u in G[v]:
            transposed_graph[u].append(v)
    return transposed_graph

def kosaraju(G):
    n = len(G)
    d = [-1] * n
    f = [-1] * n
    t = 0

    for v in range(n):
        if d[v] == -1:
            t = DFS_visit(v, G, d, f, t)

    # tworzenie grafu transponowanego
    GT = transpose_graph(G)

    nr = 0
    comp = [-1] * n

    for v in sorted(range(n), key=lambda x: f[x], reverse=True):
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_r(nr, v, GT, comp)

    return comp


def DFS_visit(v, G, d, f, t):
    t += 1
    d[v] = t

    for u in G[v]:
        if d[u] == -1:
            t = DFS_visit(u, G, d, f, t)

    t += 1
    f[v] = t
    return t


def components_r(nr, v, GT, comp):
    for u in GT[v]:
        if comp[u] == -1:
            comp[u] = nr
            components_r(nr, u, GT, comp)

# Ad. 3

# Ad. 4