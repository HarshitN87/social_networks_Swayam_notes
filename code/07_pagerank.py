"""
07_pagerank.py
==============
Implements PageRank three ways and compares them:
  1. Points Distribution Method (Power Iteration)
  2. Random Walk Method (Monte Carlo)
  3. NetworkX built-in (ground truth)
  4. Degree Rank comparison

Graph used: directed graph where nodes are pages/creators/teams
and directed edges represent endorsements/links/losses.
"""

import random
import math
import networkx as nx
import matplotlib.pyplot as plt


# ─────────────────────────────────────────────
# HELPER: Build a sample directed graph
# ─────────────────────────────────────────────

def build_sample_graph():
    """
    A small directed web/influence graph for demonstration.
    Node 0 is a 'hub' (many inbound links).
    Node 5 is a 'sink' (no outgoing links).
    """
    G = nx.DiGraph()
    # edges: (from, to) = endorser endorse recipient
    edges = [
        (1, 0), (2, 0), (3, 0),   # nodes 1,2,3 all endorse node 0
        (0, 4),                     # node 0 endorses node 4
        (4, 2), (4, 3),             # node 4 endorses 2 and 3
        (2, 1), (3, 1),             # nodes 2,3 endorse node 1
        (1, 5),                     # node 1 endorses node 5 (sink)
        (6, 0), (6, 1),             # node 6 endorses 0 and 1
    ]
    G.add_edges_from(edges)
    # Add all nodes explicitly (some may be isolated)
    for i in range(7):
        G.add_node(i)
    return G


# ─────────────────────────────────────────────
# METHOD 1: Points Distribution (Power Iteration)
# ─────────────────────────────────────────────

def pagerank_points_distribution(G, damping=0.85, initial_points=100, max_iter=1000, tol=1e-6):
    """
    Iterative Points Distribution Method for PageRank.

    Each node starts with `initial_points`. At each step:
      1. Nodes distribute ALL their current points equally to their out-neighbours.
      2. Sink nodes (no out-edges) teleport their points uniformly to all nodes.
      3. Apply damping: score = damping * distributed_score + (1-damping) * uniform_share

    Args:
        G         : networkx DiGraph
        damping   : probability of following an actual link (0.85 by default)
        initial_points: starting value for every node
        max_iter  : maximum number of iterations
        tol       : convergence threshold (L1 norm)

    Returns:
        dict of {node: pagerank_score}
    """
    n = G.number_of_nodes()
    nodes = list(G.nodes())

    # Initialize scores
    scores = {v: float(initial_points) for v in nodes}
    total_points = initial_points * n                    # conserved total

    for iteration in range(max_iter):
        new_scores = {v: 0.0 for v in nodes}

        # Step 1: Distribute points from each node to its out-neighbours
        sink_total = 0.0
        for u in nodes:
            out_neighbours = list(G.successors(u))
            if out_neighbours:
                share = scores[u] / len(out_neighbours)
                for v in out_neighbours:
                    new_scores[v] += share
            else:
                # Sink node: will teleport uniformly
                sink_total += scores[u]

        # Step 2: Distribute sink points uniformly to all nodes
        sink_share = sink_total / n
        for v in nodes:
            new_scores[v] += sink_share

        # Step 3: Apply damping factor
        # damping fraction goes through the graph; (1-damping) teleports
        teleport_share = (total_points * (1.0 - damping)) / n
        for v in nodes:
            new_scores[v] = damping * new_scores[v] + teleport_share

        # Check convergence (L1 norm difference)
        diff = sum(abs(new_scores[v] - scores[v]) for v in nodes)
        scores = new_scores

        if diff < tol:
            print(f"  [Points Distribution] Converged after {iteration + 1} iterations.")
            break
    else:
        print(f"  [Points Distribution] Did NOT converge in {max_iter} iterations.")

    # Normalize to sum to 1
    total = sum(scores.values())
    return {v: scores[v] / total for v in nodes}


# ─────────────────────────────────────────────
# METHOD 2: Random Walk (Monte Carlo)
# ─────────────────────────────────────────────

