from helpers import *
import sys
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab1.helpers import *
import numpy as np

# Ad. 1
layers = 3
G, number_of_nodes = generate_random_flow_network(layers)
draw_flow_network(G)

# Ad. 2
edges = []
for u, v, attr in G.edges(data=True):
    edges.append((u, v, attr['capacity']))

graph_matrix = np.zeros((number_of_nodes + 2, number_of_nodes + 2), dtype=int)
for edge in edges:
    column, row, weight = edge
    graph_matrix[column][row] = weight

source = 0
sink = number_of_nodes + 1
max_flow, matrix = ford_fulkerson(graph_matrix, source, sink)
print(f"Max flow is: {max_flow}")