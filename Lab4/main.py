from helpers import *
import sys
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab1.helpers import *

# # Ad. 1
print("Ad 1")
randomDigrafAdjMatrix = generateDigraph(5, 0.5)
print_data(randomDigrafAdjMatrix)
showDigraf(randomDigrafAdjMatrix)

# Ad. 2
print("Ad 2")
print(kosaraju(randomDigrafAdjMatrix))

# Ad. 3
print("Ad 3")
while True:
    size = 5
    randomGraph = generateDigraph(size, 0.8)
    showDigraf(randomGraph)
    isStronglyConnectedGraph = kosaraju(randomGraph)

    if len(isStronglyConnectedGraph) == 1:
        convertedToEdgesList = convert_to_edges(randomGraph)

        edgesValues = [np.random.randint(-1, 10) for _ in range(len(convertedToEdgesList))]

        res = bellman_ford(convertedToEdgesList, edgesValues, 2)
        if type(res) is not bool:
            print(res[:size])

        break


# Ad. 4
print("Ad 4")
while True:
    size = 5
    randomGraph = generateDigraph(size, 0.8)
    showDigraf(randomGraph)
    isStronglyConnectedGraph = kosaraju(randomGraph)

    if len(isStronglyConnectedGraph) == 1:
        convertedToEdgesList = convert_to_edges(randomGraph)
        edgesValues = [np.random.randint(-1, 10) for _ in range(len(convertedToEdgesList))]

        graph = johnson(convertedToEdgesList, edgesValues, size)
        print(graph)

        break