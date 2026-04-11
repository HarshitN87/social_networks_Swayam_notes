"""Introductory NetworkX examples.

This file demonstrates the basic functions needed for the graph examples in
this knowledge base. Run it with:

    python coding/networkx_intro.py
"""

import networkx as nx


def build_small_graph():
    """Create and return a simple undirected graph."""
    graph = nx.Graph()

    # Add individual nodes.
    graph.add_node("A")
    graph.add_node("B")

    # Add several nodes at once.
    graph.add_nodes_from(["C", "D", "E"])

    # Add edges. NetworkX automatically creates missing endpoint nodes.
    graph.add_edge("A", "B")
    graph.add_edges_from([("B", "C"), ("C", "D"), ("D", "E")])

    return graph


def print_graph_summary(graph):
    """Print common graph properties."""
    print("Nodes:", list(graph.nodes()))
    print("Edges:", list(graph.edges()))
    print("Number of nodes:", graph.number_of_nodes())
    print("Number of edges:", graph.number_of_edges())
    print("Degree of each node:", dict(graph.degree()))
    print("Is connected?", nx.is_connected(graph))
    print("Connected components:", [list(c) for c in nx.connected_components(graph)])


def demonstrate_clustering(graph):
    """Show clustering coefficient calculations."""
    print("Local clustering coefficients:", nx.clustering(graph))
    print("Average clustering coefficient:", nx.average_clustering(graph))


def demonstrate_shortest_paths(graph):
    """Show shortest-path queries."""
    source = "A"
    target = "E"

    print(f"Shortest path from {source} to {target}:", nx.shortest_path(graph, source, target))
    print(
        f"Shortest path length from {source} to {target}:",
        nx.shortest_path_length(graph, source, target),
    )


if __name__ == "__main__":
    G = build_small_graph()
    print_graph_summary(G)
    demonstrate_clustering(G)
    demonstrate_shortest_paths(G)

