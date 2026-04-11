# Network Science Knowledge Base

This knowledge base organizes the raw notes into a structured study guide on **connectedness**, **weak ties**, **clustering**, and **community detection** in social and graph networks.

## File Structure

| File / Folder | Purpose |
|---|---|
| `01_Emergence_of_Connectedness.md` | Explains how connectedness emerges in random graphs and why the phase transition threshold is around $n \ln n$ edge additions. |
| `02_Strength_of_Weak_Ties.md` | Covers Granovetter's strength of weak ties, triadic closure, clustering coefficients, and the sociological importance of local bridges. |
| `03_Community_Detection.md` | Explains communities, partitions, edge betweenness, and how the Girvan-Newman algorithm fragments a graph. |
| `code/` | Contains corrected and commented Python NetworkX coding examples, including introductory functions and community-detection scripts. |
| `images/` | Contains image assets used throughout the markdown documentation. |

> **Key idea:** A network is not only a collection of nodes and edges. Its structure controls how information, opportunities, influence, and risk move through the entire system.

---

## Suggested Reading Order

1. Start with the foundation: [`01_Emergence_of_Connectedness.md`](01_Emergence_of_Connectedness.md)
2. Learn about social edges: [`02_Strength_of_Weak_Ties.md`](02_Strength_of_Weak_Ties.md)
3. Learn to split networks: [`03_Community_Detection.md`](03_Community_Detection.md)
4. Finally, view the practical examples in the [`code/`](code/) directory.
