import sys
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab1.helpers import draw_graph
from helpers import *

graphical_sequance = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
non_graphical_sequance = [4, 4, 3, 1, 2]

# Ad. 1
print(f"Ad. 1\nis graphical? {graphical_sequance}: {is_graphical(graphical_sequance)}\n"
      f"is graphical? {non_graphical_sequance}: {is_graphical(non_graphical_sequance)}")

adj_matrix = construct_graph(graphical_sequance)
draw_graph(adj_matrix)

# Ad. 2
randomized_graph = randomize_graph(graphical_sequance, 10)
print("\nAd. 2\nrandomize graph")
draw_graph(randomized_graph)

# Ad. 3
euler_graph = [4, 2, 6, 2, 6, 2, 4, 2]
print(f"\nAd. 3\nlargest_connected_component: {find_largest_connected_component(euler_graph)}")
draw_graph(construct_graph(euler_graph))

# Ad. 4
# should be create_random_Eulerian_graph(), for not using prepared eulerian_graph
print(f"\nAd. 4\nEulerian cycle: {find_Eulerian_cycle(euler_graph)}")

# Ad. 5
k_regular_graph=generate_random_k_regular_graph(6,2)
print("\nAd. 5\nk_regular_graph")
draw_graph(k_regular_graph)

# Ad. 6
hamiltonian_graph = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

non_hamiltonian_graph = [
    [0,  1,  1,  0,  0],
    [1,  0,  1,  1,  0],
    [1,  1,  0,  1 , 0],
    [0,  1 , 1,  0 , 1],
    [0 , 0 , 0,  1,  0]
]
# not working yet
print("\nAd. 6")
print("YES") if (Hamiltonian_path(non_hamiltonian_graph, len(non_hamiltonian_graph))) else print("NO")