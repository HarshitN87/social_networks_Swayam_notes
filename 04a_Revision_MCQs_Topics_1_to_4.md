# 50 Revision MCQs — Topics 1 to 4

> **How to use:** Each answer is hidden. Click **"Show Answer"** to reveal it. This file is specifically designed to help you revise Topics 1 through 4.

---

## Topic 1 — Emergence of Connectedness

---

**Q1.** In the Erdős–Rényi random graph model $G(n, p)$, a giant connected component emerges when the expected degree $np$ exceeds:

- A) $1/n$
- B) 0.5
- C) 1
- D) $\ln n$

<details><summary>Show Answer</summary>

**C) 1**

A giant component emerges when the average degree $np > 1$. This is the phase transition threshold where a single large component absorbs a constant fraction of all nodes.

</details>

---

**Q2.** For a random graph $G(n, p)$ to be fully connected (containing no isolated nodes), the probability $p$ must be at least:

- A) $1/n$
- B) $\ln n / n$
- C) $n / \ln n$
- D) $1/\ln n$

<details><summary>Show Answer</summary>

**B) $\ln n / n$**

Full connectivity requires a sharper threshold, $p \geq \ln n / n$. At this point, the probability of any isolated node existing goes to zero.

</details>

---

**Q3.** Which centrality measure is defined as the fraction of all shortest paths in a network that pass through a given node?

- A) Closeness centrality
- B) Degree centrality
- C) Betweenness centrality
- D) Eigenvector centrality

<details><summary>Show Answer</summary>

**C) Betweenness centrality**

Betweenness centrality identifies nodes that act as "bridges" or "bottlenecks" by counting the exact fraction of shortest paths between all pairs of nodes that run through them.

</details>

---

**Q4.** A node with high **closeness centrality** is characterized by:

- A) Having a large number of direct connections
- B) Being located on many shortest paths between other nodes
- C) Having a low average shortest path distance to all other nodes
- D) Being connected to other highly central nodes

<details><summary>Show Answer</summary>

**C) Having a low average shortest path distance to all other nodes**

Closeness centrality is the inverse of the sum of distances to all other nodes. High closeness means the node is globally "close" to everyone else.

</details>

---

**Q5.** Which centrality measure recursively scores a node based on the centrality of its neighbors?

- A) Degree centrality
- B) Betweenness centrality
- C) Closeness centrality
- D) Eigenvector centrality

<details><summary>Show Answer</summary>

**D) Eigenvector centrality**

Eigenvector centrality measures transitive influence: a node is important if it is connected to other important nodes.

</details>

---

**Q6.** In the Erdős–Rényi random graph, the degree distribution converges to which of the following distributions for large $n$?

- A) Power law
- B) Normal (Gaussian) distribution
- C) Uniform distribution
- D) Exponential distribution

<details><summary>Show Answer</summary>

**B) Normal (Gaussian) distribution**

In the ER model, each possible edge is an independent Bernoulli trial. By the Central Limit Theorem, the sum of these independent trials converges to a normal/bell curve distribution.

</details>

---

**Q7.** What defines a **phase transition** (or tipping point) in network science?

- A) The gradual linear increase in network density
- B) An abrupt, sudden qualitative change in network structure at a critical parameter threshold
- C) The removal of the highest-degree node
- D) When all nodes achieve the same degree

<details><summary>Show Answer</summary>

**B) An abrupt, sudden qualitative change in network structure at a critical parameter threshold**

Phase transitions describe sudden structural shifts, such as the sudden emergence of a giant component when the average degree exceeds 1.

</details>

---

**Q8.** A connected network with $N$ nodes has the absolute minimum number of edges required to stay connected. How many edges does it have?

- A) $N$
- B) $N - 1$
- C) $N \log N$
- D) $N / 2$

<details><summary>Show Answer</summary>

**B) $N - 1$**

A connected graph with the minimum number of edges is a tree, which always has exactly $N - 1$ edges.

</details>

---

**Q9.** The **diameter** of a network is defined as:

