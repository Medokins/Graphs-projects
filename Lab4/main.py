from helpers import *
import sys
sys.path.append("./") # for running from root
sys.path.append("..") # for running from curent directory
from Lab1.helpers import print_data
from Lab3.helpers import show_graph

# Ad. 1
randomDigrafAdjMatrix = makeRandomDigraf(5, 0.5)
print_data(randomDigrafAdjMatrix)
showDigraf(randomDigrafAdjMatrix)

# Ad. 2
G = {0: [1], 1: [2], 2: [0, 3], 3: []}
print(kosaraju(G))
# Ad. 3

# Ad. 4