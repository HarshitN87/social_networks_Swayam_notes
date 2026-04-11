"""Brute-force two-community search for very small graphs.

The score used here is:

    intra-community edges / inter-community edges

This is useful for learning, but it is not scalable.
"""

from itertools import combinations

import networkx as nx


def two_community_partitions(nodes):
    """Generate unique two-way partitions of nodes.

    To avoid duplicate mirror partitions, only subsets up to half the graph are
    considered.
    """
    node_list = list(nodes)
    n = len(node_list)

    for size in range(1, (n // 2) + 1):
        for first in combinations(node_list, size):
            first_set = set(first)
            second_set = set(node_list) - first_set
            yield first_set, second_set


def partition_score(graph, first_community, second_community):
    """Return a simple score favoring many intra edges and few inter edges."""
    intra_1 = graph.subgraph(first_community).number_of_edges()
    intra_2 = graph.subgraph(second_community).number_of_edges()
    total_edges = graph.number_of_edges()
    inter_edges = total_edges - intra_1 - intra_2

    # Avoid division by zero. A perfect split gets an infinite score.
    if inter_edges == 0:
        return float("inf")

    return (intra_1 + intra_2) / inter_edges


def communities_bruteforce(graph):
    """Find the best two-community partition by exhaustive search."""
    best_partition = None
    best_score = float("-inf")

    for first, second in two_community_partitions(graph.nodes()):
        score = partition_score(graph, first, second)

        if score > best_score:
            best_score = score
            best_partition = (first, second)

    return best_partition, best_score


if __name__ == "__main__":
    G = nx.karate_club_graph()
    partition, score = communities_bruteforce(G.subgraph(range(8)).copy())

    print("Best partition for an 8-node sample:")
    print("Community 1:", sorted(partition[0]))
    print("Community 2:", sorted(partition[1]))
    print("Score:", score)

