"""
Programming Illustration: Emergence of Connectedness

Corrected to utilize proper capitalization and correct NetworkX functions.
Demonstrates the threshold of graph connectedness when randomly generating edges.
"""

import networkx as nx
import random
import sys

def add_nodes(n):
    """Initializes a graph with n distinctly disconnected nodes."""
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G

def add_random_edge(G):
    """Selects two uniform random nodes distinctively and writes an edge."""
    nodes = list(G.nodes())
    
    # Avoid errors if no nodes exist
    if not nodes:
        return G
        
    v1 = random.choice(nodes)
    v2 = random.choice(nodes)
    
    # Ensure no self-loop connections block calculations
    while v1 == v2:
        v2 = random.choice(nodes)
        
    G.add_edge(v1, v2)
    return G

def add_edges_till_connect(n):
    """Persistently triggers random edges safely until component lock is achieved."""
    # Start the graph with requested 'n' isolated nodes
    G = add_nodes(n)
    
    # nx.is_connected raises an error if graph has zero nodes
    if n == 0:
        return 0
        
    # We sequence endlessly until boolean connectivity flags true
    while not nx.is_connected(G):
        G = add_random_edge(G)
        
    # Expose total iterations
    return G.number_of_edges()

if __name__ == "__main__":
    n = 100
    print("Beginning the simulation... (this may take a split second).")
    
    edges_required = add_edges_till_connect(n)
    
    print(f"For an unlinked network of {n} nodes, it strictly required "
          f"{edges_required} randomly injected edges to trigger full lock connectedness.")
    
    # Theoretical comparative projection: (n * math.log(n)) / 2 
    import math
    theoretical = (n * math.log(n)) / 2
    print(f"Mathematical projection threshold (n log n)/2 predicted approximately: {theoretical:.2f}")
