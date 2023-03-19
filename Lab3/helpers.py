import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    while pq:
        (current_distance, current_vertex) = heapq.heappop(pq)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def show_graph(graph):
    G = nx.Graph()

    # Dodaj wierzchołki do grafu
    for vertex in graph.keys():
        G.add_node(vertex)

    # Dodaj krawędzie do grafu
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(vertex, neighbor, weight=weight)

    # Ustaw pozycje wierzchołków
    pos = nx.spring_layout(G)

    # Narysuj wierzchołki, krawędzie i wagi krawędzi
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=16)

    # Wyświetl graf
    plt.axis('off')
    plt.show()