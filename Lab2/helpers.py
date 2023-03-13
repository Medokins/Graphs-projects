import random
import numpy as np
from Lab1.helpers import *
from itertools import permutations

# Ad. 1
def is_graphical(sequence):
    sequence = sorted(sequence, reverse=True)
    while sequence[0] > 0:
        k = sequence[0]
        if k >= len(sequence) or sequence[-1] < 0:
            return False
        sequence = sequence[1:]
        for i in range(k):
            sequence[i] -= 1
        sequence = sorted(sequence, reverse=True)
    return True

# return type should be one of the types from witch we can convert to adj_matrix
def construct_graph(sequence):
    # Sort the sequence in non-increasing order
    seq = sorted(sequence, reverse=True)

    if not is_graphical(sequence):
        raise ValueError("Sekwencja nie jest graficzna")

    # Create the adjacency matrix
    n = len(seq)
    adj_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if seq[i] > 0 and seq[j] > 0:
                seq[i] -= 1
                seq[j] -= 1
                adj_matrix[i][j] = adj_matrix[j][i] = 1

    return adj_matrix

# Ad. 2
def randomize_graph(sequence, num_iterations) -> np.ndarray: 
    adj_matrix = construct_graph(sequence)
    graph = convert_from_adjacency_matrix_to_adjacency_list(adj_matrix)
    keyList = range(1, len(graph) + 1)
    
    # initialize dictionary
    randomized_graph = {}
    
    # iterating through the elements of list
    for i in keyList:
        randomized_graph[i] = graph[i-1]
    
    num_vertices = len(graph)

    for _ in range(num_iterations):
        # randomly choose two edges to swap
        u, v = random.sample(range(1, num_vertices + 1), 2)
        u_neighbors = randomized_graph[u]
        v_neighbors = randomized_graph[v]

        # choose a random vertex from each list
        u_neighbor = random.choice(u_neighbors)
        v_neighbor = random.choice(v_neighbors)
        if u_neighbor != v and v_neighbor != u and u_neighbor not in v_neighbors and v_neighbor not in u_neighbors:
            u_neighbors.remove(u_neighbor)
            u_neighbors.append(v_neighbor)
            v_neighbors.remove(v_neighbor)
            v_neighbors.append(u_neighbor)
            randomized_graph[u] = u_neighbors 
            randomized_graph[v] = v_neighbors

            u_neighbors_neighbours = randomized_graph[u_neighbor]
            v_neighbors_neighbours = randomized_graph[v_neighbor]

            # if v_neighbor not in u_neighbors_neighbours and u not in v_neighbors_neighbours:
            u_neighbors_neighbours.append(v)
            u_neighbors_neighbours.remove(u)
            v_neighbors_neighbours.append(u)
            v_neighbors_neighbours.remove(v)
            randomized_graph[u_neighbor] = u_neighbors_neighbours
            randomized_graph[v_neighbor] = v_neighbors_neighbours
        
    adj_list = []
    for value in randomized_graph.values():
        adj_list.append(value)

    adj_matrix = convert_from_adjacency_list_to_adjacency_matrix(adj_list)
    upper_values = np.tril(adj_matrix)
    symmetric_matrix = upper_values + upper_values.T
    return symmetric_matrix

# Ad. 3
def find_largest_connected_component(sequence) -> list: # graph to dictionary (lista sasiedztwa) trzeba przerobic 
    adj_matrix = construct_graph(sequence)
    adj_list = convert_from_adjacency_matrix_to_adjacency_list(adj_matrix)

    keyList = range(1, len(adj_list) + 1)
    graph = {}
    
    # iterating through the elements of list
    for i in keyList:
        graph[i] = adj_list[i-1]
    
    visited = set()
    largest_component = []
    for v in graph:
        if v not in visited:
            component = []
            dfs(graph, visited, v, component)
            if len(component) > len(largest_component):
                largest_component = component
    return largest_component

def dfs(graph, visited, v, component):
    visited.add(v)
    component.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(graph, visited, neighbor, component)


# Ad. 4
def create_random_Eulerian_graph():
    pass

def find_Eulerian_cycle(sequance):
    pass

# Ad. 5
def generate_random_k_regular_graph():
    pass

# Ad. 6
def is_Hamiltionian(sequance):
    pass