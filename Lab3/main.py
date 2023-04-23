from helpers import *
from Lab1.helpers import convert_from_adjacency_matrix_to_adjacency_list

# Ad. 1
print("Ad. 1")
adj_matrix, weight_matrix = makeRandomWeightGraph(10, 0.2, 1, 10)
show_graph(convert_adj_list_from_1_to_0_start(convert_from_adjacency_matrix_to_adjacency_list(adj_matrix)), weight_matrix)

# Ad. 2
print("\nAd. 2")
graph = [    
    [1, 2],         # 0
    [0, 2, 3],      # 1
    [0, 1, 3, 4],   # 2
    [1, 2, 4],      # 3
    [3, 2]          # 4
]

weights = [
    #       0             1         2            3               4
    [       0,            20,        4,      float('inf'),   float('inf')], # 0
    [       20,            0,        15,           5,         float('inf')], # 1
    [       4,            15,       0,           1,              3      ], # 2
    [float('inf'),        5,        1,           0,              2      ], # 3
    [float('inf'),  float('inf'),   3,           2,              0      ]  # 4
]

start_vertex = 0
lengths, predecessors = dijkstra(graph, weights, start_vertex)

paths = reconstruct_paths(predecessors, start_vertex)
for end_vertex, path in enumerate(paths):
    print(f"Shortest path from {start_vertex} to {end_vertex}: ")
    for node in path:
        if node != path[-1]:
            print(node, end=" -> ")
        else:
            print(node)
    print("")

for i, length in enumerate(lengths):
    print(f"Shortest path from node {start_vertex} to node {i} has a length of {length}")

show_graph(graph, weights)

# Ad. 3
print("\nAd. 3")
lengths_matrix = all_pairs_shortest_paths(graph, weights)
df = create_full_matrix(lengths_matrix)
center = center_of_graph(df)
print(f"Center: {center}")
show_graph(graph, weights)

# Ad. 4 
print("\nAd. 4")
minimax = center_of_graph_minimax(df)
print(f"Minmax: {minimax}")

# Ad. 5
print("\nAd. 5")
mst, we = prim(adj_matrix, weight_matrix)
show_graph(convert_adj_list_from_1_to_0_start(convert_from_adjacency_matrix_to_adjacency_list(mst)), we)