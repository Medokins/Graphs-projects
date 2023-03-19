import random
import numpy as np
from Lab1.helpers import *

# Ad. 1
def is_graphical(sequence) -> bool:
    sequence = sorted(sequence, reverse=True)
    while sequence[0] > 0:
        k = sequence[0]
        if k >= len(sequence):
            return False
        sequence = sequence[1:]
        for i in range(k):
            sequence[i] -= 1
        sequence = sorted(sequence, reverse=True)
        if sequence[-1] < 0:
            return False
    return True

def construct_graph(sequence) -> np.ndarray:
    if not is_graphical(sequence):
        raise ValueError("Sekwencja nie jest graficzna")

    # Create the adjacency matrix
    seq = sorted([[i, sequence[i]] for i in range(len(sequence))], reverse=True, key = lambda x: x[1])
    n = len(seq)
    adj_matrix = np.zeros((n, n))
    while seq[0][1] != 0:
        for pos in range(1, seq[0][1] + 1):
            seq[pos][1] -= 1
            adj_matrix[seq[0][0]][seq[pos][0]] = adj_matrix[seq[pos][0]][seq[0][0]] = 1
        seq[0][1] = 0
        seq = sorted(seq, reverse=True, key = lambda a: a[1])

    return adj_matrix

# Ad. 2
def switch_neighbours_of_vertex(randomized_graph, vertex, neighbor_vertex_to_remove, neighbour_vertex_to_add) -> None:
    vertex_neighbours = randomized_graph[vertex]
    vertex_neighbours.remove(neighbor_vertex_to_remove)
    vertex_neighbours.append(neighbour_vertex_to_add)
    randomized_graph[vertex] = vertex_neighbours

# changes edges (a, b) & (c, d) to (a, d) & (b, c)
def switch_edges_in_graph(randomized_graph, a, b, c, d) -> None:
    switch_neighbours_of_vertex(randomized_graph, a, b, d)
    switch_neighbours_of_vertex(randomized_graph, b, a, c)
    switch_neighbours_of_vertex(randomized_graph, c, d, b)
    switch_neighbours_of_vertex(randomized_graph, d, c, a)

def randomize_graph(sequence, num_iterations) -> np.ndarray: 
    adj_matrix = construct_graph(sequence)
    adj_list = convert_from_adjacency_matrix_to_adjacency_list(adj_matrix)
    
    # initialize dictionary
    randomized_graph = {}
    keyList = range(1, len(adj_list) + 1)
    for i in keyList:
        randomized_graph[i] = adj_list[i-1]
    
    num_vertices = len(randomized_graph)
    for _ in range(num_iterations):
        # randomly choose two edges to swap, random.sample chooses 2 different vertexes
        a, c = random.sample(range(1, num_vertices + 1), 2)
        a_neighbors = randomized_graph[a]
        c_neighbors = randomized_graph[c]

        # choose a random vertex from each list
        if len(a_neighbors) == 0 or len(c_neighbors) == 0:
            continue
        b = random.choice(a_neighbors)
        d = random.choice(c_neighbors)
        if b != c and a != d and b not in c_neighbors and d not in a_neighbors:
            switch_edges_in_graph(randomized_graph, a, b, c, d)

    return convert_from_adjacency_list_to_adjacency_matrix(list(randomized_graph.values()))

# Ad. 3
def find_largest_connected_component(adj_matrix) -> list: # graph to dictionary (lista sasiedztwa) trzeba przerobic 
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
def create_random_Eulerian_graph(nodes) -> np.ndarray:
    if nodes < 3:
        raise ValueError("Graf nie jest Eulerowski")

    sequence = [random.randint(1, np.floor((nodes-1)/2)) * 2 for _ in range(nodes)]
    while not is_graphical(sequence):
        sequence = [random.randint(1, np.floor((nodes-1)/2)) * 2 for _ in range(nodes)]

    adj_matrix = randomize_graph(sequence, 10)
    while len(find_largest_connected_component(adj_matrix)) != nodes:
        adj_matrix = randomize_graph(sequence, 10)

    return adj_matrix

def find_Eulerian_cycle(adj_matrix) -> list:
    adj_list = convert_from_adjacency_matrix_to_adjacency_list(adj_matrix)
    keyList = range(1, len(adj_list) + 1)
    graph = {}
    for i in keyList:
        graph[i] = adj_list[i-1]

    euler_sequence = [1]
    while not adj_list_empty(graph):
        for next_neighbour in graph[euler_sequence[-1]]:
            if edge_is_bridge(euler_sequence[-1], next_neighbour, graph):
                continue
            else:
                graph[euler_sequence[-1]].remove(next_neighbour)
                graph[next_neighbour].remove(euler_sequence[-1])
                euler_sequence.append(next_neighbour)
                break
        else:
            break
    
    # to make pycle more visible on drawing
    for i in range(len(euler_sequence)):
        euler_sequence[i] -= 1
    return euler_sequence

def adj_list_empty(graph) -> bool:
    for row in graph.values():
        if len(row) != 0:
            return False
    return True

def edge_is_bridge(a, b, graph) -> bool:
    graph[a].remove(b)
    graph[b].remove(a)

    visited = set()
    component = []
    dfs(graph, visited, a, component)

    graph[a].append(b)
    graph[b].append(a)

    return b not in visited and len(graph[a]) != 1

# Ad. 5
def generate_random_k_regular_graph(n,k) -> np.ndarray:
    if n*k % 2 != 0 and k>=n:
        raise ValueError("The product of n and k must be even")
    
    sequence = [k for _ in range(n)]
    adj_matrix = randomize_graph(sequence, 100)
    
    return adj_matrix

# Ad. 6
def isSafe(graph, v, pos, path):
    if graph[path[pos-1]][v] == 0:
        return False

    for vertex in path:
        if vertex == v:
            return False

    return True


def hamCycleUtil(graph, path, pos, V):
    if pos == V:
        if graph[path[pos-1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(1, V):
        if isSafe(graph, v, pos, path):
            path[pos] = v

            if hamCycleUtil(graph, path, pos+1, V):
                return True

            path[pos] = -1

    return False


def hamCycle(graph, V):
    path = [-1] * V
    path[0] = 0

    if hamCycleUtil(graph, path, 1, V) == False:
        print("Solution does not exist\n")
        return False

    printSolution(path)
    return True


def printSolution(path):
    print("Solution Exists: Following is one Hamiltonian Cycle")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0], "\n")
