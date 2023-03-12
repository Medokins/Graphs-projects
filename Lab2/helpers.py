import random
from Lab1.helpers import convert_from_adjacency_matrix_to_adjacency_list

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
        return None

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
def randomize_graph(sequence, num_iterations):
    adj_matrix = construct_graph(sequence)
    graph = convert_from_adjacency_matrix_to_adjacency_list(adj_matrix)

    # print(adj_matrix)
    # for _ in range(numberOfRandomisations):
    #     pass

    randomized_graph = dict(graph)  # create a copy of the original graph
    num_vertices = len(graph)

    for iteration in range(num_iterations):
        # randomly choose two edges to swap
        u, v = random.sample(range(num_vertices), 2)
        u_neighbors = randomized_graph[u]
        v_neighbors = randomized_graph[v]

        # choose a random vertex from each list
        u_neighbor = random.choice(u_neighbors)
        v_neighbor = random.choice(v_neighbors)

        # make sure the new edges don't already exist
        if u_neighbor != v and v_neighbor != u and u_neighbor not in v_neighbors and v_neighbor not in u_neighbors:
            # swap the edges
            u_neighbors.remove(u_neighbor)
            u_neighbors.append(v_neighbor)
            v_neighbors.remove(v_neighbor)
            v_neighbors.append(u_neighbor)
            randomized_graph[u] = u_neighbors
            randomized_graph[v] = v_neighbors

    return randomized_graph

# Ad. 3
def find_connected_components(sequnace):
    pass

# Ad. 4
def create_random_Eulerian_graph():
    pass

def find_Eulerian_cycle(sequence):
    pass

# Ad. 5
def generate_random_k_regular_graph():
    pass

# Ad. 6
def is_Hamiltionian(sequence):
    pass