- A) The maximum degree of any node
- B) The average distance between all pairs of nodes
- C) The longest of all shortest paths between any pair of nodes
- D) The total number of nodes in the giant component

<details><summary>Show Answer</summary>

**C) The longest of all shortest paths between any pair of nodes**

The diameter represents the maximum "degrees of separation" between any two reachable nodes in the network.

</details>

---

**Q10.** When computing Breadth-First Search (BFS) to find shortest paths, nodes are explored in what order?

- A) By descending degree centrality
- B) By increasing distance (level by level) from the source node
- C) By alphabetical order of their labels
- D) Randomly

<details><summary>Show Answer</summary>

**B) By increasing distance (level by level) from the source node**

BFS explores all neighbors at distance 1, then all nodes at distance 2, and so on, guaranteeing that the path found is the shortest.

</details>

---

**Q11.** Which of the following best describes **Degree Centrality**?

- A) The sum of distances to all other nodes
- B) The number of triangles a node is part of
- C) The number of direct connections incident to a node
- D) The clustering coefficient of a node

<details><summary>Show Answer</summary>

**C) The number of direct connections incident to a node**

Degree centrality is the simplest measure: just counting the number of direct edges a node has.

</details>

---

**Q12.** If a network has multiple disconnected components, the distance between two nodes in different components is mathematically considered to be:

- A) 0
- B) 1
- C) $N$ (number of nodes)
- D) Infinity

<details><summary>Show Answer</summary>

**D) Infinity**

There is no path connecting them, so the distance is defined as infinite.

</details>

---

**Q13.** A network that perfectly captures "who knows whom" among a group of people is best represented as:

- A) A directed graph
- B) A bipartite graph
- C) An undirected graph
- D) A signed graph

<details><summary>Show Answer</summary>

**C) An undirected graph**

Friendship/knowing someone is usually modeled as a mutual (undirected) relationship, unlike Twitter follows or web links which are directed.

</details>

---

## Topic 2 — Strength of Weak Ties

---

**Q14.** Granovetter's research on job seekers surprisingly found that most people got their jobs through:

- A) Strong ties (close friends)
- B) Weak ties (acquaintances)
- C) Family members
- D) Cold calling

<details><summary>Show Answer</summary>

**B) Weak ties (acquaintances)**

Weak ties connect you to different social circles, providing access to novel information and opportunities that your close friends (who share your same information pool) don't have.

</details>

---

**Q15.** The **Strong Triadic Closure (STC)** property states that if node A has strong ties to both B and C:

- A) B and C must have a strong tie
- B) B and C must have at least a weak tie
- C) B and C cannot have a tie
- D) A's tie to either B or C will become weak

<details><summary>Show Answer</summary>

**B) B and C must have at least a weak tie**

The STC property requires that an edge (strong or weak) forms between B and C to complete the triangle.

</details>

---

**Q16.** The **clustering coefficient** of a node is defined as:

- A) The node's degree divided by the total number of nodes
- B) The number of actual edges among its neighbors divided by the maximum possible edges among them
- C) The number of triangles in the entire network
- D) The fraction of neighbors that are strong ties

<details><summary>Show Answer</summary>

**B) The number of actual edges among its neighbors divided by the maximum possible edges among them**

It measures the probability that two of a node's friends are also friends with each other.

</details>

---

**Q17.** If a node has 4 neighbors, and there are 2 edges present among those 4 neighbors, what is the node's clustering coefficient?

- A) 1/6 (approx 0.16)
- B) 1/3 (approx 0.33)
- C) 1/2 (0.50)
- D) 2/3 (approx 0.67)

<details><summary>Show Answer</summary>

**B) 1/3 (approx 0.33)**

With 4 neighbors, the maximum possible edges among them is $\binom{4}{2} = 6$. The actual number is 2. Clustering coefficient = $2/6 = 1/3$.

</details>

---

**Q18.** The **neighbourhood overlap** of an edge connecting nodes A and B is:

