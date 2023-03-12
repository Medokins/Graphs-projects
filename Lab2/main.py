import sys
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab1.helpers import draw_graph
from helpers import *
import networkx as nx

graphical_sequance_1 = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
graphical_sequance_2 = [6, 4, 4, 2, 2, 7, 4, 2, 7, 2, 2]
graphical_sequance_3 = [2, 1, 1, 2, 2, 2, 4]
graphical_sequance_4 = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
non_graphical_sequance = [4, 4, 3, 1, 2]

# print(f"Graphical: {is_graphical(graphical_sequance_1)}\nNon graphical: {is_graphical(non_graphical_sequance)}")

# adj_matrix = construct_graph(graphical_sequance_1)
# draw_graph(adj_matrix)
# randomized_graph = randomize_graph(graphical_sequance_1, 10)

# draw_graph(construct_graph(graphical_sequance_2))
# print(find_largest_connected_component(graphical_sequance_1))
# print(find_largest_connected_component(graphical_sequance_2))
# draw_graph(construct_graph(graphical_sequance_2))
# print(find_largest_connected_component(graphical_sequance_3))
# draw_graph(construct_graph(graphical_sequance_3))
# print(find_largest_connected_component(graphical_sequance_3))
# print(find_largest_connected_component(graphical_sequance_4))

euler_graph = [4, 2, 6, 2, 6, 2, 4, 2]
draw_graph(construct_graph(euler_graph))
print(f"Eulerian cycle: {find_Eulerian_cycle(euler_graph)}")



# k_regular_graph=generate_random_k_regular_graph(6,2)
# draw_graph(k_regular_graph)



## czy hamiltonowski
# graph_hamilton = [
#     [0, 1, 1],
#     [1, 0, 1],
#     [1, 1, 0]
# ]

# not_graph_hamilton = [
#     [0,  1,  1,  0,  0],
#     [1,  0,  1,  1,  0],
#     [1,  1,  0,  1 , 0],
#     [0,  1 , 1,  0 , 1],
#     [0 , 0 , 0,  1,  0]
# ]

# if (Hamiltonian_path(not_graph_hamilton, len(not_graph_hamilton))):
#     print("YES")
# else:
#     print("NO")
