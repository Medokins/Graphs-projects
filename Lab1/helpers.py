import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random


def read_data(filename, indexing=True):
    with open(filename) as f:
        lines = f.readlines()

    data = []
    for line in lines:
        if indexing:
            arr = line.split()[1:]
            data.append([int(val) for val in arr])
        else:
            arr = line.split()[1:]
            data.append([int(val) for val in arr])

    return data

def print_data(data):
    for row in data:
        print(row)
    print()

def draw_graph(data, type="adjacency_matrix"):
    if type == "adjacency_matrix":
        pass
    elif type == "adjacency_list":
        data = convert_from_adjacency_list_to_adjacency_matrix(data)
    elif type == "incidence_matrix":
        data = convert_from_incidence_to_adjacency_matrix(data)
    else:
        print("Wrong type!")

    adjacency_matrix = np.array([np.array(x) for x in data])
    G2 = nx.from_numpy_array(adjacency_matrix)
    nx.draw_circular(G2, with_labels = True)
    plt.axis('equal')
    plt.show()

def convert_from_adjacency_matrix_to_incidence(data):
    incidence_matrix = []
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if (data[i][j] == 1):
                col = [1 if k == i or k == j else 0 for k in range(len(data))]
                incidence_matrix.append(col)

    return np.transpose(incidence_matrix)

def convert_from_adjacency_matrix_to_adjacency_list(data):
    adjacency_list = []
    for i in range(len(data)):
        neighbors = []
        for j in range(len(data[i])):
            if data[i][j] != 0:
                neighbors.append(j + 1)
        
        adjacency_list.append(neighbors)
    
    return adjacency_list

def convert_from_incidence_to_adjacency_matrix(data):
    num_vertices = len(data)
    num_edges = len(data[0])
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for j in range(num_edges):
        edge = []
        for i in range(num_vertices):
            if data[i][j] != 0:
                edge.append(i)
        if len(edge) == 2:
            adj_matrix[edge[0]][edge[1]] = 1
            adj_matrix[edge[1]][edge[0]] = 1
    return adj_matrix

def convert_from_adjacency_list_to_adjacency_matrix(data):
    n = len(data)
    adjacency_matrix = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in data[i-1]:
            adjacency_matrix[i][j] = 1

    corrected_adjacency_matrix = []
    for i in range(1 ,len(adjacency_matrix)):
        corrected_adjacency_matrix.append(adjacency_matrix[i][1:])

    return corrected_adjacency_matrix

def convert_from_incidence_to_adjacency_list(data):
    adjacency_matrix = convert_from_incidence_to_adjacency_matrix(data)
    return convert_from_adjacency_matrix_to_adjacency_list(adjacency_matrix)

def convert_from_adjacency_list_to_incidence(data):
    adjacency_matrix = convert_from_adjacency_list_to_adjacency_matrix(data)
    return convert_from_adjacency_matrix_to_incidence(adjacency_matrix)

def generate_random_graph(n, l):
    if l > n * (n - 1) / 2:
        raise ValueError("Liczba krawędzi jest większa niż liczba krawędzi w grafie pełnym.")
    
    adj_matrix = [[0] * n for _ in range(n)]
    
    edges = []
    while len(edges) < l:
        u, v = random.sample(range(n), 2)
        if adj_matrix[u][v] == 0 and u != v:
            edges.append((u, v))
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1
    
    return adj_matrix

def generate_random_graph_2(n, p):
    adj_matrix = [[0] * n for _ in range(n)]
    
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:
                adj_matrix[u][v] = 1
                adj_matrix[v][u] = 1
    
    return adj_matrix