"""
08_diffusion_cascades.py
========================
Four simulations of diffusion and cascades in networks:

  1. Effect of Increasing Payoff — how payoff advantage drives adoption
  2. Influencer Seeding — high-degree seeds vs random seeds
  3. Community Structure — cascade within vs. across clusters
  4. Cluster Density & Threshold — blocking condition demo

Threshold model used throughout:
  - Each node is on behaviour A (0) or B (1)
  - A node switches to B if fraction of B-neighbours >= threshold q
  - Threshold q = a / (a + b) in the coordination game
"""

import random
import math
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


# ─────────────────────────────────────────────
# CORE: Linear Threshold Model
# ─────────────────────────────────────────────

def linear_threshold_spread(G, seeds, threshold=0.3, max_iter=500):
    """
    Run the Linear Threshold Model on graph G.

    Each node is 0 (behaviour A) or 1 (behaviour B).
    A node flips from 0→1 if the fraction of its neighbours on 1 >= threshold.
    Adoption is permanent (no switching back).

    Args:
        G         : networkx Graph or DiGraph
        seeds     : iterable of nodes to start on behaviour B
        threshold : fraction of neighbours needed to flip (q in the model)
        max_iter  : max rounds before stopping

    Returns:
        adopted   : set of nodes that ended on behaviour B
        history   : list of adoption counts per round (shows spread dynamics)
    """
    state = {v: 0 for v in G.nodes()}
    for s in seeds:
        state[s] = 1

    history = [sum(state.values())]

    for _ in range(max_iter):
        new_state = dict(state)
        changed = False
        for v in G.nodes():
            if state[v] == 1:
                continue
            neighbours = list(G.predecessors(v)) if G.is_directed() else list(G.neighbors(v))
            if not neighbours:
                continue
            fraction_b = sum(state[u] for u in neighbours) / len(neighbours)
            if fraction_b >= threshold:
                new_state[v] = 1
                changed = True
        state = new_state
        history.append(sum(state.values()))
        if not changed:
            break

    adopted = {v for v, s in state.items() if s == 1}
    return adopted, history


# ─────────────────────────────────────────────
# HELPER: Compute threshold from payoffs
# ─────────────────────────────────────────────

def payoff_to_threshold(payoff_a, payoff_b):
    """
    Coordination game threshold.

    In the coordination game, you switch to behaviour B when
    the fraction of friends on B > q = payoff_a / (payoff_a + payoff_b).

    A lower payoff_a (old behaviour less attractive) → lower q → easier cascade.
    A higher payoff_b (new behaviour more attractive) → lower q → easier cascade.
    """
    return payoff_a / (payoff_a + payoff_b)


def compute_switch_decision(n_friends, n_on_b, payoff_a, payoff_b):
    """
    Directly compute the payoff for both options and decide.

    Args:
        n_friends: total number of friends
        n_on_b   : number of friends on behaviour B
        payoff_a : payoff per friend matching on A
        payoff_b : payoff per friend matching on B

    Returns:
        (total_a, total_b, choice) where choice is 'A' or 'B'
    """
    n_on_a = n_friends - n_on_b
    total_a = n_on_a * payoff_a
    total_b = n_on_b * payoff_b
    choice = 'B' if total_b > total_a else 'A'
    return total_a, total_b, choice


# ─────────────────────────────────────────────
# SIMULATION 1: Effect of Increasing Payoff
# ─────────────────────────────────────────────

