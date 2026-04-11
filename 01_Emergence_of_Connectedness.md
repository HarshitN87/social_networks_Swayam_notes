# Emergence of Connectedness

## Introduction
In a network consisting of multiple disconnected nodes, if we begin randomly adding edges (connections) between pairs of nodes, the graph will eventually become entirely connected. A highly fascinating phenomenon in network science is observing *when* and *how* this transition to a connected graph happens.

## The Tipping Point of Connectedness
Imagine two scenarios:
1. **Adding Edges**: Given $n$ disconnected nodes, if we keep adding new edges uniformly at random, at what point does the entire graph merge into one single connected component?
2. **Removing Edges**: Alternatively, take a completely connected graph of 100 nodes (all possible connections exist) and remove edges one by one. At what specific point does the graph break apart into disconnected pieces?

As it turns out, the emergence (or breakdown) of connectedness is not gradual but happens abruptly at a specific threshold.

## The Mathematical Probability of Isolation
To understand when a graph becomes connected, we must first understand when a single vertex stops being isolated (i.e., when no edges point to it). 

Let $n$ be the total number of vertices. 
For any specific vertex $v$:
- The total number of possible edges in the graph is $\frac{n(n-1)}{2}$.
- The total number of possible edges that directly connect to $v$ is $n-1$.
- Thus, the probability of a randomly chosen single edge connecting to $v$ is $\frac{n-1}{n(n-1)/2} = \frac{2}{n}$.
- Therefore, the probability that a single randomly added edge **does not** connect to $v$ is $1 - \frac{2}{n}$.

If we add $k$ independent edges randomly, the probability of vertex $v$ remaining isolated is:
$$ P(\text{iso}) \approx \left(1 - \frac{2}{n}\right)^k $$

### Key Thresholds
Let's analyze what happens as we increase the number of edges, $k$:

1. **When $k = n$ (Edges equal to the number of nodes):**
   $$ \left(1 - \frac{2}{n}\right)^n \approx e^{-2} \approx 0.135 $$
   This means there is still about a 13.5% chance for a vertex to remain isolated. The network is not yet fully connected.

2. **When $k = n \log_e(n)$ (A much larger number of edges):**
   $$ \left(1 - \frac{2}{n}\right)^{n \log n} \approx \left(e^{-2}\right)^{\log n} = n^{-2} = \frac{1}{n^2} $$
   At this point, the probability of *any* single vertex being isolated exponentially decays towards 0 as $n$ grows large. The graph is **almost certainly connected**.

> **Note on Threshold:** While $n \log n$ edges guarantee connectedness, mathematical limits show that the graph actually transitions to being fully connected slightly earlier, typically requiring around $k = \frac{1}{2} n \log n$ edges.

## Graph Connectivity Stages

![My Image](images/image.png)

