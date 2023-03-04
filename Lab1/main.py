from helpers import *

adjacency_matrix = read_data("adjacency_matrix.txt")
adjacency_list = read_data("adjacency_list.txt")
incidence_matrix = read_data("incidence_matrix.txt")

adj_matrix = generate_random_graph_2(20, 1)
draw_graph(adj_matrix)