# Introduction to NetworkX

`NetworkX` is a powerful, production-grade Python library designed exclusively for the creation, rigorous manipulation, and mathematical study of the structure and dynamics regarding complex networks.

## Installing Essential Packages

You will need `networkx` to compute data, and `matplotlib` to render its visualizations.

```bash
pip install networkx matplotlib
```

## Core Fundamentals & Functions

### 1. Generating & Modifying Structures
```python
import networkx as nx

# Initialize an empty, undirected graph map
G = nx.Graph()

# Appending a solitary single node recursively
G.add_node(1)

# Appending batch nodes using iterables
G.add_nodes_from([2, 3, 4, 5])

# Appending a single connection logic (Nodes will be forced into existence automatically)
G.add_edge(1, 2)

# Appending connections recursively
G.add_edges_from([(2, 3), (3, 4), (4, 1)])
```

### 2. Exploring Graph Metadata and Mathematics
```python
# Returns purely integer volume
print(G.number_of_nodes())  

# Returns strictly established edge volume
print(G.number_of_edges())  

# Extracts raw mapping references
print(list(G.nodes()))      

# Graph Boolean condition (Requires fully interlocked systems)
print("Is it entirely connected?: ", nx.is_connected(G))   
```

### 3. Plotting & Rendering (Visualizing)
Integrating NetworkX data pipelines into standard plot grids provides an immediate aesthetic visualization. You can export these to UI directly.

```python
import matplotlib.pyplot as plt

# Primary command invoking the render.
# Configure weights, labels, and color hexes internally here.
nx.draw(G, with_labels=True, node_color='#add8e6', font_weight='bold')

# Trigger display sequence directly to UI
plt.show()

# Flush sequence to hard disk output
plt.savefig("visualized_graph.png")
```

### 4. Reading Data Extraneously from Formats
NetworkX supports vast importing methods depending entirely on how the empirical data was formatted structurally.

```python
# === Approach A: Standard List Map (edges.txt) ===
# Formatted inherently via lines like: '1 2', '2 3'
G1 = nx.read_edgelist("edges.txt", nodetype=int)

# === Approach B: Raw Algorithmic Adjacency Matrix ===
import numpy as np
matrix_ref = np.matrix([
    [0, 1, 0], 
    [1, 0, 1],
    [0, 1, 0]
])
G2 = nx.from_numpy_array(matrix_ref)

# === Approach C: Graph Modelling Language (GML) ===
# Standard standard encoding representation format
# G3 = nx.read_gml("network.gml")
```
