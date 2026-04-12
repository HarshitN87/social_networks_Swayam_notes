"""
Epidemic Models, R₀ Calculations & Fixed-Point Solver
=====================================================
Implements:
  1. SIR simulation on a network
  2. SIS simulation on a network
  3. R₀ calculator with expected infections at each level
  4. Fixed-point solver for q* = 1 - (1 - p*q*)^k
  5. Branching process simulation

Usage:
  python 11_epidemic_models.py

Requires: networkx, matplotlib, numpy
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from collections import defaultdict


# ──────────────────────────────────────────────────────────
# 1. R₀ CALCULATOR
# ──────────────────────────────────────────────────────────


def calculate_r0(p, k):
    """
    Calculate the Basic Reproductive Number R₀.

    Parameters
    ----------
    p : float — probability of infection across a single link
    k : int or float — number of contacts per individual

    Returns
    -------
    R0 : float

    Formula: R₀ = p × k
    """
    R0 = p * k
    print(f"R₀ = p × k = {p} × {k} = {R0}")

    if R0 < 1:
        print(f"  → R₀ < 1: Disease CERTAINLY dies out (probability = 1)")
    elif R0 == 1:
        print(f"  → R₀ = 1: Knife-edge — critical threshold")
    else:
        print(f"  → R₀ > 1: Disease can become epidemic (positive probability)")

    return R0


def expected_infections_at_level(R0, level):
    """
    Calculate expected number of infections at a given level
    of the branching tree.

    Formula: Expected infections at level i = R₀^i
    """
    expected = R0 ** level
    print(f"  Level {level}: Expected infections = R₀^{level} = {R0}^{level} = {expected:.1f}")
    return expected


# ──────────────────────────────────────────────────────────
# 2. FIXED-POINT SOLVER FOR q*
# ──────────────────────────────────────────────────────────


def characteristic_function(x, p, k):
    """f(x) = 1 - (1 - p*x)^k"""
    return 1.0 - (1.0 - p * x) ** k


def find_q_star(p, k, iterations=200):
    """
    Find q* by iterating f(x) starting from x = 1.

    The fixed point q* satisfies: q* = 1 - (1 - p*q*)^k
    where q* is the probability that the infection reaches
    infinite depth (i.e., the probability of an epidemic).

    Parameters
    ----------
    p : float — transmission probability
    k : int — contacts per node
    iterations : int — number of iterations

    Returns
    -------
    q_star : float — the fixed point value
    trajectory : list — the convergence path
    """
    x = 1.0  # Start at x = 1
    trajectory = [x]

    for _ in range(iterations):
        x = characteristic_function(x, p, k)
        trajectory.append(x)

    R0 = p * k
    print(f"\nFixed-point analysis for p={p}, k={k}")
    print(f"  R₀ = {R0}")
    print(f"  f'(0) = pk = {R0} (derivative at origin)")
    print(f"  q* = {x:.6f}")

    if x < 1e-10:
        print(f"  → q* = 0: Disease dies out with certainty")
    else:
        print(f"  → q* > 0: Disease persists with probability {x:.4f}")

    return x, trajectory


def plot_fixed_point_analysis(p, k):
    """
    Visualize the cobwebbing / fixed-point analysis.
    Plots f(x) = 1 - (1-px)^k against y = x.
    """
    x_vals = np.linspace(0, 1, 500)
    f_vals = [characteristic_function(x, p, k) for x in x_vals]

    R0 = p * k
    q_star, trajectory = find_q_star(p, k)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: The function vs identity line
    axes[0].plot(x_vals, f_vals, color='#f97316', linewidth=2.5,
                 label=f'f(x) = 1 - (1-{p}x)^{k}')
    axes[0].plot(x_vals, x_vals, color='#818cf8', linewidth=1.5,
                 linestyle='--', label='y = x')
    axes[0].scatter([q_star], [q_star], color='#34d399', s=100, zorder=5,
                    label=f'q* = {q_star:.4f}')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('f(x)')
    axes[0].set_title(f'Fixed Point Analysis (R₀ = {R0:.2f})')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlim(0, 1)
    axes[0].set_ylim(0, 1)

    # Right: Convergence trajectory
    axes[1].plot(range(len(trajectory)), trajectory, color='#f97316',
                 linewidth=2, marker='o', markersize=3)
    axes[1].axhline(y=q_star, color='#34d399', linestyle='--', linewidth=1.5,
                    label=f'q* = {q_star:.4f}')
    axes[1].set_xlabel('Iteration')
    axes[1].set_ylabel('q_n')
    axes[1].set_title(f'Convergence of q_n → q* (p={p}, k={k})')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.suptitle(f'Epidemic Persistence Analysis', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('fixed_point_analysis.png', dpi=150, bbox_inches='tight')
    plt.show()


# ──────────────────────────────────────────────────────────
# 3. SIR SIMULATION ON A NETWORK
# ──────────────────────────────────────────────────────────


def simulate_sir(G, seed_nodes, p, T_I, max_steps=200):
    """
    Run an SIR epidemic simulation on a network.

    Parameters
    ----------
    G : nx.Graph — the network
    seed_nodes : list — initially infected nodes
    p : float — transmission probability per edge per time step
    T_I : int — number of time steps a node remains infectious
    max_steps : int — maximum simulation duration

    Returns
    -------
    history : dict — states at each time step
        {'S': [count_t0, count_t1, ...], 'I': [...], 'R': [...]}
    final_state : dict — node → final state ('S', 'I', or 'R')

    The SIR model:
    - S → I: susceptible gets infected (prob p per infected neighbor)
    - I → R: infected recovers after T_I steps (permanent immunity)
    """
    # Initialize states
    state = {}
    infection_timer = {}  # How many steps since infection

    for node in G.nodes():
        state[node] = 'S'

    for seed in seed_nodes:
        state[seed] = 'I'
        infection_timer[seed] = 0

    # Track counts over time
    history = {'S': [], 'I': [], 'R': []}

    for step in range(max_steps):
        # Record current state counts
        s_count = sum(1 for v in state.values() if v == 'S')
        i_count = sum(1 for v in state.values() if v == 'I')
        r_count = sum(1 for v in state.values() if v == 'R')
        history['S'].append(s_count)
        history['I'].append(i_count)
        history['R'].append(r_count)

        # Stop if no infected nodes remain
        if i_count == 0:
            break

        # Determine new infections and recoveries
        new_infected = set()
        new_recovered = set()

        for node in list(G.nodes()):
            if state[node] == 'I':
                # Try to infect susceptible neighbors
                for neighbor in G.neighbors(node):
                    if state[neighbor] == 'S':
                        if random.random() < p:
                            new_infected.add(neighbor)

                # Check if this node should recover
                infection_timer[node] += 1
                if infection_timer[node] >= T_I:
                    new_recovered.add(node)

        # Apply state transitions
        for node in new_infected:
            if state[node] == 'S':  # Might already be newly infected
                state[node] = 'I'
                infection_timer[node] = 0

        for node in new_recovered:
            state[node] = 'R'
            del infection_timer[node]

    return history, state


# ──────────────────────────────────────────────────────────
# 4. SIS SIMULATION ON A NETWORK
# ──────────────────────────────────────────────────────────


def simulate_sis(G, seed_nodes, p, T_I, max_steps=200):
    """
    Run an SIS epidemic simulation on a network.

    Parameters
    ----------
    Same as SIR, but recovered nodes go back to Susceptible.

    The SIS model:
    - S → I: susceptible gets infected (prob p per infected neighbor)
    - I → S: infected recovers and becomes susceptible AGAIN
    - No permanent immunity — can be reinfected
    """
    state = {}
    infection_timer = {}

    for node in G.nodes():
        state[node] = 'S'

    for seed in seed_nodes:
        state[seed] = 'I'
        infection_timer[seed] = 0

    history = {'S': [], 'I': []}

    for step in range(max_steps):
        s_count = sum(1 for v in state.values() if v == 'S')
        i_count = sum(1 for v in state.values() if v == 'I')
        history['S'].append(s_count)
        history['I'].append(i_count)

        if i_count == 0:
            break

        new_infected = set()
        new_susceptible = set()

        for node in list(G.nodes()):
            if state[node] == 'I':
                for neighbor in G.neighbors(node):
                    if state[neighbor] == 'S':
                        if random.random() < p:
                            new_infected.add(neighbor)

                infection_timer[node] += 1
                if infection_timer[node] >= T_I:
                    new_susceptible.add(node)

        # Key difference from SIR: recovered → Susceptible (NOT Recovered)
        for node in new_susceptible:
            state[node] = 'S'
            del infection_timer[node]

        for node in new_infected:
            if state[node] == 'S':
                state[node] = 'I'
                infection_timer[node] = 0

    return history, state


# ──────────────────────────────────────────────────────────
# 5. PLOTTING EPIDEMIC CURVES
# ──────────────────────────────────────────────────────────


def plot_sir_simulation(history, title="SIR Simulation"):
    """Plot the SIR epidemic curve showing S, I, R counts over time."""
    fig, ax = plt.subplots(figsize=(10, 5))

    steps = range(len(history['S']))
    ax.plot(steps, history['S'], color='#60a5fa', linewidth=2.5, label='Susceptible')
    ax.plot(steps, history['I'], color='#f87171', linewidth=2.5, label='Infected')
    ax.plot(steps, history['R'], color='#fbbf24', linewidth=2.5, label='Recovered')

    ax.set_xlabel('Time Step')
    ax.set_ylabel('Number of Nodes')
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('sir_simulation.png', dpi=150, bbox_inches='tight')
    plt.show()


def plot_sis_simulation(history, title="SIS Simulation"):
    """Plot the SIS epidemic curve showing S, I counts over time."""
    fig, ax = plt.subplots(figsize=(10, 5))

    steps = range(len(history['S']))
    ax.plot(steps, history['S'], color='#60a5fa', linewidth=2.5, label='Susceptible')
    ax.plot(steps, history['I'], color='#f87171', linewidth=2.5, label='Infected')

    ax.set_xlabel('Time Step')
    ax.set_ylabel('Number of Nodes')
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('sis_simulation.png', dpi=150, bbox_inches='tight')
    plt.show()


# ──────────────────────────────────────────────────────────
# MAIN: Run all demonstrations
# ──────────────────────────────────────────────────────────


if __name__ == "__main__":
    random.seed(42)
    np.random.seed(42)

    print("=" * 60)
    print("EPIDEMIC MODELS & R₀ DEMONSTRATIONS")
    print("=" * 60)

    # ── Demo 1: R₀ Calculations (Assignment Examples) ──
    print("\n📊 Demo 1: R₀ Calculations")
    print("-" * 40)

    print("\nCase Study 1 — COVID on Campuses:")
    print("Campus A: p=0.25, k=12")
    R0_A = calculate_r0(0.25, 12)
    print("Campus B: p=0.25, k=8")
    R0_B = calculate_r0(0.25, 8)
    print("Campus C: p=0.25, k=4")
    R0_C = calculate_r0(0.25, 4)

    print("\nCampus A after intervention: p=0.20, k=6")
    R0_intervention = calculate_r0(0.20, 6)

    print("\nCase Study 2 — Measles Outbreak:")
    print("Before intervention: p=0.90, k=12")
    R0_measles = calculate_r0(0.90, 12)
    print("\nExpected infections at each level:")
    for level in range(4):
        expected_infections_at_level(R0_measles, level)

    print("\nAfter exclusion policy: p=0.90, k=2")
    R0_post = calculate_r0(0.90, 2)

    print("\nCase Study 3 — Viral Marketing:")
    print("p=0.28, k=5")
    V0 = calculate_r0(0.28, 5)
    print("\nIncreased quality: p=0.32, k=5")
    V0_new = calculate_r0(0.32, 5)

    # ── Demo 2: Fixed-Point Analysis ──
    print("\n📊 Demo 2: Fixed-Point Analysis (q*)")
    print("-" * 40)

    print("\nSupercritical case (R₀ > 1): p=0.28, k=5")
    q_star_super, _ = find_q_star(0.28, 5)

    print("\nSubcritical case (R₀ < 1): p=0.10, k=5")
    q_star_sub, _ = find_q_star(0.10, 5)

    # Plot both cases
    plot_fixed_point_analysis(0.28, 5)  # Supercritical
    plot_fixed_point_analysis(0.10, 5)  # Subcritical

    # ── Demo 3: SIR Simulation ──
    print("\n📊 Demo 3: SIR Simulation")
    print("-" * 40)

    # Build a BA network (power law — realistic)
    G = nx.barabasi_albert_graph(500, 3, seed=42)
    print(f"Network: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # Run SIR with p=0.15, T_I=3
    history_sir, final_sir = simulate_sir(G, seed_nodes=[0], p=0.15, T_I=3)
    total_infected = sum(1 for v in final_sir.values() if v == 'R')
    print(f"Total infected (recovered): {total_infected}/{G.number_of_nodes()}")
    plot_sir_simulation(history_sir, "SIR Simulation on BA Network (p=0.15, T_I=3)")

    # ── Demo 4: SIS Simulation ──
    print("\n📊 Demo 4: SIS Simulation")
    print("-" * 40)

    history_sis, final_sis = simulate_sis(G, seed_nodes=[0], p=0.08, T_I=2,
                                          max_steps=100)
    final_infected = sum(1 for v in final_sis.values() if v == 'I')
    print(f"Infected at end: {final_infected}/{G.number_of_nodes()}")
    plot_sis_simulation(history_sis, "SIS Simulation on BA Network (p=0.08, T_I=2)")

    # ── Demo 5: Branching Process Example ──
    print("\n📊 Demo 5: Branching Process — Exposed vs Expected")
    print("-" * 40)
    k, p = 6, 0.50
    R0 = p * k
    print(f"k={k}, p={p}, R₀={R0}")
    for level in range(4):
        exposed = k ** level
        expected = R0 ** level
        print(f"  Level {level}: Exposed (k^i) = {exposed}, "
              f"Expected infections (R₀^i) = {expected:.1f}")

    print("\n✅ All demonstrations complete!")