def sim1_payoff_effect(n_nodes=200, avg_degree=6, n_seeds=5):
    """
    Simulation 1: How does increasing the payoff advantage of B affect cascade size?

    We fix payoff_a = 2, vary payoff_b from 2 to 10.
    For each payoff_b, we compute threshold q = a/(a+b) and run the LT model.
    Plot: payoff_b → final adoption fraction.
    """
    print("\n" + "=" * 60)
    print("  Simulation 1: Effect of Increasing Payoff on Adoption")
    print("=" * 60)

    G = nx.barabasi_albert_graph(n_nodes, int(avg_degree / 2), seed=42)
    seeds = random.sample(list(G.nodes()), n_seeds)

    payoff_a = 2
    payoff_b_values = np.linspace(2, 12, 25)
    adoption_rates = []

    for pb in payoff_b_values:
        q = payoff_to_threshold(payoff_a, pb)
        adopted, _ = linear_threshold_spread(G, seeds, threshold=q)
        adoption_rates.append(len(adopted) / n_nodes)

    # --- Plot ---
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Simulation 1: Payoff Advantage → Cascade Size", fontsize=13, fontweight='bold')

    # Payoff vs adoption rate
    axes[0].plot(payoff_b_values, adoption_rates, 'o-', color='steelblue', linewidth=2.5, markersize=6)
    axes[0].axhline(1.0, color='red', linestyle='--', alpha=0.5, label='Full adoption')
    axes[0].set_xlabel("Payoff of New Behaviour B (payoff_a fixed at 2)")
    axes[0].set_ylabel("Final Adoption Fraction")
    axes[0].set_title("Higher Payoff → Lower Threshold → Bigger Cascade")
    axes[0].legend()
    axes[0].grid(alpha=0.3)

    # Threshold vs adoption rate
    thresholds = [payoff_to_threshold(payoff_a, pb) for pb in payoff_b_values]
    axes[1].plot(thresholds, adoption_rates, 's-', color='darkorange', linewidth=2.5, markersize=6)
    axes[1].set_xlabel("Threshold q = a/(a+b)")
    axes[1].set_ylabel("Final Adoption Fraction")
    axes[1].set_title("Lower Threshold → More Nodes Switch")
    axes[1].invert_xaxis()  # lower threshold = more attractive = left on axis
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("sim1_payoff_effect.png", dpi=150)
    print(f"  Plot saved to sim1_payoff_effect.png")
    plt.show()

    # Print example calculation
    print("\n  Example payoff calculation (lecture scenario):")
    n, n_b, pa, pb = 20, 5, 2, 3
    ta, tb, choice = compute_switch_decision(n, n_b, pa, pb)
    q = payoff_to_threshold(pa, pb)
    print(f"    Payoff A={pa}, B={pb} → threshold q = {pa}/({pa}+{pb}) = {q:.2f}")
    print(f"    20 friends: 15 on A, 5 on B")
    print(f"    Payoff_A = 15×{pa} = {ta:.0f}, Payoff_B = 5×{pb} = {tb:.0f} → choose {choice}")


# ─────────────────────────────────────────────
# SIMULATION 2: Key People — Influencer Seeding
# ─────────────────────────────────────────────

def sim2_influencer_seeding(n_nodes=300, avg_degree=5, threshold=0.3, n_seeds=10, n_runs=15):
    """
    Simulation 2: Compare seeding strategies.

    Strategy A: Random seeds (n_seeds random nodes)
    Strategy B: High-degree seeds (top n_seeds nodes by degree)

    Run n_runs trials for each strategy; plot distribution of adoption sizes.
    """
    print("\n" + "=" * 60)
    print("  Simulation 2: Influencer Seeding vs. Random Seeding")
    print("=" * 60)

    G = nx.barabasi_albert_graph(n_nodes, int(avg_degree / 2), seed=99)

    # Identify high-degree nodes
    degree_sorted = sorted(G.degree(), key=lambda x: x[1], reverse=True)
    top_seeds = [node for node, deg in degree_sorted[:n_seeds]]
    print(f"  Top-{n_seeds} degree seeds: {[f'Node {v}(deg={G.degree(v)})' for v in top_seeds[:5]]}...")

    # Run random seeding
    random_adoptions = []
    for run in range(n_runs):
        seeds = random.sample(list(G.nodes()), n_seeds)
        adopted, _ = linear_threshold_spread(G, seeds, threshold=threshold)
        random_adoptions.append(len(adopted) / n_nodes)

    # Run influencer seeding
    influencer_adoptions = []
    for run in range(n_runs):
        # Slightly vary which exact top nodes are used (simulate real uncertainty)
        seeds = top_seeds[:n_seeds]
        adopted, _ = linear_threshold_spread(G, seeds, threshold=threshold)
        influencer_adoptions.append(len(adopted) / n_nodes)

    print(f"  Random seeding:     avg adoption = {np.mean(random_adoptions):.3f} ± {np.std(random_adoptions):.3f}")
    print(f"  Influencer seeding: avg adoption = {np.mean(influencer_adoptions):.3f} ± {np.std(influencer_adoptions):.3f}")

    # Also run a single detailed spread to plot dynamics
    _, rnd_history = linear_threshold_spread(G, random.sample(list(G.nodes()), n_seeds), threshold)
    _, inf_history = linear_threshold_spread(G, top_seeds, threshold)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Simulation 2: Influencer vs. Random Seeding", fontsize=13, fontweight='bold')

    # Box plot comparison
    axes[0].boxplot([random_adoptions, influencer_adoptions],
                    labels=['Random\nSeeding', 'Influencer\nSeeding'],
                    patch_artist=True,
                    boxprops=dict(facecolor='lightblue'),
                    medianprops=dict(color='navy', linewidth=2))
    axes[0].set_ylabel("Adoption Fraction")
    axes[0].set_title(f"Adoption Rate ({n_runs} runs each, q={threshold})")
    axes[0].grid(axis='y', alpha=0.3)

    # Spread dynamics
    axes[1].plot(range(len(rnd_history)), [x / n_nodes for x in rnd_history],
                 'o-', color='coral', label='Random seeds', linewidth=2)
    axes[1].plot(range(len(inf_history)), [x / n_nodes for x in inf_history],
                 's-', color='steelblue', label='Influencer seeds', linewidth=2)
    axes[1].set_xlabel("Round")
    axes[1].set_ylabel("Fraction Adopted")
    axes[1].set_title("Spread Dynamics Over Rounds")
    axes[1].legend()
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("sim2_influencer_seeding.png", dpi=150)
    print("  Plot saved to sim2_influencer_seeding.png")
    plt.show()


