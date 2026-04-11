# Emergence of Connectedness

## Core Question

Suppose we start with `n` isolated vertices and add edges between randomly chosen pairs of vertices. At first, the graph consists of many disconnected components. As more edges are added, small components merge into larger components, and eventually the graph becomes connected.

The central question is:

> **When does a randomly growing graph become connected?**

This is one of the classic questions in random graph theory.

---

## What Is a Connected Graph?

A graph is **connected** if every vertex can reach every other vertex by following a sequence of edges.

For example, if a graph contains vertices `{A, B, C, D}`:

- It is connected if there is a path from every vertex to every other vertex.
- It is disconnected if at least one vertex or group of vertices is separated from the rest.

### Connected vs. Disconnected

| Graph State | Meaning |
|---|---|
| Connected | Every node is reachable from every other node. |
| Disconnected | At least two nodes or components cannot reach each other. |
| Isolated vertex | A vertex with degree `0`; it has no incident edges. |
| Component | A maximal connected part of the graph. |

---

## Random Edge Addition

Imagine a graph with `n = 100` vertices. At the beginning, there are no edges. We repeatedly choose two distinct vertices uniformly at random and place an edge between them.

As the number of edges grows:

1. Many isolated vertices remain at first.
2. Small components begin to form.
3. A **giant component** appears, containing a large fraction of the vertices.
4. Eventually, the last isolated vertices are absorbed.
5. The graph becomes connected.

> **Pro-tip:** In random graphs, the main obstacle to full connectedness is often the existence of isolated vertices. Once isolated vertices disappear, the graph is usually very close to becoming connected.

---

## Probability That a Vertex Remains Isolated

Let `v` be a fixed vertex in a graph with `n` vertices.

When one random edge is added:

- The edge has two endpoints.
- The probability that `v` is selected as one endpoint is approximately `2/n`.
- Therefore, the probability that `v` is **not** selected by that edge is approximately:

```text
1 - 2/n
```

After `k` independently chosen random edges, the approximate probability that `v` is still isolated is:

```text
(1 - 2/n)^k
```

This approximation becomes easier to analyze using the exponential limit:

```text
(1 - 2/n)^k approx e^(-2k/n)
```

---

## Important Edge Counts

### If `k = n`

If we add around `n` edges, then:

```text
(1 - 2/n)^n approx e^(-2)
```

So a fixed vertex still has a substantial chance of being isolated:

```text
e^(-2) approx 0.135
```

That means the graph is very unlikely to be connected, because many vertices may still be isolated.

### If `k = n log n`

If we add around `n log n` edges, then:

```text
(1 - 2/n)^(n log n) approx e^(-2 log n) = 1/n^2
```

So the probability that a particular vertex remains isolated becomes very small:

```text
1/n^2
```

For `n = 100`:

```text
1/n^2 = 1/10000 = 0.0001
```

This is why the lecture-level rule of thumb says:

> A random graph becomes connected after roughly `n log n` random edge additions.

---

## Technical Precision: The Classical Threshold

The more precise classical result for the Erdos-Renyi random graph `G(n, m)` says the connectivity threshold occurs around:

```text
m = (n/2) log n
```

The difference between `(n/2) log n` and `n log n` comes from the exact random graph model and how the edge-addition process is counted. In many introductory explanations, using `n log n` highlights the key intuition: connectedness emerges when isolated vertices become extremely unlikely.

| Expression | Interpretation |
|---|---|
| `n` edges | Many isolated vertices may remain. |
| `(n/2) log n` edges | Classical connectivity threshold in `G(n, m)`. |
| `n log n` edge additions | A common simplified lecture-scale estimate showing isolation probability near `1/n^2`. |

---

## Reverse Experiment: Removing Edges

Another way to ask the same question is to begin with a complete graph on `n` vertices and remove edges one by one.

A **complete graph** `K_n` has every possible edge:

```text
n(n - 1) / 2
```

For `n = 100`, this is:

```text
100 x 99 / 2 = 4950 edges
```

As edges are removed randomly:

- The graph remains connected for a long time.
- It eventually becomes vulnerable around the same threshold region.
- Disconnection is likely when some vertex or group of vertices loses all its external links.

---

## Summary

- A graph is connected when every vertex can reach every other vertex.
- When random edges are added, connectedness appears suddenly around a threshold.
- A fixed vertex avoids one random edge with probability approximately `1 - 2/n`.
- After `k` edges, the probability that it remains isolated is approximately `(1 - 2/n)^k`.
- At `k = n`, this probability is about `e^-2`.
- At `k = n log n`, this probability is about `1/n^2`.
- The formal Erdos-Renyi connectivity threshold is around `(n/2) log n` edges.

