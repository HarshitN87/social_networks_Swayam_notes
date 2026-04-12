"""
Power Law, Preferential Attachment & Network Resilience
=======================================================
Implements:
  1. Barabási–Albert (BA) preferential attachment model
  2. Erdős–Rényi G(n,p) random graph model
  3. Degree distribution analysis with log-log plots
  4. Network resilience: random failure vs targeted attack

Usage:
  python 10_power_law_ba_model.py

Requires: networkx, matplotlib, numpy
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from collections import Counter

# ──────────────────────────────────────────────────────────
# 1. BARABÁSI–ALBERT PREFERENTIAL ATTACHMENT MODEL
# ──────────────────────────────────────────────────────────


def build_ba_model(n, m0, m):
    """
    Build a Barabási–Albert preferential attachment network from scratch.

    Parameters
    ----------
    n  : int — total number of nodes in the final network
    m0 : int — number of initial fully-connected nodes
    m  : int — number of edges each new node adds (m <= m0)

    Returns
    -------
    G : nx.Graph — the resulting scale-free network

    How it works:
    1. Start with m0 fully connected nodes (complete graph).
    2. For each new node, pick m existing nodes to connect to.
       The probability of picking node i is proportional to its current degree:
         P(i) = degree(i) / sum_of_all_degrees
    3. Repeat until we have n total nodes.
    """
    assert m <= m0, "m must be <= m0 (can't add more edges than initial nodes)"

    # Step 1: Start with a complete graph of m0 nodes
    G = nx.complete_graph(m0)

    # We maintain a list where each node appears once per edge it has.
    # This makes sampling proportional to degree very efficient.
    # For a complete graph of m0 nodes, each node has degree (m0-1).
    degree_list = []
    for node in G.nodes():
        degree_list.extend([node] * G.degree(node))

    # Step 2: Add new nodes one at a time
    for new_node in range(m0, n):
        # Select m unique targets, weighted by degree
        targets = set()
        while len(targets) < m:
            # Random pick from degree_list = preferential attachment
            candidate = random.choice(degree_list)
            if candidate != new_node:
                targets.add(candidate)

        # Add the new node and its edges
        G.add_node(new_node)
        for target in targets:
            G.add_edge(new_node, target)
            # Update the degree list: both endpoints gain one edge
            degree_list.append(new_node)
            degree_list.append(target)

    return G


def build_ba_using_networkx(n, m):
    """
    Build a BA model using NetworkX's built-in function.
    This is faster and cleaner than our manual implementation.

    Parameters
    ----------
    n : int — total number of nodes
    m : int — number of edges each new node adds
    """
    return nx.barabasi_albert_graph(n, m)


# ──────────────────────────────────────────────────────────
# 2. ERDŐS–RÉNYI RANDOM GRAPH MODEL — G(n, p)
# ──────────────────────────────────────────────────────────


def build_erdos_renyi(n, p):
    """
    Build an Erdős–Rényi random graph from scratch.

    Parameters
    ----------
    n : int — number of nodes
    p : float — probability of each edge existing (0 to 1)

    Returns
    -------
    G : nx.Graph — the resulting random graph

    How it works:
    For every possible pair (i, j), flip a biased coin with probability p.
    If heads, add the edge. If tails, skip it.
    Each edge decision is completely independent of all others.
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                G.add_edge(i, j)

    return G


def build_erdos_renyi_using_networkx(n, p):
    """Use NetworkX's built-in function (much faster for large n)."""
    return nx.erdos_renyi_graph(n, p)


# ──────────────────────────────────────────────────────────
# 3. DEGREE DISTRIBUTION ANALYSIS
# ──────────────────────────────────────────────────────────


def get_degree_distribution(G):
    """
    Compute the degree distribution of a graph.

    Returns
    -------
    degrees : list of int — sorted unique degree values
    frequencies : list of float — fraction of nodes with each degree
    """
    degree_sequence = [d for _, d in G.degree()]
    count = Counter(degree_sequence)
    total_nodes = G.number_of_nodes()

    degrees = sorted(count.keys())
    frequencies = [count[k] / total_nodes for k in degrees]

    return degrees, frequencies