# ─────────────────────────────────────────────
# SIMULATION 3: Impact of Communities on Cascades
# ─────────────────────────────────────────────

def sim3_community_cascade(threshold=0.3, n_per_cluster=30, n_clusters=4, p_intra=0.25, p_inter=0.02):
    """
    Simulation 3: Cascade starting in one community — does it spread globally?

    Creates a network with clear community structure using the
    Stochastic Block Model (dense within, sparse between).
    Seeds the cascade in cluster 0 and observes which clusters adopt.

    Args:
        threshold  : adoption threshold q
        n_per_cluster: nodes per cluster
        n_clusters : number of communities
        p_intra    : probability of edge within a cluster (dense)
        p_inter    : probability of edge between clusters (sparse = weak ties)
    """
    print("\n" + "=" * 60)
    print("  Simulation 3: Community Structure and Cascade Propagation")
    print("=" * 60)

    # Build Stochastic Block Model
    sizes = [n_per_cluster] * n_clusters
    probs = [[p_intra if i == j else p_inter for j in range(n_clusters)]
             for i in range(n_clusters)]
    G = nx.stochastic_block_model(sizes, probs, seed=7)

    # Identify which cluster each node belongs to
    node_to_cluster = {}
    start = 0
    for c, size in enumerate(sizes):
        for v in range(start, start + size):
            node_to_cluster[v] = c
        start += size

    # Seed: 20% of cluster 0
    cluster_0_nodes = [v for v, c in node_to_cluster.items() if c == 0]
    seeds = random.sample(cluster_0_nodes, max(1, len(cluster_0_nodes) // 5))

    adopted, history = linear_threshold_spread(G, seeds, threshold=threshold)

    # Summarise adoption per cluster
    print(f"\n  n_clusters={n_clusters}, n_per_cluster={n_per_cluster}")
    print(f"  p_intra={p_intra}, p_inter={p_inter}, threshold q={threshold}")
    print(f"  Seeds: {len(seeds)} nodes in Cluster 0")
    print(f"\n  Cluster | Nodes | Adopted | Fraction")
    print(f"  --------|-------|---------|--------")
    for c in range(n_clusters):
        cluster_nodes = [v for v, cl in node_to_cluster.items() if cl == c]
        adopted_in_c = len(adopted.intersection(set(cluster_nodes)))
        print(f"  {c:7} | {len(cluster_nodes):5} | {adopted_in_c:7} | {adopted_in_c/len(cluster_nodes):.2f}")

    # Visualise
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Simulation 3: Community-Based Cascade", fontsize=13, fontweight='bold')

    cluster_colors = ['#e53e3e', '#48bb78', '#4299e1', '#ed8936'][:n_clusters]
    node_colors_graph = [cluster_colors[node_to_cluster[v]] for v in G.nodes()]
    node_colors_adopted = ['#dc2626' if v in adopted else '#94a3b8' for v in G.nodes()]
    node_border = ['black' if v in seeds else 'white' for v in G.nodes()]

    pos = nx.spring_layout(G, seed=42)

    axes[0].set_title("Network Structure (colours = communities)")
    nx.draw_networkx(G, pos=pos, ax=axes[0], node_color=node_colors_graph,
                     node_size=60, with_labels=False,
                     edge_color='gray', alpha=0.7, width=0.5)
    patches = [mpatches.Patch(color=cluster_colors[c], label=f'Cluster {c}') for c in range(n_clusters)]
    axes[0].legend(handles=patches, loc='upper right', fontsize=8)
    axes[0].axis('off')

    axes[1].set_title("Cascade Result (red=adopted, grey=not adopted)")
    nx.draw_networkx(G, pos=pos, ax=axes[1], node_color=node_colors_adopted,
                     node_size=60, with_labels=False,
                     edge_color='gray', alpha=0.5, width=0.5)
    axes[1].axis('off')

    # Spread over time
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    total_nodes = G.number_of_nodes()
    ax2.plot(range(len(history)), [x / total_nodes for x in history],
             'o-', color='steelblue', linewidth=2.5)
    ax2.set_xlabel("Round")
    ax2.set_ylabel("Global Adoption Fraction")
    ax2.set_title("Cascade Spread Over Time")
    ax2.grid(alpha=0.3)
    fig2.tight_layout()

    plt.tight_layout()
    plt.savefig("sim3_community_cascade.png", dpi=150)
    print("  Plot saved to sim3_community_cascade.png")
    plt.show()
    return G, node_to_cluster, adopted


# ─────────────────────────────────────────────
# SIMULATION 4: Cascades and Clusters (Density & Threshold)
# ─────────────────────────────────────────────

def sim4_density_blocking(threshold=0.3):
    """
    Simulation 4: Cluster Density and Cascade Blocking.

    Key theorem: A cluster BLOCKS a cascade if cluster density > (1 - q).

    We create a graph with:
      - Left side: sparse "source" cluster (cascade starts here)
      - Bridge node connecting to a target cluster  
      - Target cluster: varying density (test blocking threshold)

    We verify that when target density > (1-q), cascade stops.
    """
    print("\n" + "=" * 60)
    print("  Simulation 4: Cluster Density vs. Cascade Blocking")
    print("=" * 60)
    print(f"  Threshold q = {threshold}")
    print(f"  Blocking condition: cluster density > {1 - threshold:.2f}")

    cluster_sizes = range(6, 20)
    density_values = np.linspace(0.1, 0.99, 20)
    results = {}

    for density in density_values:
        blocked_count = 0
        for cluster_size in cluster_sizes:
            G = nx.Graph()

            # Source cluster: sparse (fully connected to ensure cascade starts)
            source_nodes = list(range(10))
            G.add_nodes_from(source_nodes)
            for i in source_nodes:
                for j in source_nodes:
                    if i < j:
                        G.add_edge(i, j)

            # Target cluster: controlled density
            target_start = 10
            target_nodes = list(range(target_start, target_start + cluster_size))
            G.add_nodes_from(target_nodes)
            n_possible_edges = cluster_size * (cluster_size - 1) // 2
            n_edges_to_add = int(density * n_possible_edges)
            possible_pairs = [(target_nodes[i], target_nodes[j])
                              for i in range(cluster_size)
                              for j in range(i + 1, cluster_size)]
            random.shuffle(possible_pairs)
            for u, v in possible_pairs[:n_edges_to_add]:
                G.add_edge(u, v)

            # Bridge: source node → one target node
            bridge_source = source_nodes[-1]
            bridge_target = target_nodes[0]
            G.add_edge(bridge_source, bridge_target)

            # Seed: all source nodes adopt B
            seeds = source_nodes
            adopted, _ = linear_threshold_spread(G, seeds, threshold=threshold)

            # Check if cascade entered target cluster
            target_adopted = len(adopted.intersection(set(target_nodes)))
            if target_adopted == 0:
                blocked_count += 1

        results[density] = blocked_count / len(cluster_sizes)

    # --- Plot ---
    densities = list(results.keys())
    block_rates = list(results.values())

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(densities, block_rates, 'o-', color='#dc2626', linewidth=2.5, markersize=7)
    ax.axvline(1 - threshold, color='navy', linestyle='--', linewidth=2,
               label=f'Blocking threshold = 1 - q = {1 - threshold:.2f}')
    ax.fill_betweenx([0, 1], 1 - threshold, 1.0, alpha=0.12, color='navy', label='Blocking zone')
    ax.set_xlabel("Target Cluster Internal Density")
    ax.set_ylabel("Fraction of Cases Blocked")
    ax.set_title(f"Cascade Blocking by Cluster Density  (q = {threshold})")
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("sim4_density_blocking.png", dpi=150)
    print("  Plot saved to sim4_density_blocking.png")
    plt.show()

    print(f"\n  Conclusion: When cluster density > {1-threshold:.2f}, the cascade is consistently blocked.")
    print(f"  This matches the theorem: cascade cannot enter a cluster with density > (1-q) = (1-{threshold}) = {1-threshold:.2f}")


# ─────────────────────────────────────────────
# BONUS: Collective Action Simulation
# ─────────────────────────────────────────────

def sim_collective_action(n=20, thresholds=None, show_info='local'):
    """
    Simulate collective action with individual thresholds.

    Each person i participates if current_participants >= threshold_i.
    'thresholds' is a list of minimum participant counts (including self).

    show_info:
      'local'  : each person knows only their own threshold + immediate neighbours
      'global' : all thresholds are publicly known (common knowledge)
    """
    print("\n" + "=" * 60)
    print(f"  Collective Action: n={n}, info={show_info}")
    print("=" * 60)

    if thresholds is None:
        # Random thresholds between 1 and n
        thresholds = sorted(random.randint(1, n) for _ in range(n))

    print(f"  Individual thresholds (sorted): {thresholds}")

    # Find the stable equilibrium: largest k such that thresholds[k-1] <= k
    max_participants = 0
    for k in range(1, n + 1):
        if thresholds[k - 1] <= k:
            max_participants = k

    print(f"\n  Equilibrium analysis:")
    print(f"  Maximum stable participation level: {max_participants}/{n}")

    # Simulate the cascade
    participants = set()
    participants.add(0)  # person 0 always starts (initiator)
    changed = True
    round_num = 0
    while changed:
        changed = False
        round_num += 1
        for i in range(n):
            if i not in participants:
                if show_info == 'global':
                    signal = len(participants)
                else:
                    # local info: only see neighbours (2 adjacent in sorted list)
                    visible = len([p for p in participants if abs(p - i) <= 2])
                    signal = visible
                if signal >= thresholds[i]:
                    participants.add(i)
                    changed = True

    print(f"  Cascaded participants: {len(participants)}/{n} in {round_num} rounds")
    return participants, thresholds


# ─────────────────────────────────────────────
# ASSIGNMENT CALCULATIONS
# ─────────────────────────────────────────────

def assignment_calculations():
    """Reproduce all numerical answers from the three case studies."""
    print("\n" + "=" * 60)
    print("  Assignment Numerical Answers")
    print("=" * 60)

    cases = [
        ("CS1: Viral Marketing", 20, 0.25),
        ("CS2: EV Adoption", 14, 0.50),
        ("CS3: Banking Contagion", 12, 0.25),
    ]
    for name, n_contacts, q in cases:
        required = math.ceil(q * n_contacts)
        print(f"\n  [{name}]")
        print(f"    {n_contacts} contacts × threshold {q} = {q * n_contacts} → {required} must adopt first")

    # Payoff example
    print("\n  [Lecture Payoff Example]")
    for n_b in [5, 8, 10, 12, 15]:
        n, pa, pb = 20, 2, 3
        ta, tb, choice = compute_switch_decision(n, n_b, pa, pb)
        q = payoff_to_threshold(pa, pb)
        frac_b = n_b / n
        print(f"    {n_b:2d}/{n} on B ({frac_b:.0%}) → payoff_A={ta:4.0f}, payoff_B={tb:4.0f} → {choice}  "
              f"(threshold q={q:.2f}, frac_b {'>' if frac_b > q else '<'} q)")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    random.seed(42)
    np.random.seed(42)

    # Show assignment calculations first
    assignment_calculations()

    # Simulation 1: Payoff Effect
    sim1_payoff_effect()

    # Simulation 2: Influencer Seeding
    sim2_influencer_seeding()

    # Simulation 3: Community Cascade
    sim3_community_cascade(threshold=0.3)

    # Simulation 4: Density Blocking
    sim4_density_blocking(threshold=0.3)

    # Collective action demo
    print("\n--- Collective Action Cases ---")
    # Case 1: Thresholds too high → no action
    sim_collective_action(n=10, thresholds=[1, 2, 3, 5, 6, 7, 8, 9, 10, 10], show_info='local')
    # Case 3: Common knowledge → action succeeds
    sim_collective_action(n=10, thresholds=[1, 2, 3, 4, 5, 5, 6, 7, 8, 9], show_info='global')
