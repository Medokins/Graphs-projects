import sys
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory

from helpers import *
from Lab1.helpers import *

# Ad. 1
print("Ad 1")
randomDigrafAdjMatrix = randomDigraf(10, 0.2, consistent=True)
print_data(randomDigrafAdjMatrix)
showDigraf(randomDigrafAdjMatrix)

# Ad. 2
print("Ad 2")
print(kosaraju(randomDigrafAdjMatrix))
print()

# Ad. 3
print("Ad 3")
while True:
    size = 5
    randomGraph = randomDigraf(size, 0.3, consistent=True)
    showDigraf(randomGraph)
    isStronglyConnectedGraph = kosaraju(randomGraph)

    if len(isStronglyConnectedGraph) == 1:
        convertedToEdgesList = convert_to_edges(randomGraph)
        print(convertedToEdgesList)

        edgesValues = [np.random.randint(-5, 10) for _ in range(len(convertedToEdgesList))]
        print(edgesValues)
        show_weighted_graph(convertedToEdgesList, edgesValues)

        res = bellman_ford(convertedToEdgesList, edgesValues, 2)
        if type(res) is not bool:
            print(res[:size])

        break


# # Ad. 4
# print("Ad 4")
# while True:
#     size = 5
#     randomGraph = randomDigraf(size, 0.8)
#     showDigraf(randomGraph)
#     isStronglyConnectedGraph = kosaraju(randomGraph)
#
#     if len(isStronglyConnectedGraph) == 1:
#         convertedToEdgesList = convert_to_edges(randomGraph)
#         edgesValues = [np.random.randint(-1, 10) for _ in range(len(convertedToEdgesList))]
#
#         graph = johnson(convertedToEdgesList, edgesValues, size)
#         print(graph)
#
#         break