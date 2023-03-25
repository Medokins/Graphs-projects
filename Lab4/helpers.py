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

def showDigraf(adj_matrix, weight = None):
    G = nx.DiGraph()

    # Dodanie wierzchołków do grafu
    for i in range(len(adj_matrix)):
        G.add_node(i)

    # Dodanie krawędzi i wag do grafu
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                if weight == None:
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
    if weight != None:
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # Wyświetlenie grafu
    plt.show()

# Ad. 2

# Ad. 3

# Ad. 4