- A) The number of shared neighbors divided by the total unique neighbors of A and B
- B) The product of A and B's degrees
- C) The proportion of weak ties shared by A and B
- D) The number of triangles in the network

<details><summary>Show Answer</summary>

**A) The number of shared neighbors divided by the total unique neighbors of A and B**

Specifically: $\frac{|N(A) \cap N(B)|}{|N(A) \cup N(B) \setminus \{A, B\}|}$.

</details>

---

**Q19.** An edge is considered a **local bridge** if its neighbourhood overlap is exactly:

- A) 1
- B) 0.5
- C) 0
- D) $-1$

<details><summary>Show Answer</summary>

**C) 0**

Overlap is 0 when the endpoints share no common neighbors. Removing this edge would increase the shortest path between the two nodes to strictly greater than 2.

</details>

---

**Q20.** According to STC theory, why are **strong ties** almost never local bridges?

- A) Because strong ties connect nodes with very low degrees
- B) Because under STC, mutual strong ties foster common neighbors, resulting in high neighbourhood overlap
- C) Because strong ties are always negative
- D) Because bridges can only be formed in bipartite graphs

<details><summary>Show Answer</summary>

**B) Because under STC, mutual strong ties foster common neighbors, resulting in high neighbourhood overlap**

Since STC forces triangles to close, nodes connected by a strong tie will likely share multiple mutual friends, completely preventing the overlap from being zero.

</details>

---

**Q21.** Triadic closure is driven analytically by three main sociological reasons. Which of the following is NOT one of them?

- A) Increased opportunity/proximity
- B) Trust and social incentives
- C) Structural balance
- D) Random preferential attachment

<details><summary>Show Answer</summary>

**D) Random preferential attachment**

Triadic closure happens because of opportunity (meeting), trust (endorsed by a mutual friend), and structural balance (reducing psychological stress). Preferential attachment is a different concept related to hub formation.

</details>

---

**Q22.** A **global bridge** (strict bridge) is an edge whose removal:

- A) Decreases the distance between its endpoints
- B) Increases the clustering coefficient of its endpoints
- C) Disconnects the graph into two separate components
- D) Has no effect on path lengths

<details><summary>Show Answer</summary>

**C) Disconnects the graph into two separate components**

A global bridge is the *only* path between two parts of the network, meaning its removal completely shatters connectivity.

</details>

---

**Q23.** In a social network containing both strong and weak ties, which ties are structurally the most crucial for keeping distant communities connected?

- A) Strong ties
- B) Weak ties
- C) Ties with overlap = 1
- D) Ties inside densely knit cliques

<details><summary>Show Answer</summary>

**B) Weak ties**

Weak ties act as the crucial "bridges" holding different densely clustered factions together.

</details>

---

**Q24.** High neighbourhood overlap indicates that an edge is:

- A) A bridge between communities
- B) Deeply embedded within a single dense community
- C) The only path between two nodes
- D) A random long-range shortcut

<details><summary>Show Answer</summary>

**B) Deeply embedded within a single dense community**

High overlap means the two endpoints share many mutual friends, heavily characteristic of the inside of tight-knit cliques.

</details>

---

**Q25.** A node that connects multiple tight-knit groups but does not belong firmly to any of them exploits what network property?

- A) High degree centrality
- B) Strong ties
- C) High betweenness centrality via weak ties
- D) Maximum neighborhood overlap

<details><summary>Show Answer</summary>

**C) High betweenness centrality via weak ties**

These nodes act as brokers between groups; they have high betweenness centrality specifically because they manage the weak ties bridging the structural holes between communities.

</details>

---

## Topic 3 — Community Detection

---

**Q26.** The Girvan-Newman algorithm identifies communities by iteratively removing edges with the highest:

- A) Closeness centrality
- B) Edge betweenness centrality
- C) Neighbourhood overlap
- D) Modularity score

<details><summary>Show Answer</summary>

**B) Edge betweenness centrality**

The algorithm targets the structural "bottlenecks" — edges through which massive numbers of shortest paths pass. Removing these splits the network into natural communities.

