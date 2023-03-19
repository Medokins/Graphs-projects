from helpers import show_graph, dijkstra

# Ad. 1
# Ad. 2
graph = {'A': {'B': 2, 'C': 5},
         'B': {'C': 1, 'D': 3},
         'C': {'D': 2, 'E': 4},
         'D': {'E': 1},
         'E': {'A': 1},
         'F': {'B': 3, 'D': 5}
         }

start = 'A'
distances = dijkstra(graph, start)

# Print the shortest distance from the starting node to all other nodes
for node, distance in distances.items():
    print(f"Shortest distance from {start} to {node}: {distance}")

show_graph(graph)

# Ad. 3
# Ad. 4
# Ad. 5
# Ad. 6