def plot_degree_distributions(G_ba, G_er, title="Degree Distribution Comparison"):
    """
    Plot degree distributions for a BA (scale-free) and ER (random) graph
    on both linear and log-log scales.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # --- Linear scale ---
    deg_ba, freq_ba = get_degree_distribution(G_ba)
    deg_er, freq_er = get_degree_distribution(G_er)

    axes[0].bar(deg_er, freq_er, alpha=0.6, color='#6366f1', label='Erdős–Rényi (Bell Curve)')
    axes[0].bar(deg_ba, freq_ba, alpha=0.6, color='#f97316', label='Barabási–Albert (Power Law)')
    axes[0].set_xlabel('Degree (k)')
    axes[0].set_ylabel('Fraction of Nodes P(k)')
    axes[0].set_title('Linear Scale')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # --- Log-log scale ---
    # Filter out zeros for log plot
    deg_ba_pos = [d for d, f in zip(deg_ba, freq_ba) if f > 0 and d > 0]
    freq_ba_pos = [f for f in freq_ba if f > 0]
    deg_er_pos = [d for d, f in zip(deg_er, freq_er) if f > 0 and d > 0]
    freq_er_pos = [f for f in freq_er if f > 0]

    axes[1].scatter(deg_er_pos, freq_er_pos, alpha=0.6, color='#6366f1',
                    label='Erdős–Rényi', s=20)
    axes[1].scatter(deg_ba_pos, freq_ba_pos, alpha=0.6, color='#f97316',
                    label='Barabási–Albert', s=20)
    axes[1].set_xscale('log')
    axes[1].set_yscale('log')
    axes[1].set_xlabel('log(Degree)')
    axes[1].set_ylabel('log(P(k))')
    axes[1].set_title('Log-Log Scale (straight line = power law)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.suptitle(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('degree_distributions.png', dpi=150, bbox_inches='tight')
    plt.show()


# ──────────────────────────────────────────────────────────
# 4. NETWORK RESILIENCE: RANDOM FAILURE vs TARGETED ATTACK
# ──────────────────────────────────────────────────────────


def largest_connected_component_size(G):
    """Return the number of nodes in the largest connected component."""
    if G.number_of_nodes() == 0:
        return 0
    return len(max(nx.connected_components(G), key=len))


def simulate_random_failure(G, steps=None):
    """
    Simulate random node removal (like random server crashes).

    At each step, remove a RANDOM node and measure the
    largest connected component size.

    Returns
    -------
    fractions_removed : list of float — fraction of nodes removed at each step
    lcc_sizes : list of float — fraction of nodes in largest component at each step
    """
    G_copy = G.copy()
    n = G_copy.number_of_nodes()
    if steps is None:
        steps = int(n * 0.9)  # Remove up to 90% of nodes

    nodes = list(G_copy.nodes())
    random.shuffle(nodes)  # Random order for removal

    fractions_removed = [0.0]
    lcc_sizes = [largest_connected_component_size(G_copy) / n]

    for i in range(min(steps, len(nodes))):
        G_copy.remove_node(nodes[i])
        fraction = (i + 1) / n
        lcc = largest_connected_component_size(G_copy) / n
        fractions_removed.append(fraction)
        lcc_sizes.append(lcc)

    return fractions_removed, lcc_sizes


def simulate_targeted_attack(G, steps=None):
    """
    Simulate targeted attack: remove nodes in order of HIGHEST DEGREE first.

    This represents an attacker who knows the network structure and
    deliberately disables the most important hubs.

    Returns
    -------
    fractions_removed : list of float — fraction of nodes removed at each step
    lcc_sizes : list of float — fraction of nodes in largest component at each step
    """
    G_copy = G.copy()
    n = G_copy.number_of_nodes()
    if steps is None:
        steps = int(n * 0.9)

    fractions_removed = [0.0]
    lcc_sizes = [largest_connected_component_size(G_copy) / n]

    for i in range(steps):
        if G_copy.number_of_nodes() == 0:
            break
        # Find the node with the highest degree (the biggest hub)
        node_to_remove = max(G_copy.nodes(), key=lambda x: G_copy.degree(x))
        G_copy.remove_node(node_to_remove)

        fraction = (i + 1) / n
        lcc = largest_connected_component_size(G_copy) / n
        fractions_removed.append(fraction)
        lcc_sizes.append(lcc)

    return fractions_removed, lcc_sizes


def plot_resilience(G_ba, G_er):
    """
    Compare resilience of BA (scale-free) vs ER (random) networks
    under both random failure and targeted attack.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Scale-Free (BA)
    fr_rand_ba, lcc_rand_ba = simulate_random_failure(G_ba)
    fr_targ_ba, lcc_targ_ba = simulate_targeted_attack(G_ba)

    axes[0].plot(fr_rand_ba, lcc_rand_ba, color='#34d399', linewidth=2,
                 label='Random Failure (robust!)')
    axes[0].plot(fr_targ_ba, lcc_targ_ba, color='#f87171', linewidth=2,
                 label='Targeted Attack (fragile!)')
    axes[0].set_xlabel('Fraction of Nodes Removed')
    axes[0].set_ylabel('Largest Component (fraction)')
    axes[0].set_title('Scale-Free (BA) Network')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlim(0, 0.5)

    # Random (ER)
    fr_rand_er, lcc_rand_er = simulate_random_failure(G_er)
    fr_targ_er, lcc_targ_er = simulate_targeted_attack(G_er)

    axes[1].plot(fr_rand_er, lcc_rand_er, color='#34d399', linewidth=2,
                 label='Random Failure')
    axes[1].plot(fr_targ_er, lcc_targ_er, color='#f87171', linewidth=2,
                 label='Targeted Attack')
    axes[1].set_xlabel('Fraction of Nodes Removed')
    axes[1].set_ylabel('Largest Component (fraction)')
    axes[1].set_title('Random (ER) Network')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xlim(0, 0.5)

    plt.suptitle('Network Resilience Comparison', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('network_resilience.png', dpi=150, bbox_inches='tight')
    plt.show()


# ──────────────────────────────────────────────────────────
# 5. PREFERENTIAL ATTACHMENT PROBABILITY CALCULATOR
# ──────────────────────────────────────────────────────────


def calculate_attachment_probability(degrees, target_node_index):
    """
    Calculate the probability that a new node connects to the target node
    under the preferential attachment rule.

    Parameters
    ----------
    degrees : dict or list — degrees of all existing nodes
              e.g., {'A': 4, 'B': 3, 'C': 5, 'D': 3, 'E': 3, 'F': 4, 'G': 3, 'H': 3}
    target_node_index : str or int — the node we want the probability for

    Returns
    -------
    probability : float

    Formula: P(attach to i) = k_i / Σk_j
    """
    if isinstance(degrees, dict):
        total = sum(degrees.values())
        k_i = degrees[target_node_index]
    else:
        total = sum(degrees)
        k_i = degrees[target_node_index]

    probability = k_i / total
    return probability


# ──────────────────────────────────────────────────────────
# 6. BA MODEL EDGE COUNT CALCULATOR
# ──────────────────────────────────────────────────────────


def count_ba_edges(m0, m, new_nodes, initial_graph='complete'):
    """
    Calculate the total number of edges in a BA model.

    Parameters
    ----------
    m0 : int — number of initial nodes
    m  : int — edges per new node
    new_nodes : int — number of nodes added after initial setup
    initial_graph : str — 'complete' for fully connected, 'linear' for chain

    Returns
    -------
    total_edges : int

    Formula:
    - Complete initial graph: m0*(m0-1)/2 + new_nodes * m
    - Linear initial graph:   (m0-1) + new_nodes * m
    """
    if initial_graph == 'complete':
        initial_edges = m0 * (m0 - 1) // 2
    elif initial_graph == 'linear':
        initial_edges = m0 - 1
    else:
        raise ValueError("initial_graph must be 'complete' or 'linear'")

    new_edges = new_nodes * m
    total_edges = initial_edges + new_edges

    print(f"Initial graph ({initial_graph}) with {m0} nodes: {initial_edges} edges")
    print(f"New nodes added: {new_nodes}, each adding {m} edges: {new_edges} edges")
    print(f"Total edges: {initial_edges} + {new_edges} = {total_edges}")

    return total_edges


# ──────────────────────────────────────────────────────────
# MAIN: Run all demonstrations
# ──────────────────────────────────────────────────────────


if __name__ == "__main__":
    random.seed(42)
    np.random.seed(42)

    print("=" * 60)
    print("POWER LAW & PREFERENTIAL ATTACHMENT DEMONSTRATIONS")
    print("=" * 60)

    # ── Demo 1: Build and compare networks ──
    print("\n📊 Demo 1: Building Networks")
    print("-" * 40)

    N = 1000  # Total nodes
    M = 3     # Edges per new node (BA) / target average degree (ER)

    # BA model
    G_ba = build_ba_using_networkx(N, M)
    print(f"BA Network: {G_ba.number_of_nodes()} nodes, {G_ba.number_of_edges()} edges")
    print(f"  Max degree: {max(dict(G_ba.degree()).values())}")
    print(f"  Avg degree: {sum(dict(G_ba.degree()).values()) / N:.1f}")

    # ER model (calibrate p so average degree ≈ 2*M)
    p = 2 * M / N  # Average degree ≈ 2*M
    G_er = build_erdos_renyi_using_networkx(N, p)
    print(f"ER Network: {G_er.number_of_nodes()} nodes, {G_er.number_of_edges()} edges")
    print(f"  Max degree: {max(dict(G_er.degree()).values())}")
    print(f"  Avg degree: {sum(dict(G_er.degree()).values()) / N:.1f}")

    # ── Demo 2: Degree distributions ──
    print("\n📊 Demo 2: Plotting Degree Distributions")
    print("-" * 40)
    plot_degree_distributions(G_ba, G_er)

    # ── Demo 3: Preferential attachment probability ──
    print("\n📊 Demo 3: Preferential Attachment Probability")
    print("-" * 40)
    # Assignment example: 8 users, degrees A=4, B=3, C=5, D=3, E=3, F=4, G=3, H=3
    degrees = {'A': 4, 'B': 3, 'C': 5, 'D': 3, 'E': 3, 'F': 4, 'G': 3, 'H': 3}
    total_deg = sum(degrees.values())
    print(f"Node degrees: {degrees}")
    print(f"Total degree sum: {total_deg}")
    for node in sorted(degrees.keys()):
        prob = calculate_attachment_probability(degrees, node)
        print(f"  P(new node → {node}) = {degrees[node]}/{total_deg} = {prob:.4f}")

    # ── Demo 4: Edge counting ──
    print("\n📊 Demo 4: BA Model Edge Counting")
    print("-" * 40)
    print("Case 1: m0=5 fully connected, m=3, 15 new nodes:")
    count_ba_edges(m0=5, m=3, new_nodes=15, initial_graph='complete')

    print("\nCase 2: 4 linear airports, m=3, 8 new airports:")
    count_ba_edges(m0=4, m=3, new_nodes=8, initial_graph='linear')

    # ── Demo 5: Network resilience ──
    print("\n📊 Demo 5: Network Resilience Simulation")
    print("-" * 40)
    print("Building larger networks for resilience test (n=500)...")
    G_ba_500 = build_ba_using_networkx(500, 3)
    G_er_500 = build_erdos_renyi_using_networkx(500, 6 / 500)
    plot_resilience(G_ba_500, G_er_500)

    print("\n✅ All demonstrations complete!")
    print("Generated plots: degree_distributions.png, network_resilience.png")
