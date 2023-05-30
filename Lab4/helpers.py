import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys
import copy
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab2.helpers import find_largest_connected_component

# Ad. 1
def convertDigraphToBasic(adj_matrix):
    basicGraph = adj_matrix

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if basicGraph[i][j] == 1:
                basicGraph[j][i] = 1
    return basicGraph

def randomDigraf(node_count, probability, consistent = False):
    edges = []

    while True:
        for i in range(node_count):
            for j in range(node_count):
                if i != j and np.random.rand() < probability:
                    edges.append([i, j])
        
        if len(edges) != 0:
            basicGraph = convertDigraphToBasic(convert_to_adjacency_matrix(edges))
            if len(basicGraph) == node_count:
                if not consistent or len(find_largest_connected_component(basicGraph)) == node_count:
                    break

        edges = []
    return convert_to_adjacency_matrix(edges)

def showDigraf(adj_matrix):
    G = nx.DiGraph()
    for i in range(len(adj_matrix)):
        G.add_node(i)

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                    G.add_edge(i, j)

    pos = nx.circular_layout(G)

    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    plt.show()

def show_weighted_graph(edges, weights):
    G = nx.DiGraph()

    numOfNodes = 0
    for edge in edges:
        n = max(edge[0], edge[1])
        if numOfNodes < n:
            numOfNodes = n

    for i in range(n):
        G.add_node(i)

    for i, edge in enumerate(edges):
        u, v = edge
        weight = weights[i]
        G.add_edge(u, v, label=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.savefig('plot.png')
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

    if n != len(adjacency_matrix[0]):
        raise ValueError("Input adjacency matrix is not square")

    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(adjacency_matrix, visited, stack, i)

    transposed_matrix = transpose(adjacency_matrix)

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
    max_node = max(max(edge) for edge in edges)

    adjacency_matrix = [[0] * (max_node + 1) for _ in range(max_node + 1)]
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

def convertEdgesToNeighborList(edges_list):

    neighbor_dict = {}

    for u, v in edges_list:
        if u not in neighbor_dict:
            neighbor_dict[u] = []
        neighbor_dict[u].append(v)

        if v not in neighbor_dict:
            neighbor_dict[v] = []
        neighbor_dict[v].append(u)

    neighbor_list = [v for k, v in neighbor_dict.items()]

    return neighbor_list

def bellman_ford(edges, values, start):
    n = len(edges)
    dist = np.full(n, np.inf)
    dist[start] = 0

    for i in range(n-1):
        for j, (u, v) in enumerate(edges):
            if dist[u] + values[j] < dist[v]:
                dist[v] = dist[u] + values[j]

    for j, (u, v) in enumerate(edges):
        if dist[u] + values[j] < dist[v]:
            print("Negative cycle detected in graph")
            return False

    return dist

def add_s(edges_list, edgesValues, nodesCount):
    copied = copy.deepcopy(edges_list)
    copiedEdgesValues = copy.deepcopy(edgesValues)
    copied.extend([nodesCount, index] for index in range(nodesCount))
    copiedEdgesValues.extend([0 for _ in range(nodesCount)])
    return copied, copiedEdgesValues
