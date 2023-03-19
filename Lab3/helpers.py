import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(graph, start):
    # Initialize the distance of all nodes as infinity
    dist = {node: float('inf') for node in graph}
    # Set the distance of the starting node as 0
    dist[start] = 0
    # Initialize the heap with the starting node and its distance
    heap = [(0, start)]
    # Initialize the visited set
    visited = set()

    while heap:
        # Pop the node with the minimum distance from the heap
        (min_dist, node) = heapq.heappop(heap)
        # If the node has already been visited, continue
        if node in visited:
            continue
        # Add the node to the visited set
        visited.add(node)
        # Update the distance of all unvisited neighbors of the node
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_dist = dist[node] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

    # Return the distance of all nodes from the starting node
    return dist

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