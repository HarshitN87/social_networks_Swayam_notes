"""
Community Detection: Dividing into two communities using Brute Force Evaluation

WARNING: Brute force operations map to an O(2^n) time complexity. 
This script inherently will only complete evaluations safely on drastically small graphs.
Do not test with node capacities surpassing ~20.
"""

import networkx as nx
import itertools

def communities_brute(G):
    # Extract distinct graph definitions
    nodes = list(G.nodes())
    n = G.number_of_nodes()
    
    # Validation
    if n == 0 or G.number_of_edges() == 0:
        return None, None
    
    # 1. Synthesize Combinations
    # Accumulate all possible combinations (from 1 to Half of n) for evaluation mapping
    first_community_groups = []
    # Note: Corrected iteration loop uppercase `I` typos.
    for i in range(1, (n // 2) + 1):
        # Generate combination tuples and project into physical nested lists
        comb = [list(x) for x in itertools.combinations(nodes, i)]
        first_community_groups.extend(comb)
        
    # 2. Extract Remainder Components
    second_community_groups = []
    for i in range(len(first_community_groups)):
        # Mathematically subtract group set blocks from absolute base root
        l = list(set(nodes) - set(first_community_groups[i]))
        second_community_groups.append(l)
        
    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []
    ratio = []
    
    e = G.number_of_edges()
    
    # 3. Assess the Intra/Inter Connection Weights
    for i in range(len(first_community_groups)):
        
        # Calculate isolated sub-graph capacities internally
        edges1 = G.subgraph(first_community_groups[i]).number_of_edges()
        num_intra_edges1.append(edges1)
        
        edges2 = G.subgraph(second_community_groups[i]).number_of_edges()
        num_intra_edges2.append(edges2)
        
        # Establish bridge/inter edges
        inter_edges = e - edges1 - edges2
        num_inter_edges.append(inter_edges)
        
        # Guard against zero-division for naturally disconnected graph states
        if inter_edges == 0:
            ratio.append(float('inf'))
        else:
            # Objective: Maximize combined internal connectivity / inter-bridge gaps
            ratio.append((edges1 + edges2) / inter_edges)
            
    # Locate optimized maximum target
    max_value = max(ratio)
    max_index = ratio.index(max_value)
    
    # Result retrieval
    optimized_split_first = first_community_groups[max_index]
    optimized_split_second = second_community_groups[max_index]
    
    print("\n--- Successful Bruteforce Optimization Output ---")
    print(f"Sub-Community Vector A: {optimized_split_first}")
    print(f"Sub-Community Vector B: {optimized_split_second}")
    
    return optimized_split_first, optimized_split_second

if __name__ == "__main__":
    # Generating mock configuration for testing (2 groups of 4 linked via 1 bridge)
    G = nx.Graph()
    nx.add_cycle(G, [1, 2, 3, 4])  # Community 1
    nx.add_cycle(G, [5, 6, 7, 8])  # Community 2
    G.add_edge(4, 5)  # Single vulnerable weak-tie acting as an inter-bridge
    
    communities_brute(G)
