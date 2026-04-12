# Network Science Knowledge Base

This knowledge base organizes the raw notes into a structured study guide on **connectedness**, **weak ties**, **clustering**, **community detection**, and **PageRank** in social and graph networks.

## File Structure

| File / Folder | Purpose |
|---|---|
| `01_Emergence_of_Connectedness.md` | Explains how connectedness emerges in random graphs and why the phase transition threshold is around $n \ln n$ edge additions. |
| `02_Strength_of_Weak_Ties.md` | Covers Granovetter's strength of weak ties, triadic closure, clustering coefficients, and the sociological importance of local bridges. |
| `03_Community_Detection.md` | Explains communities, partitions, edge betweenness, and how the Girvan-Newman algorithm fragments a graph. |
| `04_Homophily_and_Social_Influence.md` | Covers homophily, distinguishing selection vs. social influence, network closure mechanisms, and the Fatman evolutionary model. |
| `06_Structural_Balance.md` | Covers signed networks, triadic stability, the Balance Theorem, and faction identification using BFS. |
| `07_PageRank_and_Web_Graph.md` | Covers PageRank from first principles: the web graph, n·ln(n) random walk coverage, coin-dropping intuition, points distribution, random walk Monte Carlo, damping factors, and PageRank vs. Degree Rank. Includes full assignment case study solutions. |
| `08_Diffusion_and_Cascades.md` | Covers how behaviour spreads in networks: the coordination game, payoff threshold formula, cascade mechanics, community structure blocking, the Cluster Density Theorem (density > 1−q), collective action problems, and all 3 case study assignment answers. |
| `09_HITS_and_Recommender_Systems.md` | Covers the HITS algorithm (hub & authority scores), bipartite recommender scoring with iterative normalization, PageRank matrix formulation, Markov matrices, eigenvalue convergence proof, and all 3 case study assignment answers with key traps. |
| `code/` | Contains corrected and commented Python NetworkX coding examples, including introductory functions, community-detection scripts, the Fatman model simulation, PageRank implementations, and 4 diffusion/cascade simulations. |
| `images/` | Contains image assets used throughout the markdown documentation. |

> **Key idea:** A network is not only a collection of nodes and edges. Its structure controls how information, opportunities, influence, and risk move through the entire system.

---

## Suggested Reading Order

1. Start with the foundation: [`01_Emergence_of_Connectedness.md`](01_Emergence_of_Connectedness.md)
2. Learn about social edges: [`02_Strength_of_Weak_Ties.md`](02_Strength_of_Weak_Ties.md)
3. Learn to split networks: [`03_Community_Detection.md`](03_Community_Detection.md)
4. Understand peer dynamics: [`04_Homophily_and_Social_Influence.md`](04_Homophily_and_Social_Influence.md)
5. Model social segregation: [`05_Schelling_Model.md`](05_Schelling_Model.md)
6. Study alliance formation: [`06_Structural_Balance.md`](06_Structural_Balance.md)
7. Learn network importance ranking: [`07_PageRank_and_Web_Graph.md`](07_PageRank_and_Web_Graph.md)
8. Understand how behaviours spread: [`08_Diffusion_and_Cascades.md`](08_Diffusion_and_Cascades.md)
9. Learn HITS, recommender scoring & PageRank linear algebra: [`09_HITS_and_Recommender_Systems.md`](09_HITS_and_Recommender_Systems.md)
10. Finally, view the practical examples and simulations in the [`code/`](code/) directory.
