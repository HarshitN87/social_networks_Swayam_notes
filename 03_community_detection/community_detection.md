# Community Detection

## What Is a Community?

A **community** in a graph is a group of nodes with many connections inside the group and relatively fewer connections to the rest of the graph.

In social networks, communities might represent:

- Friend groups
- Departments in an organization
- Research fields
- Online fandoms
- Geographic neighborhoods
- Collaboration groups

In technical terms:

> A community is a region of a graph with dense internal connectivity and sparse external connectivity.

---

## What Is a Partition?

A **partition** divides the vertices of a graph into groups so that every node belongs to exactly one group.

A good community partition usually has:

- Many **intra-community edges**: edges inside the same community.
- Few **inter-community edges**: edges crossing between different communities.

| Edge Type | Meaning |
|---|---|
| Intra-community edge | Both endpoints are in the same community. |
| Inter-community edge | The endpoints are in different communities. |

> **Valid community intuition:** A partition is meaningful if it places densely connected nodes together and separates regions connected by relatively few edges.

---

## Detecting Communities by Looking for Bottlenecks

One way to detect communities is to look for edges that act as bottlenecks between groups.

If removing a small number of edges separates the graph into meaningful pieces, those edges likely connect communities.

This idea leads to the concept of **betweenness**.

---

## Betweenness

**Betweenness centrality** measures how often a node or edge lies on shortest paths between other nodes.

### Node Betweenness

A node has high betweenness if many shortest paths between other node pairs pass through it.

Such nodes often act as:

- Brokers
- Gatekeepers
- Connectors between communities

### Edge Betweenness

An edge has high betweenness if many shortest paths between pairs of nodes pass through that edge.

Edges between communities often have high betweenness because they serve as narrow routes between dense regions.

```text
Community A ---- high-betweenness edge ---- Community B
```

---

## Girvan-Newman Algorithm

The **Girvan-Newman algorithm** is a classic community-detection method based on edge betweenness.

### Algorithm Steps

1. Compute edge betweenness for all edges.
2. Remove the edge with the highest betweenness.
3. Recompute edge betweenness because shortest paths may have changed.
4. Repeat until the graph splits into communities.
5. Continue if more hierarchical levels of communities are needed.

> **Important:** Edge betweenness must be recomputed after each removal. Removing one bridge-like edge changes the shortest paths in the remaining graph.

---

## Girvan-Newman vs. Brute Force Partitioning

| Method | Idea | Strength | Limitation |
|---|---|---|---|
| Brute force | Try many possible partitions and score them. | Conceptually simple for tiny graphs. | Becomes computationally impossible as graphs grow. |
| Girvan-Newman | Remove high-betweenness edges to reveal communities. | Interpretable and historically important. | Can be slow on large graphs. |

The brute-force method in the raw notes compares partitions by maximizing:

```text
(intra-community edges in group 1 + intra-community edges in group 2) / inter-community edges
```

This captures the intuition that communities should have many internal edges and few crossing edges.

However, brute force has a major problem: the number of possible partitions grows extremely fast. For real graphs, algorithms like Girvan-Newman, Louvain, Leiden, or spectral methods are more practical.

---

## Summary

- Communities are groups with dense internal connections and sparse external connections.
- A partition divides the graph into non-overlapping groups.
- Edge betweenness measures how often an edge lies on shortest paths.
- Edges connecting communities often have high betweenness.
- The Girvan-Newman algorithm repeatedly removes high-betweenness edges to reveal communities.