</details>

---

**Q27.** Why MUST edge betweenness centrality be recalculated after *every single* edge removal in the Girvan-Newman algorithm?

- A) To increase the speed of the algorithm
- B) Because removing an edge redirects traffic (shortest paths), profoundly changing the betweenness scores of all remaining edges
- C) Because modularity requires it
- D) To prevent nodes from being deleted

<details><summary>Show Answer</summary>

**B) Because removing an edge redirects traffic (shortest paths), profoundly changing the betweenness scores of all remaining edges**

If you don't recalculate, you're using outdated traffic patterns that don't reflect the new structural reality of the degrading network.

</details>

---

**Q28.** The **modularity score ($Q$)** of a network partition compares the actual density of edges within communities to:

- A) The density of edges in a perfectly connected clique
- B) The expected density if edges were distributed entirely at random while preserving node degrees
- C) The number of triangles in the graph
- D) The max possible betweenness centrality

<details><summary>Show Answer</summary>

**B) The expected density if edges were distributed entirely at random while preserving node degrees**

Modularity asks: "Is this community structure mathematically more densely connected than pure random chance would dictate?"

</details>

---

**Q29.** In the expected edge formula used in modularity $\left(\frac{k_i k_j}{2m}\right)$, $k_i$ represents:

- A) The betweenness of node $i$
- B) The degree of node $i$
- C) The clustering coefficient of node $i$
- D) The community ID of node $i$

<details><summary>Show Answer</summary>

**B) The degree of node $i$**

The formula relies on the configuration model, which predicts random connections proportionally based on the actual degrees ($k_i$ and $k_j$) of the two nodes.

</details>

---

**Q30.** A modularity score $Q$ is generally considered indicative of strong, meaningful community structure when it is:

- A) Less than $0$
- B) Between $0.0$ and $0.1$
- C) Between $0.3$ and $0.7$
- D) Exactly $1.0$

<details><summary>Show Answer</summary>

**C) Between $0.3$ and $0.7$**

Values above ~0.3 indicate significant community structure. Max theoretical modularity is 1.0, but real-world graphs rarely approach it.

</details>

---

**Q31.** In a hierarchical dendrogram for community detection, what does cutting the dendrogram horizontally at different heights achieve?

- A) It predicts future edges
- B) It yields different valid partitions of the network with varying numbers of communities
- C) It removes the highest-degree nodes
- D) It calculates the graph's diameter

<details><summary>Show Answer</summary>

**B) It yields different valid partitions of the network with varying numbers of communities**

A dendrogram provides a nested hierarchy. A high cut gives a few large communities; a low cut gives many small, fine-grained communities.

</details>

---

**Q32.** Edge betweenness via BFS requires two passes. What does the "bottom-up" pass do?

- A) It computes the shortest path distances from the root
- B) It calculates how much credit flows up through each edge based on the number of shortest paths via that edge
- C) It calculates the modularity score
- D) It deletes the root node

<details><summary>Show Answer</summary>

**B) It calculates how much credit flows up through each edge based on the number of shortest paths via that edge**

The top-down pass builds the tree and path counts. The bottom-up pass propogates "credit" from the leaves up to the root to determine betweenness values.

</details>

---

**Q33.** If all edges in a network are contained strictly *inside* the defined communities, and zero edges exist *between* communities, what can we say about the modularity $Q$?

- A) It will be $-0.5$
- B) It will be $0$
- C) It will be significantly positive, representing very strong community structure
- D) It cannot be calculated

<details><summary>Show Answer</summary>

**C) It will be significantly positive, representing very strong community structure**

Since all actual edges are inside communities, the actual intra-community fraction ($A_{ij}$) is extremely high compared to the random expectation, yielding maximum possible modularity for that degree sequence.

</details>

---

**Q34.** What does a modularity score of exactly **zero** indicate?

- A) The graph has no edges
- B) The within-community edge density is exactly what would be expected if edges were thrown down at random
- C) The algorithm has failed
- D) Every node is in its own isolated community

