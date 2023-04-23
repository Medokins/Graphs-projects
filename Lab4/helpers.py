import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys
import copy
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab3.helpers import dijkstra

# Ad. 1
def generateDigraph(node_count, probability):
    if probability < 0 or probability > 1:
        sys.exit("Wrong randomization arguments")

    edges = []

    while True:
        for i in range(0, node_count):
            for j in range(0, node_count):
                if i != j:
                    rand = np.random.rand()

                    if rand < probability:
                        edges.append([i, j])

        maxList = map(max, edges)
        maxNode = max(maxList, default=-1)

        if maxNode == node_count - 1:
            break

        edges = []
    return convert_to_adjacency_matrix(edges)

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

def dfs(graph, visited, stack, node):
    visited[node] = True
    for i in range(len(graph)):
        if graph[node][i] == 1 and not visited[i]:
            dfs(graph, visited, stack, i)
    stack.append(node)


def transpose(graph):
    return [list(row) for row in zip(*graph)]


def kosaraju(adjacency_matrix):
    n = len(adjacency_matrix)

    # Check if the adjacency matrix is square
    if n != len(adjacency_matrix[0]):
        raise ValueError("Input adjacency matrix is not square")

    # Step 1: Perform depth-first search to fill the stack
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(adjacency_matrix, visited, stack, i)

    # Step 2: Transpose the adjacency matrix
    transposed_matrix = transpose(adjacency_matrix)

    # Step 3: Perform depth-first search on the transposed graph to find strongly connected components
    visited = [False] * n
    strongly_connected_components = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs(transposed_matrix, visited, component, node)
            strongly_connected_components.append(component)

    return strongly_connected_components


# Ad. 3

def convert_to_adjacency_matrix(edges):
    # Find the highest node number in the list of edges
    max_node = max(max(edge) for edge in edges)

    # Initialize a matrix filled with zeros
    adjacency_matrix = [[0] * (max_node + 1) for _ in range(max_node + 1)]

    # Set the values in the adjacency matrix based on the edges
    for edge in edges:
        adjacency_matrix[edge[0]][edge[1]] = 1

    return adjacency_matrix


def convert_to_edges(adjacency_matrix):
    edges = []
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                edges.append([i, j])
    return edges

def bellman_ford(edges_list, edgesValues, s): # todo sparafrazowac w chatgpt bo zajebane
    edgesLen = len(edges_list)
    distance = [np.inf for _ in range(edgesLen)]
    distance[s] = 0

    for _ in range(edgesLen - 1):
        for i in range(len(edges_list)):
            if distance[edges_list[i][1]] > distance[edges_list[i][0]] + edgesValues[i]:
                distance[edges_list[i][1]] = distance[edges_list[i][0]] + edgesValues[i]

    for i in range(len(edges_list)):
        if distance[edges_list[i][1]] > distance[edges_list[i][0]] + edgesValues[i]:
            print("Graph contains negative cycle")
            return False

    return distance

def convertEdgesToNeighborList(edges_list):

    neighbor_dict = {}

    for u, v in edges_list:
        # Add u as a neighbor of v
        if u not in neighbor_dict:
            neighbor_dict[u] = []
        neighbor_dict[u].append(v)

        # Add v as a neighbor of u
        if v not in neighbor_dict:
            neighbor_dict[v] = []
        neighbor_dict[v].append(u)

    neighbor_list = [v for k, v in neighbor_dict.items()]

    return neighbor_list

def add_s(edges_list, edgesValues, nodesCount):
    edgesLen = len(edges_list)
    G_prim = copy.deepcopy(edges_list)
    G_prim_edgesValues = copy.deepcopy(edgesValues)
    G_prim.extend([nodesCount, index] for index in range(nodesCount))
    G_prim_edgesValues.extend([0 for _ in range(nodesCount)])
    return G_prim,G_prim_edgesValues

def johnson(edges_list, edgesValues, nodesCount):
    edgesLen = len(edges_list)

    G_prim_edges, G_prim_edgesValues = add_s(edges_list, edgesValues, nodesCount)

    d = bellman_ford(G_prim_edges, G_prim_edgesValues, nodesCount)

    if d == False:
        return False

    h = copy.deepcopy(d)
    w_prim = [
        edgesValues[i] + h[edges_list[i][0]] - h[edges_list[i][1]]
        for i in range(edgesLen)
    ]

    D = np.zeros((nodesCount, nodesCount), dtype="int")

    neighbour_list = convertEdgesToNeighborList(edges_list)
    d_prim = [dijkstra(neighbour_list, w_prim, i)[0] for i in range(nodesCount)]

    D = [ [d_prim[i][j] + h[j] - h[i] for j in range(nodesCount)] for i in range(nodesCount) ]

    return D
# Ad. 4