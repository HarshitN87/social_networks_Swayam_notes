import networkx as nx
import random
import itertools
import matplotlib.pyplot as plt

def display_graph(G, title="Network"):
    pos = nx.circular_layout(G)
    edge_colors = []
    
    for u, v in G.edges():
        if G[u][v]['sign'] == '+':
            edge_colors.append('green')
        else:
            edge_colors.append('red')
            
    plt.figure(figsize=(6,6))
    nx.draw(G, pos, node_color='lightblue', with_labels=True, 
            edge_color=edge_colors, width=2)
    plt.title(title)
    plt.show()

def get_triangles_and_unstable_count(G):
    # 4.1 Get a list of all the triangles in the network.
    nodes = list(G.nodes())
    triangles = list(itertools.combinations(nodes, 3))
    
    unstable_triangles = []
    
    # 4.2 Store the sign details of all the triangles.
    for tri in triangles:
        u, v, w = tri
        
        # Get edges of the triangle
        edges = [(u, v), (v, w), (w, u)]
        
        pos_count = 0
        neg_count = 0
        
        for edge in edges:
            if G[edge[0]][edge[1]]['sign'] == '+':
                pos_count += 1
            else:
                neg_count += 1
                
        # Determine stability
        # Stable: 3 positives (+++) or 1 positive/2 negatives (+--)
        # Unstable: 2 positives (++-) or 0 positives (---)
        if pos_count == 2 or pos_count == 0:
            unstable_triangles.append(tri)

    # 4.3 Count the number of unstable triangles in the network.
    return triangles, unstable_triangles

def stabilize_triangle(G, tri):
    u, v, w = tri
    edges = [(u, v), (v, w), (w, u)]
    
    signs = [G[e[0]][e[1]]['sign'] for e in edges]
    pos_count = signs.count('+')
    
    # 5.2 Make that triangle stable.
    # As per Case Study 3 rules:
    if pos_count == 0:
        # Zero positive edges: randomly convert one negative to positive.
        edge_to_change = random.choice(edges)
        G[edge_to_change[0]][edge_to_change[1]]['sign'] = '+'
    elif pos_count == 2:
        # Two positive edges: one edge is randomly selected and inverted.
        edge_to_change = random.choice(edges)
        current_sign = G[edge_to_change[0]][edge_to_change[1]]['sign']
        G[edge_to_change[0]][edge_to_change[1]]['sign'] = '+' if current_sign == '-' else '-'

def main():
    # 1. Create a graph with 'n' nodes, where the nodes are the countries.
    n = 10
    G = nx.Graph()
    G.add_nodes_from(range(n))

    # 2. Make it a complete graph by adding all possible edges. Also, assign (sign/random weight)
    for u, v in itertools.combinations(range(n), 2):
        sign = random.choice(['+', '-'])
        G.add_edge(u, v, sign=sign)

    # 3. Display the network.
    # display_graph(G, "Initial Random Complete Signed Network")
    
    _, unstable_triangles = get_triangles_and_unstable_count(G)
    print(f"Initial Unstable Triangles: {len(unstable_triangles)}")

    # 5. While the number of unstable triangles is not zero, do the following:
    iterations = 0
    while len(unstable_triangles) > 0:
        # 5.1 Choose a triangle in the graph that is unstable.
        target_tri = random.choice(unstable_triangles)
        
        # 5.2 Make that triangle stable.
        stabilize_triangle(G, target_tri)
        
        # 5.3 Count the number of unstable triangles
        _, unstable_triangles = get_triangles_and_unstable_count(G)
        iterations += 1
        
        # Safety break for massive graphs
        if iterations > 5000:
            print("Reached iteration limit.")
            break

    print(f"Graph dynamically stabilized after {iterations} iterations.")
    # display_graph(G, "Final Stable Network")

    # 6. Now that there is no unstable triangle in the network, it can be divided:
    # 6.1 Choose a random node. Add it to the first coalition.
    coalition_1 = set()
    coalition_2 = set()
    
    start_node = random.choice(list(G.nodes()))
    coalition_1.add(start_node)
    
    # 6.2 Also put all the 'friends' of this node in the first coalition.
    # 6.3 Put all the 'enemies' of this node in the second coalition.
    for neighbor in G.neighbors(start_node):
        if G[start_node][neighbor]['sign'] == '+':
            coalition_1.add(neighbor)
        else:
            coalition_2.add(neighbor)
            
    print(f"\nExtraction Results based on Node {start_node}:")
    print(f"Coalition 1 (Size: {len(coalition_1)}): {coalition_1}")
    print(f"Coalition 2 (Size: {len(coalition_2)}): {coalition_2}")

if __name__ == "__main__":
    main()