<details><summary>Show Answer</summary>

**B) The within-community edge density is exactly what would be expected if edges were thrown down at random**

A score of 0 means the partition provides no better community definition than a randomized null model.

</details>

---

**Q35.** A negative modularity score ($Q < 0$) indicates that:

- A) The graph is bipartite
- B) The communities assigned have *fewer* internal edges than expected by random chance
- C) The algorithm perfectly partitioned the graph
- D) The graph is disconnected

<details><summary>Show Answer</summary>

**B) The communities assigned have fewer internal edges than expected by random chance**

Negative modularity occurs when the proposed communities are mathematically worse than random guessing — e.g., if you created communities out of nodes that deliberately avoid each other.

</details>

---

**Q36.** Which edges tend to have the **lowest** edge betweenness centrality?

- A) Edges that connect two different communities
- B) Edges that form a global bridge
- C) Edges tightly embedded deep inside a dense clique
- D) Edges attached to the highest degree node

<details><summary>Show Answer</summary>

**C) Edges tightly embedded deep inside a dense clique**

Inside a dense clique, there are many alternative shortest paths between any two nodes. Traffic is diluted across many edges, so no single edge carries a high load of shortest paths.

</details>

---

**Q37.** In the context of Girvan-Newman, after removing an edge, the number of connected components in the graph:

- A) Always increases
- B) Stays the same or increases
- C) Decreases
- D) Drops to 1

<details><summary>Show Answer</summary>

**B) Stays the same or increases**

If the removed edge was a strict bridge, the number of components increases. If the edge was part of a cycle, the graph might remain in the same number of components.

</details>

---

**Q38.** Modularity optimization algorithms often stop merging or splitting communities when:

- A) The graph becomes a single component
- B) All edges are removed
- C) The modularity score $Q$ reaches its maximum possible peak and further changes would decrease it
- D) Exactly two communities are formed

<details><summary>Show Answer</summary>

**C) The modularity score $Q$ reaches its maximum possible peak and further changes would decrease it**

Modularity serves as the objective function. The optimal partition is the layer of the dendrogram that maximizes $Q$.

</details>

---

## Topic 4 — Homophily and Social Influence

---

**Q39.** The phenomenon of "Homophily" is best translated conceptually as:

- A) Opposites attract
- B) Love of the same ("birds of a feather flock together")
- C) The rich get richer
- D) Triadic closure

<details><summary>Show Answer</summary>

**B) Love of the same ("birds of a feather flock together")**

Homophily is the universal tendency of individuals to associate and bond with similar others.

</details>

---

**Q40.** What is the key distinction between **Selection** and **Social Influence**?

- A) Selection means adopting behaviors of friends; Social Influence means choosing friends with similar behaviors
- B) Both mean the exact same thing
- C) Selection means choosing friends who are already similar; Social Influence means your behaviors change to match existing friends
- D) Selection occurs only in bipartite graphs

<details><summary>Show Answer</summary>

**C) Selection means choosing friends who are already similar; Social Influence means your behaviors change to match existing friends**

Direction of causality: Selection = Similarity causes connection. Social Influence = Connection causes similarity.

</details>

---

**Q41.** Suppose a network contains 60% Group X and 40% Group Y. If friendships form purely at random, what is the expected fraction of **cross-group edges**?

- A) $0.60 \times 0.40 = 24\%$
- B) $2 \times 0.60 \times 0.40 = 48\%$
- C) $50\%$
- D) $0.60^2 = 36\%$

<details><summary>Show Answer</summary>

**B) $2 \times 0.60 \times 0.40 = 48\%$**

With probabilities $p$ and $q$, the random chance of an edge connecting different groups is $2pq$. If the actual network has significantly *fewer* than 48% cross-group edges, it exhibits homophily.

</details>

---

**Q42.** If a researcher measures the cross-group edge ratio and finds it is drastically lower than the $2pq$ actual baseline, this is mathematical evidence for:

- A) A bipartite structure
- B) The absence of ties
- C) Strong homophily
- D) Negative modularity

