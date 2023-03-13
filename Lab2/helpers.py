import random
import numpy as np
from Lab1.helpers import *

# Ad. 1
def is_graphical(sequence) -> bool:
    sequence = sorted(sequence, reverse=True)
    while sequence[0] > 0:
        k = sequence[0]
        if k > len(sequence):
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
    seq = sorted(sequence, reverse=True)
    n = len(seq)
    adj_matrix = np.zeros((n, n))
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
def create_random_Eulerian_graph(nodes):
    if nodes < 3:
        raise ValueError("Graf nie jest Eulerowski")

    sequence = []
    for _ in range(nodes):
        sequence.append(random.randint(1, np.floor((nodes-1)/2)) * 2)

    while not is_graphical(sequence) or len(find_largest_connected_component(sequence)) != nodes:
        sequence = []
        for _ in range(nodes):
            sequence.append(random.randint(1, np.floor((nodes-1)/2)) * 2)
    return sequence

def find_Eulerian_cycle(sequence):
    adj_matrix = construct_graph(sequence)
    adj_list = convert_from_adjacency_matrix_to_adjacency_list(adj_matrix)
    keyList = range(1, len(adj_list) + 1)
    graph = {}
    for i in keyList:
        graph[i] = adj_list[i-1]

    euler_sequence = [1]
    while not adj_list_empty(graph):
        for next_neighbour in graph[euler_sequence[-1]]:
            graph[euler_sequence[-1]].pop(0)
            graph[next_neighbour].remove(euler_sequence[-1])
            if edge_is_bridge(euler_sequence[-1], next_neighbour, graph):
                pass
            else:
                euler_sequence.append(next_neighbour)
                break
        else:
            break
    
    return euler_sequence

def adj_list_empty(graph):
    for row in graph.values():
        if len(row) != 0:
            return False
    return True

def edge_is_bridge(a, b, graph):
    visited = set()
    for v in graph:
        if v not in visited:
            component = []
            dfs(graph, visited, v, component)

# Ad. 5
def generate_random_k_regular_graph(n,k):
    if n*k % 2 != 0 and k>=n:
        raise ValueError("The product of n and k must be even")
    
    # Create an empty adjacency matrix
    adj_matrix = np.zeros((n,n), dtype=int)
    
    # Create a list of all possible edges
    all_edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    
    # Shuffle the list of edges
    np.random.shuffle(all_edges)
    
    # Create a dictionary to keep track of the degree of each node
    degree = {i: 0 for i in range(n)}
    
    # Loop over the shuffled list of edges until all nodes have degree k
    for edge in all_edges:
        if degree[edge[0]] < k and degree[edge[1]] < k:
            adj_matrix[edge[0], edge[1]] = 1
            adj_matrix[edge[1], edge[0]] = 1
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        
        if all(d == k for d in degree.values()):
            break
    
    return adj_matrix

# Ad. 6
def Hamiltonian_path(adj, N):
     
    dp = [[False for i in range(1 << N)]
                 for j in range(N)]
 
    # Set all dp[i][(1 << i)] to
    # true
    for i in range(N):
        dp[i][1 << i] = True
 
    # Iterate over each subset
    # of nodes
    for i in range(1 << N):
        for j in range(N):
 
            # If the jth nodes is included
            # in the current subset
            if ((i & (1 << j)) != 0):
 
                # Find K, neighbour of j
                # also present in the
                # current subset
                for k in range(N):
                    if ((i & (1 << k)) != 0 and
                             adj[k][j] == 1 and
                                     j != k and
                          dp[k][i ^ (1 << j)]):
                         
                        # Update dp[j][i]
                        # to true
                        dp[j][i] = True
                        break
     
    # Traverse the vertices
    for i in range(N):
 
        # Hamiltonian Path exists
        if (dp[i][(1 << N) - 1]):
            return True
 
    # Otherwise, return false
    return False