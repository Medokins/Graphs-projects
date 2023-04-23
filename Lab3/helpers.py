import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import heapq
from typing import List, Tuple

import sys
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab2.helpers import *

# Ad. 1
def convert_adj_list_from_1_to_0_start(adjacency_list):
    for i in range(len(adjacency_list)):
        for j in range(len(adjacency_list[i])):
            adjacency_list[i][j] -= 1
    return adjacency_list

def makeRandomWeightGraph(num_of_vertexes, edge_probability, min_weight, max_weight):
    adj_matrix = np.zeros((num_of_vertexes, num_of_vertexes))
    while len(find_largest_connected_component(adj_matrix)) != num_of_vertexes:
        adj_matrix = np.zeros((num_of_vertexes, num_of_vertexes))
        for i in range(num_of_vertexes):
            for j in range(i+1, num_of_vertexes):
                if np.random.random() < edge_probability:
                    adj_matrix[i][j] = adj_matrix[j][i] = 1
    
    weight_matrix = np.full((num_of_vertexes, num_of_vertexes), float('inf'))
    for i in range(num_of_vertexes):
        weight_matrix[i][i] = 0
        for j in range(i, num_of_vertexes):
            if adj_matrix[i][j] == 1:
                weight_matrix[i][j] = weight_matrix[j][i] = np.random.randint(min_weight, max_weight+1)
    
    return adj_matrix, weight_matrix

# Ad. 2
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

# Ad. 3
def all_pairs_shortest_paths(graph, weights):
    n = len(graph)
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]

    for vertex in range(n):
        lengths, _ = dijkstra(graph, weights, vertex)
        distances[vertex] = lengths

    return distances

# Ad. 4
def create_full_matrix(distances) -> pd.DataFrame:
    for row in distances:
        row.append(np.sum(row))
        row.append(np.max(row[:-1]))
    df = pd.DataFrame(distances)
    df = df.rename(columns={5: 'summ', 6: 'length from furthest'})
    print(df)
    return df

def center_of_graph(distances_df: pd.DataFrame) -> int:
    minSum = np.min(distances_df["summ"])
    for i, value in enumerate(distances_df['summ']):
        if value == minSum:
            return i

def center_of_graph_minimax(distances_df: pd.DataFrame) -> int:
    min = np.min(distances_df["length from furthest"])
    for i, value in enumerate(distances_df['length from furthest']):
        if value == min:
            return i


# Ad. 5
import heapq
from typing import List

def prim(graph: List[List[int]], weights: List[List[float]]) -> Tuple[List[List[float]], List[List[float]]]:
    n = len(graph)
    mst = [[0] * n for _ in range(n)]
    mst_weights = [[float('inf')] * n for _ in range(n)]
    visited = [False] * n
    pq = [(0, 0, None)]  # (weight, vertex, parent)

    while pq:
        w, v, parent = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        if parent is not None:
            mst[v][parent] = mst[parent][v] = w
            mst_weights[v][parent] = mst_weights[parent][v] = weights[v][parent]

        for u, weight in enumerate(weights[v]):
            if weight != float('inf') and not visited[u]:
                heapq.heappush(pq, (weight, u, v))

    return mst, mst_weights