<details><summary>Show Answer</summary>

**C) Strong homophily**

Fewer cross-group edges than random chance dictates that nodes are purposefully preferentially attaching to their own group.

</details>

---

**Q43.** Two people become friends because they both join the same weekly chess club. This is an example of what type of closure?

- A) Triadic closure
- B) Membership closure
- C) Focal closure
- D) Local bridge closure

<details><summary>Show Answer</summary>

**C) Focal closure**

Focal closure occurs when people connect because they share a "focus" — a physical or conceptual center of activity like a workplace, a club, or an event.

</details>

---

**Q44.** A person decides to join the weekly chess club because several of their existing friends are already members. This represents:

- A) Focal closure
- B) Triadic closure
- C) Membership closure
- D) Assortative mixing

<details><summary>Show Answer</summary>

**C) Membership closure**

Membership closure operates in the reverse direction of focal closure: the connections (friends) cause the individual to adopt the "focus" (the club).

</details>

---

**Q45.** Christakis and Fowler's famous study on the spread of obesity through social networks is fundamentally a study trying to prove the existence of:

- A) The purely genetic basis of weight gain
- B) Social influence cascading across ties
- C) Random preferential attachment
- D) Negative edge betweenness

<details><summary>Show Answer</summary>

**B) Social influence cascading across ties**

Their study demonstrated that obesity acts dynamically like a social contagion — having obese friends *influences* you to become obese, proving the "social influence" side of homophily.

</details>

---

**Q46.** In the obesity study, having an obese direct friend increased your chance of obesity by approx ~45%. Having an obese "friend of a friend" (distance 2) increased it by ~25%. This demonstrates that:

- A) Social influence only operates at a distance of 1
- B) Social influence can propagate across multiple degrees of separation, but weakens with distance
- C) Obesity is purely a selection effect
- D) Weak ties cannot transmit social influence

<details><summary>Show Answer</summary>

**B) Social influence can propagate across multiple degrees of separation, but weakens with distance**

Influence successfully cascades up to 3 degrees of separation before fading into statistical noise.

</details>

---

**Q47.** Trying to determine whether teenagers started smoking because their friends smoked (Influence) OR whether they befriended smokers because they already wanted to smoke (Selection) is fundamentally a problem of proving:

- A) Graph diameter
- B) Causality
- C) Modularity
- D) Centralization

<details><summary>Show Answer</summary>

**B) Causality**

Both mechanisms result in the same observable state (smokers being friends with smokers). Distinguishing which came first requires longitudinal data to untangle the causal direction.

</details>

---

**Q48.** If the actual fraction of cross-group edges in an equal 50/50 population is $0.50$, the network exhibits:

- A) Strong homophily
- B) Perfect heterophily (opposites attract)
- C) No homophily (pure random mixing)
- D) Impossible structure

<details><summary>Show Answer</summary>

**C) No homophily (pure random mixing)**

For a 50/50 split, $2pq = 2(0.5)(0.5) = 0.50$. Since the observed equals the expected random baseline, the network shows zero homophily.

</details>

---

**Q49.** In a social affiliation network (a bipartite graph of individuals and the groups they belong to), **Focal closure** creates an edge between:

- A) Two individuals
- B) Two groups
- C) An individual and a group
- D) Two weak ties

<details><summary>Show Answer</summary>

**A) Two individuals**

Focal closure is the formation of a direct tie between two *individuals* who previously only shared a connection to the same *group/focus*.

</details>

---

**Q50.** The fundamental mathematical test for homophily ($2pq$) relies on comparing the observable network to a theoretical:

- A) Scale-free Barabasi-Albert model
- B) Null model where edges are scrambled without regard to node attributes
- C) Perfect lattice
- D) Fully connected clique

<details><summary>Show Answer</summary>

**B) Null model where edges are scrambled without regard to node attributes**

The test strictly relies on asking "what would this look like if people ignored attributes and chose friends completely randomly?"

</details>

---
> **End of Revision MCQs** — Great job! 🎯
