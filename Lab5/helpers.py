import random
import networkx as nx
import matplotlib.pyplot as plt

#Ad. 1
def generate_random_flow_network(layers):
    G = nx.DiGraph()

    source_node = 0
    G.add_node(source_node, layer=0)

    node_id = 1
    num_nodes = 0

    for i in range(1, layers + 1):
        layer_nodes = random.randint(2, layers)
        num_nodes += layer_nodes
        for _ in range(layer_nodes):
            G.add_node(node_id, layer=i)
            node_id += 1

    sink_node = node_id
    G.add_node(sink_node, layer=layers + 1)

    for i in range(layers + 1):
        current_layer_nodes = [node for node in G.nodes if G.nodes[node]['layer'] == i]
        next_layer_nodes = [node for node in G.nodes if G.nodes[node]['layer'] == i + 1]

        for node in current_layer_nodes:
            if next_layer_nodes:
                target_node = random.choice(next_layer_nodes)
                G.add_edge(node, target_node, capacity=0, flow=0)
                next_layer_nodes.remove(target_node)
            else:
                break

    all_nodes = list(G.nodes)
    all_nodes.remove(source_node)
    all_nodes.remove(sink_node)

    for _ in range(2 * layers):
        source_node = random.choice(all_nodes)
        target_node = random.choice(all_nodes)
        while target_node == source_node or G.has_edge(source_node, target_node):
            target_node = random.choice(all_nodes)

        G.add_edge(source_node, target_node, capacity=0, flow=0)

    for u, v in G.edges:
        G.edges[u, v]['capacity'] = random.randint(1, 10)

    return G, num_nodes



def draw_flow_network(G):
    pos = nx.multipartite_layout(G, subset_key='layer', align='vertical')
    capacities = nx.get_edge_attributes(G, 'capacity')

    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue')

    # to make labels readable on crossing edges
    edge_labels = nx.draw_networkx_edge_labels(G, pos, edge_labels=capacities, label_pos=0.3)
    for _, label in edge_labels.items():
        label.set_bbox({'boxstyle': 'round', 'ec': 'none', 'fc': 'white'})

    plt.title("Losowa sieć przepływowa")
    plt.axis("off")
    plt.show()



# Ad. 2
def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = []

    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)

        for v, capacity in enumerate(graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True

    return False


def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = parent[v]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow, graph