def pagerank_random_walk(G, damping=0.85, num_walks=500_000):
    """
    Random Walk (Monte Carlo) Method for PageRank.

    A random surfer:
      - With probability `damping`: follows a random outgoing edge from current node.
      - With probability (1 - damping): teleports to a completely random node.
      - At sink nodes: always teleports (no outgoing edges to follow).

    Each visit to a node increments its counter.
    Final PageRank = visit_count / total_steps.

    Args:
        G         : networkx DiGraph
        damping   : probability of following an actual link (0.85 by default)
        num_walks : total number of random walk steps

    Returns:
        dict of {node: pagerank_score}
    """
    nodes = list(G.nodes())
    n = len(nodes)
    visit_count = {v: 0 for v in nodes}

    # Start at a random node
    current = random.choice(nodes)

    for _ in range(num_walks):
        visit_count[current] += 1

        out_neighbours = list(G.successors(current))

        if out_neighbours and random.random() < damping:
            # Follow a random outgoing link
            current = random.choice(out_neighbours)
        else:
            # Teleport: jump to any random node
            current = random.choice(nodes)

    # Normalize to sum to 1
    total = sum(visit_count.values())
    return {v: visit_count[v] / total for v in nodes}


# ─────────────────────────────────────────────
# METHOD 3: NetworkX built-in (ground truth)
# ─────────────────────────────────────────────

def pagerank_networkx(G, damping=0.85):
    """Wrapper around NetworkX's built-in PageRank."""
    return nx.pagerank(G, alpha=damping)


# ─────────────────────────────────────────────
# DEGREE RANK (In-Degree Centrality)
# ─────────────────────────────────────────────

def degree_rank(G):
    """
    Simple in-degree rank: rank nodes by how many incoming links they have.
    Normalized by (n-1) to be in [0, 1].
    """
    return dict(nx.in_degree_centrality(G))


# ─────────────────────────────────────────────
# COMPARISON & VISUALIZATION
# ─────────────────────────────────────────────

def compare_methods(G, damping=0.85):
    """Run all methods and print a side-by-side comparison table."""
    print("\n" + "=" * 60)
    print("  PageRank Method Comparison")
    print("=" * 60)

    pr_points = pagerank_points_distribution(G, damping=damping)
    pr_walk   = pagerank_random_walk(G, damping=damping, num_walks=500_000)
    pr_nx     = pagerank_networkx(G, damping=damping)
    dr        = degree_rank(G)

    nodes = sorted(G.nodes())

    print(f"\n{'Node':>6} | {'Points Dist':>12} | {'Random Walk':>12} | {'NetworkX':>10} | {'Degree Rank':>12}")
    print("-" * 62)
    for v in nodes:
        print(f"  {v:>4} | {pr_points[v]:>12.5f} | {pr_walk[v]:>12.5f} | {pr_nx[v]:>10.5f} | {dr[v]:>12.5f}")

    print("\n  Rank order by PageRank (NetworkX):")
    ranked = sorted(pr_nx.items(), key=lambda x: x[1], reverse=True)
    for rank, (node, score) in enumerate(ranked, 1):
        print(f"    #{rank}: Node {node}  (PR={score:.5f}, Degree Rank={dr[node]:.5f})")

    return pr_points, pr_walk, pr_nx, dr


