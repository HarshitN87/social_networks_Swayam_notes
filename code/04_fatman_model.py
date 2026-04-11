import networkx as nx
import random
import matplotlib.pyplot as plt

def get_colors(G):
    """
    Assign colors based on the BMI value of the node.
    Thin/Low BMI = Blue, Average = Green, High BMI ('Fat') = Red
    """
    colors = []
    for node in G.nodes():
        bmi = G.nodes[node]['bmi']
        if bmi < 20:
            colors.append('blue')
        elif bmi < 25:
            colors.append('green')
        else:
            colors.append('red')
    return colors

def add_selection(G):
    """
    Selection: People tend to become friends with others who have a similar BMI.
    We iterate over all pairs of non-connected nodes and connect them with a probability
    inversely proportional to their difference in BMI.
    """
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            if not G.has_edge(u, v):
                diff = abs(G.nodes[u]['bmi'] - G.nodes[v]['bmi'])
                # Probability of linking decreases as BMI difference increases
                prob = 1 / (1 + diff) 
                
                # Introduce a threshold or randomness to form selection tie
                if random.random() < 0.2 * prob:
                    G.add_edge(u, v)
    return G

def add_closure(G):
    """
    Triadic Closure: If two nodes share a common friend, they have a higher probability 
    of becoming friends themselves.
    """
    # Create a list of new edges to add, to avoid modifying graph during iteration
    new_edges = []
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            if not G.has_edge(u, v):
                # Count common friends
                common_friends = list(nx.common_neighbors(G, u, v))
                k = len(common_friends)
                
                if k > 0:
                    # Probability of them becoming friends increases with k
                    # For example: p = 1 - (1 - base_p)^k
                    base_p = 0.1
                    prob = 1 - (1 - base_p)**k
                    if random.random() < prob:
                        new_edges.append((u, v))
                        
    for u, v in new_edges:
        G.add_edge(u, v)
    return G

def apply_social_influence(G):
    """
    Social Influence: Over time, people are influenced by their friends.
    We adjust the BMI of each node towards the average BMI of its neighbors.
    """# Wait, wait, actually updating the BMI based on social influence.
    # We must calculate new bmi values first before assigning them so updates happen simultaneously step-by-step
    new_bmi = {}
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        if len(neighbors) > 0:
            neighbor_bmis = [G.nodes[n]['bmi'] for n in neighbors]
            avg_neighbor_bmi = sum(neighbor_bmis) / len(neighbor_bmis)
            
            # Move the node's BMI slightly towards the neighbors' average BMI (Influence rate of 10%)
            current_bmi = G.nodes[node]['bmi']
            new_bmi[node] = current_bmi + 0.1 * (avg_neighbor_bmi - current_bmi)
        else:
            new_bmi[node] = G.nodes[node]['bmi']
            
    # Apply the new bmis
    nx.set_node_attributes(G, new_bmi, 'bmi')
    return G

def simulate_fatman_model(num_nodes=50, iterations=5):
    """
    Simulates the Evolutionary Model incorporating:
    1. Selection (Homophily)
    2. Closure (Triadic)
    3. Social Influence
    """
    print("Initializing the Network...")
    G = nx.Graph()
    
    # 1. Add nodes with random initial BMIs ranging from 15 to 40
    for i in range(num_nodes):
        G.add_node(i, bmi=random.uniform(15, 40))
        
    for step in range(iterations):
        print(f"--- Iteration {step + 1} ---")
        
        # Apply mechanisms
        G = add_selection(G)
        G = add_closure(G)
        G = apply_social_influence(G)
        
        # Optional: visualizing statistics
        avg_deg = sum(dict(G.degree()).values()) / num_nodes
        print(f"Number of Edges: {G.number_of_edges()}, Average Degree: {avg_deg:.2f}")
        
    print("Simulation Complete.")
    return G

if __name__ == "__main__":
    G = simulate_fatman_model(num_nodes=50, iterations=5)
