from helpers import *

# Ad.1
print('adjacency_matrix:')
adjacency_matrix = read_data("adjacency_matrix.txt")
print_data(adjacency_matrix)

print('adjacency_matrix to adjacency_list')
adjacency_list = convert_from_adjacency_matrix_to_adjacency_list(adjacency_matrix)
print_adj_list(adjacency_list)

print('adjacency_matrix to incidence_matrix')
incidence_matrix = convert_from_adjacency_matrix_to_incidence(adjacency_matrix)
print_data(incidence_matrix)

print('='*40)
# ==========================

print('adjacency_list:')
adjacency_list = read_data("adjacency_list.txt")
print_adj_list(adjacency_list)

print('adjacency_list to adjacency_matrix')
adjacency_matrix = convert_from_adjacency_list_to_adjacency_matrix(adjacency_list)
print_data(adjacency_matrix)

print('adjacency_list to incidence_matrix')
incidence_matrix = convert_from_adjacency_list_to_incidence(adjacency_list)
print_data(incidence_matrix)

print('='*40)
# ==========================

print('incidence_matrix:')
incidence_matrix = read_data("incidence_matrix.txt")
print_data(incidence_matrix)

print('incidence_matrix to adjacency_matrix')
adjacency_matrix = convert_from_incidence_to_adjacency_matrix(incidence_matrix)
print_data(adjacency_matrix)

print('incidence_matrix to adjacency_list')
adjacency_list = convert_from_incidence_to_adjacency_list(incidence_matrix)
print_adj_list(adjacency_list)

print('='*40)
# ==========================

# Ad.2
adjacency_matrix = read_data("adjacency_matrix.txt")
draw_graph(adjacency_matrix)

# Ad.3
adj_matrix = generate_random_graph(10, 25)
draw_graph(adj_matrix)
adj_matrix = generate_random_graph_2(10, 0.5)
draw_graph(adj_matrix)