def plot_comparison(G, pr_nx, dr):
    """
    Plot PageRank vs. Degree Rank for all nodes to visualize
    why the two metrics disagree.
    """
    nodes = sorted(G.nodes())
    pr_vals = [pr_nx[v] for v in nodes]
    dr_vals = [dr[v] for v in nodes]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("PageRank vs. Degree Rank", fontsize=14, fontweight='bold')

    # --- Bar chart side by side ---
    x = range(len(nodes))
    width = 0.35
    axes[0].bar([i - width/2 for i in x], pr_vals, width, label='PageRank', color='steelblue')
    axes[0].bar([i + width/2 for i in x], dr_vals, width, label='Degree Rank', color='coral')
    axes[0].set_xticks(list(x))
    axes[0].set_xticklabels([f"Node {n}" for n in nodes], rotation=30)
    axes[0].set_title("Score Comparison per Node")
    axes[0].set_ylabel("Score (normalized)")
    axes[0].legend()
    axes[0].grid(axis='y', linestyle='--', alpha=0.5)

    # --- Scatter: Degree Rank vs PageRank ---
    in_degrees = [G.in_degree(v) for v in nodes]
    axes[1].scatter(in_degrees, pr_vals, color='steelblue', s=120, zorder=5)
    for i, v in enumerate(nodes):
        axes[1].annotate(f"  Node {v}", (in_degrees[i], pr_vals[i]), fontsize=8)
    axes[1].set_xlabel("In-Degree (raw count)")
    axes[1].set_ylabel("PageRank Score")
    axes[1].set_title("In-Degree vs. PageRank\n(non-linear scatter = they measure different things)")
    axes[1].grid(linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig("pagerank_vs_degreerank.png", dpi=150)
    print("\n  Plot saved to 'pagerank_vs_degreerank.png'")
    plt.show()


def visualize_graph(G, pr_nx):
    """Draw the directed graph with node size proportional to PageRank."""
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)

    node_sizes  = [pr_nx[v] * 8000 for v in G.nodes()]
    node_colors = [pr_nx[v] for v in G.nodes()]

    nx.draw_networkx_nodes(G, pos, node_size=node_sizes,
                           node_color=node_colors, cmap=plt.cm.YlOrRd, alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_color='black', font_weight='bold')
    nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20,
                           edge_color='gray', connectionstyle='arc3,rad=0.1')

    sm = plt.cm.ScalarMappable(cmap=plt.cm.YlOrRd,
                                norm=plt.Normalize(vmin=min(pr_nx.values()),
                                                   vmax=max(pr_nx.values())))
    sm.set_array([])
    plt.colorbar(sm, label='PageRank Score')
    plt.title("Web Graph – Node Size & Color ∝ PageRank", fontsize=13)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("web_graph_pagerank.png", dpi=150)
    print("  Graph saved to 'web_graph_pagerank.png'")
    plt.show()


# ─────────────────────────────────────────────
# n log n RANDOM WALK COVERAGE DEMO
# ─────────────────────────────────────────────

def nlogn_coverage_demo():
    """
    Demonstrates the n log n rule for random walk coverage.
    Shows how many steps are needed to visit all n nodes at least once.
    """
    print("\n" + "=" * 50)
    print("  n·ln(n) Random Walk Coverage Estimates")
    print("=" * 50)
    test_cases = [30, 100, 1000, 8000, 10000, 50000]
    print(f"{'n':>8} | {'n·ln(n)':>14} | {'approx':>10}")
    print("-" * 38)
    for n in test_cases:
        steps = n * math.log(n)
        print(f"{n:>8,} | {steps:>14,.1f} | ~{round(steps,-3):>10,}")


# ─────────────────────────────────────────────
# BASKETBALL / NCAA EXAMPLE
# ─────────────────────────────────────────────

def ncaa_example():
    """
    Builds the directed graph from Case Study 2:
    Edges go FROM loser TO winner.
    Runs PageRank and compares with simple win-count ranking.
    """
    print("\n" + "=" * 50)
    print("  NCAA Basketball PageRank Example")
    print("=" * 50)

    # Define game results as (winner, loser)
    results = [
        ("Duke", "UNC"),
        ("UNC",  "Kentucky"),
        ("Duke", "Kentucky"),
        ("Michigan", "Duke"),
        ("Michigan", "Louisville"),
        ("Louisville", "Duke"),
        ("Louisville", "UNC"),
        ("Syracuse", "UNC"),
        ("Syracuse", "Kentucky"),
        ("Michigan", "Georgetown"),
    ]

    G = nx.DiGraph()
    win_count = {}
    for winner, loser in results:
        G.add_edge(loser, winner)   # edge from LOSER to WINNER
        win_count[winner] = win_count.get(winner, 0) + 1
        win_count.setdefault(loser, 0)

    pr = nx.pagerank(G, alpha=0.85)

    print("\n  PageRank ranking:")
    for rank, (team, score) in enumerate(sorted(pr.items(), key=lambda x: x[1], reverse=True), 1):
        wins = win_count.get(team, 0)
        print(f"    #{rank}: {team:<12} PR={score:.4f}  Wins={wins}")

    print("\n  Win-count ranking:")
    for rank, (team, wins) in enumerate(sorted(win_count.items(), key=lambda x: x[1], reverse=True), 1):
        print(f"    #{rank}: {team:<12} Wins={wins}  PR={pr.get(team, 0):.4f}")

    print("\n  Observation: PageRank captures TRANSITIVE strength.")
    print("  e.g. Louisville beat Duke → Duke beat UNC → UNC beat Kentucky")
    print("  Louisville gains indirect validation from this chain.")


