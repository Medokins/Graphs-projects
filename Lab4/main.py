from helpers import *
import sys
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab1.helpers import *
from Lab3.helpers import show_graph

def convert_to_edges(adjacency_matrix):
    edges = []
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                edges.append([i, j])
    return edges

def bellman_ford(edges_list, edgesValues, s): # todo sparafrazowac w chatgpt bo zajebane
    edgesLen = len(edges_list)
    distance = [np.inf for _ in range(edgesLen)]
    distance[s] = 0

    for _ in range(edgesLen - 1):
        for i in range(len(edges_list)):
            if distance[edges_list[i][1]] > distance[edges_list[i][0]] + edgesValues[i]:
                distance[edges_list[i][1]] = distance[edges_list[i][0]] + edgesValues[i]

    for i in range(len(edges_list)):
        if distance[edges_list[i][1]] > distance[edges_list[i][0]] + edgesValues[i]:
            print("Graph contains negative cycle")
            return False

    return distance

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
    print(isStronglyConnectedGraph)
    if len(isStronglyConnectedGraph) == 1:
        convertedToEdgesList = convert_to_edges(randomGraph)

        edgesValues = [np.random.randint(-5, 10) for _ in range(len(convertedToEdgesList))]

        res = bellman_ford(convertedToEdgesList, edgesValues, 2)
        if res:
            print(res[:size])

        break


# Ad. 4

