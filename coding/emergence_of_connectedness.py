"""Simulate the emergence of connectedness in a random graph."""

import random
from math import log

import networkx as nx


def create_empty_graph(n):
    """Create a graph with n isolated nodes and no edges."""
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    return graph


def add_random_edge(graph):
    """Add one random edge between two distinct nodes."""
    v1, v2 = random.sample(list(graph.nodes()), 2)
    graph.add_edge(v1, v2)
    return graph


def add_edges_until_connected(n, seed=None):
    """Return the number of edges needed until the graph becomes connected."""
    if seed is not None:
        random.seed(seed)

    graph = create_empty_graph(n)

    while not nx.is_connected(graph):
        add_random_edge(graph)

    return graph.number_of_edges(), graph


if __name__ == "__main__":
    number_of_nodes = 100
    edge_count, G = add_edges_until_connected(number_of_nodes, seed=7)

    print(f"Nodes: {number_of_nodes}")
    print(f"Edges needed for connectedness in this run: {edge_count}")
    print(f"n log n approximation: {number_of_nodes * log(number_of_nodes):.0f}")
    print("Connected?", nx.is_connected(G))
