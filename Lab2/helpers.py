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
def constuct_graph(sequnace):
    pass

# Ad. 2
def randomize_graph(sequance):
    pass

# Ad. 3
def find_connected_components(sequnace):
    pass

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