# ─────────────────────────────────────────────
# ASSIGNMENT NUMERICAL ANSWERS
# ─────────────────────────────────────────────

def assignment_answers():
    """Print step-by-step solutions to the numerical assignment questions."""
    print("\n" + "=" * 60)
    print("  Assignment Answer Calculations")
    print("=" * 60)

    # Q1: n log n for n=8000
    n = 8000
    steps = n * math.log(n)
    print(f"\n[Q1] TrendHub n={n:,} creators:")
    print(f"     {n} × ln({n}) = {n} × {math.log(n):.4f} = {steps:,.1f}")
    print(f"     ≈ 72,000 steps  ✅")

    # Q4: Jordan percentage
    visits = 3500
    total = 100_000
    pct = visits / total * 100
    print(f"\n[Q4] Jordan visits: {visits:,} / {total:,} × 100 = {pct} %  ✅")

    # Case Study 2: Alpha points
    alpha_pts = 240
    opponents = 3
    per_opp = alpha_pts / opponents
    print(f"\n[CS2-Q1] Alpha {alpha_pts} pts ÷ {opponents} opponents = {per_opp} pts each  ✅")

    # Case Study 2: Team B total
    a_pts, a_losses = 500, 2   # A lost to B and C
    d_pts, d_losses = 300, 1   # D lost only to B
    e_pts, e_losses = 200, 3   # E lost to B, C, D

    b_from_a = a_pts / a_losses
    b_from_d = d_pts / d_losses
    b_from_e = e_pts / e_losses
    total_b  = b_from_a + b_from_d + b_from_e
    print(f"\n[CS2-Q4] Team B receives:")
    print(f"     From A: {a_pts}/{a_losses} = {b_from_a}")
    print(f"     From D: {d_pts}/{d_losses} = {b_from_d}")
    print(f"     From E: {e_pts}/{e_losses} = {b_from_e:.4f}")
    print(f"     Total  = {total_b:.2f} ≈ 617  ✅")

    # Case Study 3: Damping calculation
    paper_pts = 250
    s = 0.8
    n_papers = 500
    total_pts = n_papers * 100
    retained = paper_pts * s
    redistributed_pool = total_pts * (1 - s)
    per_paper_redistribution = redistributed_pool / n_papers
    print(f"\n[CS3-Q1] Paper with {paper_pts} pts, s={s}, n={n_papers} papers, total={total_pts} pts:")
    print(f"     Retained:       {paper_pts} × {s} = {retained}")
    print(f"     Redistribution pool: {total_pts} × {1-s} = {redistributed_pool}")
    print(f"     Each paper receives: {redistributed_pool} / {n_papers} = {per_paper_redistribution}")
    print(f"     Answer: 200 retained + 10 redistribution  ✅")

    # Case Study 3: PR/in-degree ratio
    pr1, deg1 = 0.0087, 5
    pr2, deg2 = 0.0031, 150
    ratio1 = pr1 / deg1
    ratio2 = pr2 / deg2
    result = ratio1 / ratio2
    print(f"\n[CS3-Q3] PR/in-degree ratio:")
    print(f"     Paper 1: {pr1}/{deg1} = {ratio1}")
    print(f"     Paper 2: {pr2}/{deg2} = {ratio2:.8f}")
    print(f"     Ratio:   {ratio1} / {ratio2:.8f} = {result:.2f}  ✅")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("Building sample directed graph...")
    G = build_sample_graph()

    # Compare all three PageRank methods
    pr_points, pr_walk, pr_nx, dr = compare_methods(G, damping=0.85)

    # Visualize
    visualize_graph(G, pr_nx)
    plot_comparison(G, pr_nx, dr)

    # n log n demo
    nlogn_coverage_demo()

    # NCAA example
    ncaa_example()

    # Assignment answers
    assignment_answers()
