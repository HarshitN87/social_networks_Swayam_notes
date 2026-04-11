"""
Community Detection: Girvan-Newman Algorithm

Operation: Dynamically calculates Edge Betweenness Centrality limits
and persistently breaks edges reporting the highest values to disconnect networks.
"""

import networkx as nx

def determine_highest_betweenness(G):
    """Scans all established edges and reveals the centralized bottleneck."""
    # Method returns a localized dictionary mapping edge tuples to weight values.
    edge_centralities = nx.edge_betweenness_centrality(G)
    
    # Utilizing native dict maximum retrieval based on values
    return max(edge_centralities, key=edge_centralities.get)

def girvan_newman(G, requested_communities=2):
    """Mutates network graph intentionally until communities segregate."""
    if G.number_of_nodes() == 0:
        return []
        
    # Extract isolated subgraph component volume initially
    components = list(nx.connected_components(G))
    
    # Keep stripping critical edges iteratively until separation demands are reached
    while len(components) < requested_communities:
        if G.number_of_edges() == 0:
            break
            
        edge_to_eliminate = determine_highest_betweenness(G)
        print(f"Fracturing weakest bridge / target identified: {edge_to_eliminate}")
        
        # Destruct edge
        G.remove_edge(*edge_to_eliminate)
        
        # Re-evaluate network topologies
        components = list(nx.connected_components(G))
        
    return components

if __name__ == "__main__":
    print("Initiating test graph constraints...")
    
    G = nx.Graph()
    # Identical Mock: Two robust communities bridged
    nx.add_cycle(G, [1, 2, 3, 4, 5])
    nx.add_cycle(G, [6, 7, 8, 9, 10])
    G.add_edge(4, 7) # Expected target bridge
    
    # Copy graph map to prevent mutating globally unless required
    analyzed_communities = girvan_newman(G.copy(), requested_communities=2)
    
    print("\n--- Final Discovered Isolated Communities ---")
    for i, comm in enumerate(analyzed_communities):
        print(f"Set Community [{i+1}]: {comm}")
