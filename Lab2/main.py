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

# print(f"Graphical: {is_graphical(graphical_sequance)}\nNon graphical: {is_graphical(non_graphical_sequance)}")

adj_matrix = construct_graph(graphical_sequance)
randomized_graph = randomize_graph(graphical_sequance, 10)

draw_graph(adj_matrix)
print(find_largest_connected_component(graphical_sequance))