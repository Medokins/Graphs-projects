from helpers import *
import sys
import copy
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab1.helpers import *
from Lab3.helpers import show_graph, dijkstra


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

def convertEdgesToNeighborList(edges_list):

    neighbor_dict = {}

    for u, v in edges_list:
        # Add u as a neighbor of v
        if u not in neighbor_dict:
            neighbor_dict[u] = []
        neighbor_dict[u].append(v)

        # Add v as a neighbor of u
        if v not in neighbor_dict:
            neighbor_dict[v] = []
        neighbor_dict[v].append(u)

    neighbor_list = [v for k, v in neighbor_dict.items()]

    return neighbor_list




def add_s(edges_list, edgesValues, nodesCount):
    edgesLen = len(edges_list)
    G_prim = copy.deepcopy(edges_list)
    G_prim_edgesValues = copy.deepcopy(edgesValues)
    G_prim.extend([nodesCount, index] for index in range(nodesCount))
    G_prim_edgesValues.extend([0 for _ in range(nodesCount)])
    return G_prim,G_prim_edgesValues

def johnson(edges_list, edgesValues, nodesCount):
    edgesLen = len(edges_list)

    G_prim_edges, G_prim_edgesValues = add_s(edges_list, edgesValues, nodesCount)

    d = bellman_ford(G_prim_edges, G_prim_edgesValues, nodesCount)

    if d == False:
        return False

    h = copy.deepcopy(d)
    w_prim = [
        edgesValues[i] + h[edges_list[i][0]] - h[edges_list[i][1]]
        for i in range(edgesLen)
    ]

    D = np.zeros((nodesCount, nodesCount), dtype="int")

    neighbour_list = convertEdgesToNeighborList(edges_list)
    d_prim = [dijkstra(neighbour_list, w_prim, i)[0] for i in range(nodesCount)]

    D = [ [d_prim[i][j] + h[j] - h[i] for j in range(nodesCount)] for i in range(nodesCount) ]

    return D


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
print("Ad 4")
while True:
    size = 5
    randomGraph = generateDigraph(size, 0.8)
    showDigraf(randomGraph)
    isStronglyConnectedGraph = kosaraju(randomGraph)
    print(isStronglyConnectedGraph)
    if len(isStronglyConnectedGraph) == 1:
        convertedToEdgesList = convert_to_edges(randomGraph)
        edgesValues = [np.random.randint(-1, 10) for _ in range(len(convertedToEdgesList))]

        graph = johnson(convertedToEdgesList, edgesValues, size)
        print(graph)

        break

