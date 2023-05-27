from helpers import *
import numpy as np
import sys
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab1.helpers import *

# Ad. 1
layers = 2
G = generate_random_flow_network(layers)
draw_flow_network(G)

# Ad. 2
graph_matrix = np.zeros((len(G.nodes), len(G.nodes)), dtype=int)
nodes = sorted(G.nodes)
for u, v, attr in G.edges(data=True):
    u_idx = nodes.index(u)
    v_idx = nodes.index(v)
    capacity = attr['capacity']
    graph_matrix[u_idx][v_idx] = capacity

source = 0
sink = layers
max_flow, matrix = ford_fulkerson(graph_matrix, source, sink)
# TO DO, write a function to draw max flow path
print(max_flow)