import networkx as nx
import matplotlib.pyplot as plt

def relax(u, v, weights, lengths, predecessors):
    if lengths[v] > lengths[u] + weights[u][v]:
        lengths[v] = lengths[u] + weights[u][v]
    predecessors[v] = u

def dijkstra(graph, weights, vertexId):
    n = len(graph)
    lengths = [float('inf') for _ in range(n)]
    predecessors = [None for _ in range(n)]
    lengths[vertexId] = 0
    S = set()

    adjacencyList = [[] for _ in range(n)]
    for u, neighbors in enumerate(graph):
        for v in neighbors:
            adjacencyList[u].append(v)

    vertexList = [v for v in range(n)]

    while len(S) != n:
        u = min((v for v in vertexList if v not in S), key=lambda v: lengths[v])
        S.add(u)
        for v in adjacencyList[u]:
            if v not in S:
                relax(u, v, weights, lengths, predecessors)

    return lengths, predecessors

def show_graph(graph, weights) -> None:
    G = nx.Graph()

    # Dodanie wierzchołków do grafu
    for i in range(len(graph)):
        G.add_node(i)

    # Dodanie krawędzi i wag do grafu
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if weights[i][j] != float('inf'):
                G.add_edge(i, graph[i][j], weight=weights[i][graph[i][j]])

    # Ustawienie pozycji wierzchołków
    pos = nx.circular_layout(G)

    # Rysowanie grafu
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    # Dodanie wag do krawędzi
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Wyświetlenie grafu
    plt.show()