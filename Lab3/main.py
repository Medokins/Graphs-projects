from helpers import dijkstra, show_graph

# Ad. 1

# Ad. 2
graph = [    
    [1, 2],         # 0
    [0, 2, 3],      # 1
    [0, 1, 3, 4],   # 2
    [1, 2, 4],      # 3
    [3, 2]          # 4
]

weights = [
    #       0             1         2            3               4
    [       0,            1,        4,      float('inf'),   float('inf')], # 0
    [       1,            0,        2,           5,         float('inf')], # 1
    [       4,            2,        0,           1,              3      ], # 2
    [float('inf'),        5,        1,           0,              2      ], # 3
    [float('inf'),  float('inf'),   3,           2,              0      ]  # 4
]

start_vertex = 0
lengths, predecessors = dijkstra(graph, weights, start_vertex)

for predecessor in predecessors:
    print(predecessor, end=" ")
    if predecessor != predecessors[-1]:
        print("->", end=" ")

for i, length in enumerate(lengths):
    print(f"Shorest path from node {start_vertex} to node {i} has a length of {length}")

show_graph(graph, weights)
# Ad. 3

# Ad. 4
# Ad. 5
# Ad. 6