"""Community detection using the Girvan-Newman algorithm."""

from itertools import islice

import networkx as nx
from networkx.algorithms.community import girvan_newman


def first_girvan_newman_split(graph):
    """Return the first community split produced by Girvan-Newman."""
    communities_generator = girvan_newman(graph)
    first_split = next(communities_generator)
    return tuple(sorted(community) for community in first_split)


def girvan_newman_levels(graph, levels=3):
    """Return the first few hierarchical community splits."""
    communities_generator = girvan_newman(graph)

    result = []
    for communities in islice(communities_generator, levels):
        result.append(tuple(sorted(community) for community in communities))

    return result


if __name__ == "__main__":
    G = nx.karate_club_graph()

    print("First Girvan-Newman split:")
    for index, community in enumerate(first_girvan_newman_split(G), start=1):
        print(f"Community {index}:", community)

    print("\nFirst three hierarchical levels:")
    for level, communities in enumerate(girvan_newman_levels(G, levels=3), start=1):
        print(f"Level {level}:")
        for index, community in enumerate(communities, start=1):
            print(f"  Community {index}: {community}")

