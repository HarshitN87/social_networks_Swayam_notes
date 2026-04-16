# 100 MCQs — Network Science (All Topics)

> **How to use:** Each answer is hidden. Click **"Show Answer"** to reveal it.

---

## Topic 1 — Emergence of Connectedness

---

**Q1.** In the Erdős–Rényi random graph model $G(n, p)$, a giant connected component emerges when the expected degree exceeds which threshold?

- A) $\ln n$
- B) 0.5
- C) 1
- D) $n$

<details><summary>Show Answer</summary>

**C) 1**

A giant component emerges when the average degree $np > 1$. This is the phase transition threshold — below it, only small isolated clusters exist; above it, a single large component absorbs a constant fraction of all nodes.

</details>

---

**Q2.** What is the critical edge probability $p$ required for a random graph $G(n, p)$ to become **fully connected** (a single component containing all nodes) with high probability?

- A) $p = 1/n$
- B) $p = \ln n / n$
- C) $p = 1/\ln n$
- D) $p = n / \ln n$

<details><summary>Show Answer</summary>

**B) $p = \ln n / n$**

Full connectivity requires $p \geq \ln n / n$. This is a sharper threshold than the giant component threshold ($p = 1/n$). At $p = \ln n / n$, isolated nodes vanish and the graph becomes connected.

</details>

---

**Q3.** Which centrality measure identifies the node through which the most shortest paths pass?

- A) Degree centrality
- B) Closeness centrality
- C) Betweenness centrality
- D) Eigenvector centrality

<details><summary>Show Answer</summary>

**C) Betweenness centrality**

Betweenness centrality counts how many shortest paths between all pairs of nodes pass through a given node. A high value means the node acts as a critical bridge or gatekeeper.

</details>

---

**Q4.** In a random graph $G(n, p)$, the degree of each node follows approximately which distribution?

- A) Power law
- B) Uniform
- C) Exponential
- D) Normal (bell curve)

<details><summary>Show Answer</summary>

**D) Normal (bell curve)**

Each node's degree is the sum of $n-1$ independent Bernoulli trials (each with probability $p$). By the Central Limit Theorem, this sum converges to a normal distribution.

</details>

---

**Q5.** A "tipping point" in network connectivity refers to:

- A) The moment when all edges are added
- B) A sudden qualitative change in the network's structure at a critical threshold
- C) The gradual increase in average degree
- D) The removal of the highest-degree node

<details><summary>Show Answer</summary>

**B) A sudden qualitative change in the network's structure at a critical threshold**

Phase transitions (tipping points) are characterized by abrupt changes — such as the sudden emergence of a giant component — that occur at a precise critical value of $p$.

</details>

---

**Q6.** In a network, what does **degree centrality** measure?

- A) The average distance to all other nodes
- B) The number of triangles involving the node
- C) The number of direct connections a node has
- D) The fraction of shortest paths passing through the node

<details><summary>Show Answer</summary>

**C) The number of direct connections a node has**

Degree centrality is the simplest centrality measure — it counts the number of edges incident to a node. A higher degree means more direct influence.

</details>

---

## Topic 2 — Strength of Weak Ties

---

**Q7.** According to Granovetter's theory, what is the primary role of **weak ties** in a social network?

- A) They increase the clustering coefficient
- B) They provide redundant information within a group
- C) They act as bridges connecting different social clusters
- D) They strengthen trust within a community

<details><summary>Show Answer</summary>

**C) They act as bridges connecting different social clusters**

Weak ties connect individuals in different clusters, providing access to novel information and opportunities that were previously unavailable within one's own tightly-knit group.

</details>

---

**Q8.** If a strong tie between nodes A and B and between A and C exists, then the **Strong Triadic Closure (STC)** property predicts that:

- A) B and C must have a strong tie
- B) B and C must have at least a weak tie
- C) B and C cannot be connected
- D) A must be removed from the network

<details><summary>Show Answer</summary>

**B) B and C must have at least a weak tie**

The STC property states: if node A has strong ties to both B and C, then B and C must be connected by at least a weak tie. They don't need a strong tie — any edge suffices.

</details>

---

**Q9.** The **clustering coefficient** of a node measures:

- A) The node's total degree
- B) The fraction of the node's neighbors that are connected to each other
- C) The shortest path from the node to every other node
- D) The number of communities the node belongs to

<details><summary>Show Answer</summary>

**B) The fraction of the node's neighbors that are connected to each other**

The clustering coefficient quantifies how "cliquish" a node's neighborhood is. A value of 1 means all neighbors know each other; 0 means none do.

</details>

---

**Q10.** The **neighbourhood overlap** of an edge (A, B) is defined as:

- A) The degree of A plus the degree of B
- B) The number of common neighbors divided by the total number of unique neighbors (excluding A and B)
- C) The betweenness centrality of the edge
- D) The clustering coefficient of A times the clustering coefficient of B

<details><summary>Show Answer</summary>

**B) The number of common neighbors divided by the total number of unique neighbors (excluding A and B)**

Neighbourhood overlap = $|N(A) \cap N(B)| / |N(A) \cup N(B) \setminus \{A, B\}|$. Low overlap suggests the edge is a bridge; high overlap suggests embeddedness.

</details>

---

**Q11.** An edge is called a **local bridge** if:

- A) It connects two components
- B) Its endpoints share at least one common neighbor
- C) Its endpoints share **no** common neighbors (neighbourhood overlap = 0)
- D) It has the highest betweenness centrality

<details><summary>Show Answer</summary>

**C) Its endpoints share no common neighbors (neighbourhood overlap = 0)**

A local bridge is an edge whose removal would increase the distance between its endpoints. This occurs when the two endpoints have zero common neighbors (overlap = 0).

</details>

---

**Q12.** Granovetter's real-world study on job seekers found that most people obtained their jobs through:

- A) Strong ties (close friends and family)
- B) Weak ties (acquaintances)
- C) Online advertisements
- D) Random encounters

<details><summary>Show Answer</summary>

**B) Weak ties (acquaintances)**

Granovetter found that the majority of successful job referrals came through acquaintances rather than close friends, because weak ties provide access to non-redundant information from different social circles.

</details>

---

**Q13.** If a node has 5 neighbors and 4 edges exist among those neighbors, what is its clustering coefficient?

- A) 0.20
- B) 0.40
- C) 0.80
- D) 0.50

<details><summary>Show Answer</summary>

**B) 0.40**

Maximum possible edges among 5 neighbors = $\binom{5}{2} = 10$. Actual edges = 4. Clustering coefficient = $4/10 = 0.40$.

</details>

---

**Q14.** According to the Strength of Weak Ties theory, a strong tie is **unlikely** to be a bridge because:

- A) Strong ties always have high neighbourhood overlap due to triadic closure
- B) Strong ties connect nodes in different clusters
- C) Strong ties have low betweenness centrality
- D) Strong ties are rare in real networks

<details><summary>Show Answer</summary>

**A) Strong ties always have high neighbourhood overlap due to triadic closure**

The STC property forces common friends between strongly connected nodes, which means they share neighbors and the edge has high overlap — the opposite of what a bridge requires.

</details>

---

**Q15.** In the context of weak ties, removing a **bridge** from a connected graph:

- A) Increases the clustering coefficient
- B) Disconnects the graph into two components
- C) Reduces the degree of all nodes
- D) Has no structural effect

<details><summary>Show Answer</summary>

**B) Disconnects the graph into two components**

A bridge is an edge whose removal splits the graph. It is the sole path connecting two parts of the network.

</details>

---

## Topic 3 — Community Detection

---

**Q16.** The Girvan-Newman algorithm identifies communities by iteratively removing the edge with the highest:

- A) Degree centrality
- B) Weight
- C) Edge betweenness centrality
- D) Clustering coefficient

<details><summary>Show Answer</summary>

**C) Edge betweenness centrality**

Girvan-Newman computes the betweenness centrality of every edge (how many shortest paths pass through it), removes the highest one, recalculates, and repeats. Edges between communities carry many shortest paths.

</details>

---

**Q17.** What does the **modularity** score $Q$ measure in a network partition?

- A) The total number of communities
- B) The density of the network
- C) How much the within-community edge density exceeds what is expected by random chance
- D) The average shortest path length within communities

<details><summary>Show Answer</summary>

**C) How much the within-community edge density exceeds what is expected by random chance**

Modularity compares the fraction of edges within communities to the expected fraction if edges were placed at random. Higher $Q$ means the partition captures more meaningful structure.

</details>

---

**Q18.** In the Girvan-Newman algorithm, after each edge removal, what must be recalculated before the next removal?

- A) Degree centrality of all nodes
- B) The modularity score
- C) Edge betweenness centrality of all remaining edges
- D) The PageRank of every node

<details><summary>Show Answer</summary>

**C) Edge betweenness centrality of all remaining edges**

After each edge removal, the shortest path structure of the graph changes, so all edge betweenness values must be recomputed from scratch. Skipping this step can lead to incorrect community detection.

</details>

---

**Q19.** A dendrogram in community detection represents:

- A) The degree distribution of the network
- B) A hierarchical tree showing the order of edge removals and resulting community splits
- C) The PageRank values of all nodes
- D) The adjacency matrix of the network

<details><summary>Show Answer</summary>

**B) A hierarchical tree showing the order of edge removals and resulting community splits**

A dendrogram visualizes the nested hierarchy of communities that emerge as edges are progressively removed. Cutting the dendrogram at different heights gives different numbers of communities.

</details>

---

**Q20.** The modularity score $Q$ is typically in the range:

- A) 0 to 1
- B) $-1$ to $+1$
- C) $-0.5$ to $+1$
- D) 0 to $\infty$

<details><summary>Show Answer</summary>

**C) $-0.5$ to $+1$**

Modularity ranges from $-0.5$ to $1$. Values above $0.3$ are generally considered indicative of significant community structure. A negative value means the partition is worse than random.

</details>

---

**Q21.** Why does edge betweenness centrality tend to be **high** for edges that connect different communities?

- A) Because those edges are the longest in the network
- B) Because they carry many shortest paths between nodes in different communities
- C) Because they have the highest weight
- D) Because the nodes they connect have the lowest degree

<details><summary>Show Answer</summary>

**B) Because they carry many shortest paths between nodes in different communities**

Inter-community edges act as bridges — virtually all shortest paths between the two communities must pass through them, inflating their betweenness centrality.

</details>

---

**Q22.** When computing edge betweenness using BFS, what do we assign to each node in the BFS tree?

- A) Its degree centrality
- B) Its distance from the source and the number of shortest paths reaching it
- C) Its PageRank score
- D) Its clustering coefficient

<details><summary>Show Answer</summary>

**B) Its distance from the source and the number of shortest paths reaching it**

BFS from the source computes the level (distance) of each node and counts the number of shortest paths from the source to that node. These values are then used in the credit-propagation step.

</details>

---

**Q23.** In the modularity formula, the term $\frac{k_i k_j}{2m}$ represents:

- A) The actual number of edges between nodes $i$ and $j$
- B) The expected number of edges between nodes $i$ and $j$ under a random null model
- C) The clustering coefficient between $i$ and $j$
- D) The shortest path distance between $i$ and $j$

<details><summary>Show Answer</summary>

**B) The expected number of edges between nodes $i$ and $j$ under a random null model**

This term comes from the configuration model: if edges were distributed randomly preserving node degrees, the expected edges between $i$ and $j$ would be $k_i k_j / 2m$. Modularity measures how the actual network deviates from this expectation.

</details>

---

## Topic 4 — Homophily and Social Influence

---

**Q24.** Homophily in social networks refers to:

- A) The tendency for nodes to share resources equally
- B) The tendency for individuals to form connections with others who are similar to them
- C) The tendency for all nodes to have the same degree
- D) The preference for connecting to high-degree nodes

<details><summary>Show Answer</summary>

**B) The tendency for individuals to form connections with others who are similar to them**

Homophily ("love of the same") describes the well-documented phenomenon that people preferentially form friendships with those who share traits like geography, profession, ethnicity, and interests.

</details>

---

**Q25.** The key difference between **selection** and **social influence** is:

- A) Selection involves choosing friends; social influence involves changing your behavior to match your friends
- B) Selection always precedes social influence chronologically
- C) Social influence is always stronger than selection
- D) They are identical processes with different names

<details><summary>Show Answer</summary>

**A) Selection involves choosing friends; social influence involves changing your behavior to match your friends**

Selection: you choose friends who are already similar to you. Social influence: your existing friends change your behavior to become more like them. Both produce correlation in attributes among connected individuals, but through different causal mechanisms.

</details>

---

**Q26.** If the fraction of cross-group edges in a network is **significantly less** than what would be expected by random chance, this suggests:

- A) No homophily exists
- B) Strong homophily exists
- C) The network is random
- D) All nodes belong to the same group

<details><summary>Show Answer</summary>

**B) Strong homophily exists**

Fewer cross-group edges than random expectation means people preferentially connect within their own group, which is the definition of homophily. The larger the deviation from the random baseline, the stronger the homophily.

</details>

---

**Q27.** Which type of closure mechanism explains that two people become friends because they share a mutual friend?

- A) Focal closure
- B) Membership closure
- C) Triadic closure
- D) Preferential attachment

<details><summary>Show Answer</summary>

**C) Triadic closure**

Triadic closure is the process by which a mutual friend introduces two people, completing the triangle. If A knows B and B knows C, triadic closure predicts that A and C will eventually become connected.

</details>

---

**Q28.** **Focal closure** occurs when:

- A) Two people become friends through a mutual friend
- B) Two people become friends because they participate in the same activity or institution
- C) A high-degree node attracts new connections
- D) An edge is removed between two communities

<details><summary>Show Answer</summary>

**B) Two people become friends because they participate in the same activity or institution**

Focal closure is driven by shared foci (activities, organizations, workplaces) rather than by existing mutual friends. For example, joining the same club creates opportunities for new friendships.

</details>

---

**Q29.** In a network with two groups (X and Y) of equal size, if edges form uniformly at random, what fraction of edges would be cross-group edges?

- A) 25%
- B) 50%
- C) 75%
- D) 100%

<details><summary>Show Answer</summary>

**B) 50%**

With two equally sized groups and random edge formation, the probability of a cross-group edge = $2 \times 0.5 \times 0.5 = 0.50$ (50%). Observing significantly fewer cross-group edges than this indicates homophily.

</details>

---

**Q30.** Research on social influence and obesity found that having a direct friend who is obese increases your own likelihood of becoming obese by approximately:

- A) 5%
- B) 25%
- C) 45%
- D) 75%

<details><summary>Show Answer</summary>

**C) 45%**

The Christakis-Fowler study found that having a direct obese friend increases your obesity risk by ~45%, a friend-of-friend by ~25%, and a friend-of-friend-of-friend by ~12%. Social influence cascades through multiple degrees of separation.

</details>

---

## Topic 5 — Schelling Model

---

**Q31.** The Schelling segregation model demonstrates that:

- A) People must be strongly racist for segregation to emerge
- B) Even mild individual preferences for similar neighbors can produce large-scale segregation
- C) Random placement of agents always leads to integration
- D) Segregation only occurs when more than 80% of agents are intolerant

<details><summary>Show Answer</summary>

**B) Even mild individual preferences for similar neighbors can produce large-scale segregation**

Schelling's key insight is the gap between micro-motives and macro-behavior: agents with only a slight preference (e.g., wanting just 1/3 of neighbors to be similar) can produce dramatic, large-scale segregation patterns.

</details>

---

**Q32.** In the Schelling model, an agent is "satisfied" if:

- A) All of their neighbors are of the same type
- B) At least a certain threshold fraction of their neighbors are of the same type
- C) They have the maximum number of neighbors
- D) They are located at the center of the grid

<details><summary>Show Answer</summary>

**B) At least a certain threshold fraction of their neighbors are of the same type**

An agent is satisfied when the proportion of same-type neighbors meets or exceeds their personal threshold (e.g., ≥ 1/3). If unsatisfied, the agent relocates to a vacant cell.

</details>

---

**Q33.** The concept of "micro-motives vs. macro-behavior" in the Schelling model means:

- A) Individual preferences perfectly predict collective outcomes
- B) Small individual preferences aggregate into disproportionately large collective patterns
- C) Macro-level policies always override individual preferences
- D) Individual motives have no effect on group outcomes

<details><summary>Show Answer</summary>

**B) Small individual preferences aggregate into disproportionately large collective patterns**

The central lesson: mild individual tolerance thresholds produce extreme macro-level segregation. The collective outcome far exceeds what any individual intended.

</details>

---

**Q34.** In a Schelling grid, if an agent has 8 neighbors and requires at least 3 to be of the same type to be satisfied, what is their threshold?

- A) 25%
- B) 37.5%
- C) 50%
- D) 62.5%

<details><summary>Show Answer</summary>

**B) 37.5%**

Threshold = required same-type neighbors / total neighbors = $3/8 = 0.375 = 37.5\%$.

</details>

---

**Q35.** What happens in the Schelling model when the similarity threshold is set to 0 (agents are satisfied with any neighbor composition)?

- A) Complete segregation occurs
- B) Agents never move — the initial random placement is the final state
- C) All agents move to the center
- D) The grid empties out

<details><summary>Show Answer</summary>

**B) Agents never move — the initial random placement is the final state**

With a threshold of 0, every agent is satisfied regardless of who their neighbors are. No agent has any reason to relocate, so the initial random (integrated) placement persists.

</details>

---

**Q36.** A key limitation of the Schelling model is:

- A) It perfectly predicts real-world segregation patterns
- B) Agents on the grid can only interact with adjacent cells, not the entire population
- C) It considers only two types of agents
- D) Both B and C

<details><summary>Show Answer</summary>

**D) Both B and C**

The basic Schelling model uses a grid (limited neighborhood) and only two agent types. Real-world scenarios involve multiple groups, variable sizes, and non-grid geographies.

</details>

---

**Q37.** In the Schelling model, once the system reaches equilibrium:

- A) All agents are guaranteed to be satisfied
- B) The segregation level is always proportional to the threshold
- C) No unsatisfied agents remain, OR no vacant cells are available for movement
- D) Exactly half the grid is occupied by each type

<details><summary>Show Answer</summary>

**C) No unsatisfied agents remain, OR no vacant cells are available for movement**

Equilibrium is reached when no agent can or wants to move. This can happen because all agents are satisfied, or because no suitable vacant positions exist for dissatisfied agents.

</details>

---

## Topic 6 — Structural Balance

---

**Q38.** In structural balance theory, a triangle with three positive (+) edges is considered:

- A) Unbalanced
- B) Balanced — "the friend of my friend is my friend"
- C) Unstable
- D) Impossible

<details><summary>Show Answer</summary>

**B) Balanced — "the friend of my friend is my friend"**

A triangle with three positive edges represents mutual friendship among all three parties. This is inherently stable and satisfies the balance condition (an even number of negative edges = 0 or 2).

</details>

---

**Q39.** Which triangle configuration is **unbalanced** according to structural balance theory?

- A) Three positive edges (+, +, +)
- B) Two negative edges and one positive edge (+, −, −)
- C) One negative edge and two positive edges (+, +, −)
- D) Three negative edges (−, −, −)

<details><summary>Show Answer</summary>

**C) One negative edge and two positive edges (+, +, −)**

This represents "the friend of my friend is my enemy," which creates instability. Balanced triangles have an even number of negative edges (0 or 2). One negative edge (odd) is unbalanced.

</details>

---

**Q40.** A triangle with three negative edges (−, −, −) is:

- A) Balanced
- B) Unbalanced
- C) Not covered by balance theory
- D) Always stable

<details><summary>Show Answer</summary>

**B) Unbalanced**

Three negative edges means "the enemy of my enemy is my enemy" — this has an odd number of negative edges (3), violating the balance condition. It creates pressure for at least one pair to become friends.

</details>

---

**Q41.** The **Balance Theorem** states that a complete signed graph is balanced if and only if:

- A) All edges are positive
- B) The nodes can be divided into two groups such that all within-group edges are positive and all between-group edges are negative
- C) Every node has equal positive and negative edges
- D) The number of positive edges exceeds the number of negative edges

<details><summary>Show Answer</summary>

**B) The nodes can be divided into two groups such that all within-group edges are positive and all between-group edges are negative**

The Balance Theorem provides the global characterization: a balanced network is one where exactly two "factions" exist — friends within each faction, enemies between factions.

</details>

---

**Q42.** In the context of international relations, structural balance predicts that:

- A) All countries will eventually become allies
- B) Countries will organize into two opposing coalitions
- C) Neutral relationships are the most stable
- D) No stable configuration exists

<details><summary>Show Answer</summary>

**B) Countries will organize into two opposing coalitions**

By the Balance Theorem, a balanced signed network partitions into exactly two groups — mirroring phenomena like NATO vs. Warsaw Pact, where alliances and rivalries align into a bipolar structure.

</details>

---

**Q43.** A signed graph is balanced if and only if every cycle in the graph contains:

- A) An odd number of negative edges
- B) An even number of negative edges
- C) No negative edges
- D) Exactly one negative edge

<details><summary>Show Answer</summary>

**B) An even number of negative edges**

This is the cycle-based characterization of balance: every cycle (not just triangles) must contain an even number of negative edges for the entire graph to be balanced.

</details>

---

**Q44.** If you know that A is friends with B (+), and B is enemies with C (−), structural balance predicts that the relationship between A and C will be:

- A) Positive (friends)
- B) Negative (enemies)
- C) Neutral
- D) Cannot be determined

<details><summary>Show Answer</summary>

**B) Negative (enemies)**

"The friend of my enemy is my enemy" — since A is friends with B, and B is enemies with C, balance theory predicts A and C will be enemies. This produces a balanced triangle (+, −, −) with 2 negative edges.

</details>

---

## Topic 7 — PageRank and Web Graph

---

**Q45.** In the basic PageRank formula (without damping), the rank of node $v$ is computed as:

- A) The sum of the degrees of all nodes linking to $v$
- B) The sum of $PR(u) / \text{out-degree}(u)$ for all nodes $u$ linking to $v$
- C) The total number of incoming links to $v$
- D) The product of all neighbor ranks

<details><summary>Show Answer</summary>

**B) The sum of $PR(u) / \text{out-degree}(u)$ for all nodes $u$ linking to $v$**

Each node $u$ distributes its rank equally among its outgoing links. Node $v$ receives a fraction $PR(u)/|N^+(u)|$ from each in-neighbor $u$, and these contributions are summed.

</details>

---

**Q46.** A **dangling node** in PageRank is a node with:

- A) No incoming links
- B) No outgoing links
- C) Only self-loops
- D) The highest degree

<details><summary>Show Answer</summary>

**B) No outgoing links**

A dangling node has zero outgoing links. Its column in the transition matrix is all zeros, meaning it absorbs rank without redistributing it — breaking the Markov property.

</details>

---

**Q47.** The **damping factor** $d$ in PageRank (typically $d = 0.85$) represents:

- A) The probability that a random surfer follows a link on the current page
- B) The probability that a random surfer jumps to a random page
- C) The fraction of nodes that are dangling
- D) The convergence rate of the algorithm

<details><summary>Show Answer</summary>

**A) The probability that a random surfer follows a link on the current page**

With probability $d$, the surfer follows a random outgoing link; with probability $1 - d$, they "teleport" to a uniformly random page. This prevents getting stuck at dead ends.

</details>

---

**Q48.** The PageRank transition matrix $M$ is a **Markov matrix** because:

- A) All entries are positive
- B) Every column sums to exactly 1
- C) It is symmetric
- D) It has no zero entries

<details><summary>Show Answer</summary>

**B) Every column sums to exactly 1**

A (column) stochastic / Markov matrix has all column sums equal to 1. This ensures that the total rank is conserved at every iteration — no rank is created or destroyed.

</details>

---

**Q49.** PageRank converges to a unique stable vector because:

- A) The matrix is always symmetric
- B) The dominant eigenvalue of the Markov matrix is 1, and all other eigenvalues have absolute value less than 1
- C) All nodes start with equal rank
- D) The web graph is always fully connected

<details><summary>Show Answer</summary>

**B) The dominant eigenvalue of the Markov matrix is 1, and all other eigenvalues have absolute value less than 1**

The Perron-Frobenius theorem guarantees that a well-behaved Markov matrix has a unique eigenvector for eigenvalue 1. All other components decay to zero after repeated multiplication.

</details>

---

**Q50.** In a 3-node network where A→C, C→B, B→A, and B→C, the converged PageRank values are A = 0.2, B = 0.4, C = 0.4. What does this tell us?

- A) A is the most important node
- B) B and C are equally important and both more important than A
- C) All nodes are equally important
- D) The algorithm did not converge

<details><summary>Show Answer</summary>

**B) B and C are equally important and both more important than A**

A only receives from B (which splits its value), making A least important. B and C form a mutually reinforcing cycle, giving them equal and higher rank (ratio 1:2:2).

</details>

---

**Q51.** Why does the random teleportation (damping factor) fix the dangling node problem?

- A) It removes dangling nodes from the graph
- B) It ensures every node can reach every other node, maintaining valid probability flow
- C) It doubles the rank of dangling nodes
- D) It converts the directed graph to undirected

<details><summary>Show Answer</summary>

**B) It ensures every node can reach every other node, maintaining valid probability flow**

Teleportation means that from any node (including dangling ones), there's a probability $1-d$ of jumping to any random node. This restores the Markov property and guarantees convergence.

</details>

---

**Q52.** In the PageRank transition matrix, column $j$ represents:

- A) The incoming links to node $j$
- B) How node $j$ distributes its rank to nodes it links to
- C) The PageRank score of node $j$
- D) The eigenvalue associated with node $j$

<details><summary>Show Answer</summary>

**B) How node $j$ distributes its rank to nodes it links to**

Each column $j$ shows the fraction of $j$'s rank that goes to each other node. If $j$ has 3 outgoing links, each recipient gets $1/3$ in the corresponding row of column $j$.

</details>

---

## Topic 8 — Diffusion and Cascades

---

**Q53.** In a coordination game on a network, a node adopts behavior B if the fraction of its neighbors using B exceeds a threshold $q$. This is an example of:

- A) Independent cascade model
- B) Linear threshold model / deterministic cascade
- C) SIR epidemic model
- D) Random diffusion

<details><summary>Show Answer</summary>

**B) Linear threshold model / deterministic cascade**

Threshold-based adoption where a node switches when enough neighbors adopt is the hallmark of the linear threshold model, rooted in coordination game theory.

</details>

---

**Q54.** In the diffusion model with threshold $q$, a **complete cascade** (B takes over the entire network) is more likely when:

- A) $q$ is higher
- B) $q$ is lower
- C) The network has higher clustering
- D) The initial adopters are in the periphery

<details><summary>Show Answer</summary>

**B) $q$ is lower**

A lower threshold means each node needs fewer neighbors to adopt B before switching. This makes cascades easier to trigger and more likely to spread through the entire network.

</details>

---

**Q55.** According to the **Cluster Density Theorem**, a cascade of behavior B is blocked if and only if there exists a cluster of nodes all using A with internal edge density:

- A) Greater than $q$
- B) Greater than $1 - q$
- C) Equal to $q$
- D) Less than $q$

<details><summary>Show Answer</summary>

**B) Greater than $1 - q$**

A cluster blocks diffusion when its internal density exceeds $1 - q$. At that density, every node inside the cluster has enough A-using neighbors to resist switching, regardless of external influence.

</details>

---

**Q56.** In the context of cascades, who are **bilingual** or **early adopters**?

- A) Nodes that refuse to adopt any new technology
- B) Nodes that can use both the old and new behavior simultaneously, reducing the coordination cost
- C) Nodes with the highest degree
- D) Nodes in the innermost core

<details><summary>Show Answer</summary>

**B) Nodes that can use both the old and new behavior simultaneously, reducing the coordination cost**

Bilingual nodes lower the effective threshold for their neighbors by being compatible with both technologies, acting as catalysts that help cascades penetrate tightly-knit clusters.

</details>

---

**Q57.** In a direct-benefit coordination game, a node chooses behavior A or B based on which gives a higher total payoff from interactions with neighbors. If the payoff for matching on B is $b$ and on A is $a$, the threshold $q$ for adopting B is:

- A) $q = b / (a + b)$
- B) $q = a / (a + b)$
- C) $q = a / b$
- D) $q = b / a$

<details><summary>Show Answer</summary>

**B) $q = a / (a + b)$**

A node switches to B when the fraction of B-using neighbors exceeds $q = a/(a+b)$. A larger $a$ (benefit of A) makes switching harder, requiring a higher fraction of B adopters.

</details>

---

**Q58.** A cascade starting from a small group of B-adopters can be **blocked** by:

- A) Low-degree nodes in the network
- B) Tightly-knit communities with high internal density using A
- C) The existence of dangling nodes
- D) A low clustering coefficient

<details><summary>Show Answer</summary>

**B) Tightly-knit communities with high internal density using A**

Dense clusters of A-users resist switching because each member has enough A-using neighbors to exceed their threshold. The cascade bounces off the boundary of these clusters.

</details>

---

**Q59.** Financial contagion through networks differs from idea/behavior cascades because:

- A) Financial networks have no structure
- B) Financial failures can cascade through **contractual obligations** and debt linkages, not just behavioral copying
- C) Financial contagion follows the SIR model exactly
- D) Banks always act rationally

<details><summary>Show Answer</summary>

**B) Financial failures can cascade through contractual obligations and debt linkages, not just behavioral copying**

In financial contagion, a bank's failure directly impacts creditors and counterparties through contractual linkages — this is a mechanistic cascade driven by balance sheet effects, not imitation.

</details>

---

**Q60.** In a network cascade, the set of initial adopters is called the:

- A) Core
- B) Seed set
- C) K-shell
- D) Giant component

<details><summary>Show Answer</summary>

**B) Seed set**

The seed set is the initial group of nodes that adopt the new behavior. The cascade's success depends on the size, location, and connectivity of this seed set.

</details>

---

**Q61.** The key difference between a **coordination game cascade** and an **information cascade** is:

- A) Coordination games involve payoffs from matching behaviors with neighbors; information cascades involve rational inference from observed actions
- B) They are identical models
- C) Information cascades require network structure
- D) Coordination games involve no strategic thinking

<details><summary>Show Answer</summary>

**A) Coordination games involve payoffs from matching behaviors with neighbors; information cascades involve rational inference from observed actions**

In coordination games, you benefit from matching your choice with neighbors. In information cascades, you draw inferences about the "correct" choice by observing what others have chosen, potentially ignoring your own private signal.

</details>

---

## Topic 9 — HITS and Recommender Systems

---

**Q62.** In the HITS algorithm, the **hub score** of a node $v$ is computed by:

- A) Summing the hub scores of all nodes that point to $v$
- B) Summing the authority scores of all nodes that $v$ points to
- C) Counting the number of outgoing links from $v$
- D) Computing the PageRank of $v$

<details><summary>Show Answer</summary>

**B) Summing the authority scores of all nodes that $v$ points to**

Hub score = "How good are the pages you recommend?" A node's hub score is the sum of the authority scores of its out-neighbors. Hub looks **OUT**.

</details>

---

**Q63.** In the HITS algorithm, the **authority score** of a node $v$ is computed by:

- A) Summing the authority scores of all nodes that point to $v$
- B) Summing the hub scores of all nodes that point to $v$
- C) Counting the total incoming links to $v$
- D) Dividing the node's degree by the total number of nodes

<details><summary>Show Answer</summary>

**B) Summing the hub scores of all nodes that point to $v$**

Authority score = "How many good pointers endorse you?" A node's authority score is the sum of the hub scores of its in-neighbors. Authority looks **IN**.

</details>

---

**Q64.** A user on a social platform is followed by two hubs with hub scores of 3 and 5. What is the user's authority score (before normalization)?

- A) 2
- B) 8
- C) 15
- D) 1.5

<details><summary>Show Answer</summary>

**B) 8**

Authority score = sum of hub scores of all in-neighbors = $3 + 5 = 8$.

</details>

---

**Q65.** HITS is more suitable than PageRank for:

- A) Ranking the entire web globally
- B) Topic-specific or focused queries on a small subgraph
- C) Handling dangling nodes
- D) Large-scale stable ranking systems

<details><summary>Show Answer</summary>

**B) Topic-specific or focused queries on a small subgraph**

HITS builds a focused subgraph per query and computes hub/authority within it. This makes it ideal for topic-specific ranking but unstable for global ranking (where PageRank excels).

</details>

---

**Q66.** Why does HITS perform poorly on large graphs?

- A) It cannot handle directed edges
- B) It is sensitive to irrelevant parts of the graph AND it lacks a global notion of importance
- C) It always gives all nodes equal scores
- D) It requires a damping factor that doesn't exist

<details><summary>Show Answer</summary>

**B) It is sensitive to irrelevant parts of the graph AND it lacks a global notion of importance**

Both factors contribute: (1) irrelevant nodes in a large graph pollute hub/authority computations, and (2) HITS has no mechanism to assess global importance — it relies entirely on the subgraph provided.

</details>

---

**Q67.** In a bipartite recommender system, **normalization** is performed after each update to:

- A) Remove low-scoring nodes
- B) Prevent scores from growing unboundedly so relative proportions are preserved
- C) Convert directed edges to undirected
- D) Ensure every node has the same score

<details><summary>Show Answer</summary>

**B) Prevent scores from growing unboundedly so relative proportions are preserved**

Without normalization, each iteration would multiply scores, causing them to grow to infinity. Normalization scales them so they sum to 1 within each group, preserving meaningful proportions.

</details>

---

**Q68.** Which of the following is a key difference between HITS and PageRank?

- A) HITS gives each node one score; PageRank gives two
- B) PageRank gives each node one score; HITS gives each node two scores (hub and authority)
- C) HITS uses a damping factor; PageRank does not
- D) PageRank requires a bipartite graph

<details><summary>Show Answer</summary>

**B) PageRank gives each node one score; HITS gives each node two scores (hub and authority)**

PageRank computes a single importance score per node. HITS computes two scores per node — a hub score (how good a pointer it is) and an authority score (how good a destination it is).

</details>

---

**Q69.** In HITS, it is important to update hub and authority scores using values from the **previous** round, not mid-round updates. Why?

- A) It makes computation faster
- B) Mixing current and previous values produces incorrect converged results
- C) It reduces the number of iterations needed
- D) It avoids negative scores

<details><summary>Show Answer</summary>

**B) Mixing current and previous values produces incorrect converged results**

Like Jacobi iteration in linear algebra, HITS requires all updates in a round to be computed from the same snapshot of scores. Using partially updated values introduces order-dependent bias.

</details>

---

## Topic 10 — Power Law and Preferential Attachment

---

**Q70.** A power law degree distribution is characterized by:

- A) A symmetric bell curve centered at the average degree
- B) Most nodes having very few connections and a few nodes having extremely many connections
- C) All nodes having exactly the same degree
- D) An exponential decay in the number of high-degree nodes

<details><summary>Show Answer</summary>

**B) Most nodes having very few connections and a few nodes having extremely many connections**

Power law: $P(k) \propto 1/k^\alpha$. This creates a sharp peak at low degrees and a long tail extending to very high degrees — generating massive "hub" nodes.

</details>

---

**Q71.** How do you visually confirm that a degree distribution follows a power law?

- A) Plot it on a linear scale and look for a bell curve
- B) Plot it on a log-log scale and look for a straight line
- C) Compute the average degree
- D) Count the number of triangles

<details><summary>Show Answer</summary>

**B) Plot it on a log-log scale and look for a straight line**

Taking $\log$ of both sides of $P(k) = 1/k^\alpha$ gives $\log P(k) = -\alpha \log k$, a straight line with slope $-\alpha$ on a log-log plot.

</details>

---

**Q72.** In the Barabási–Albert preferential attachment model, the probability that a new node connects to an existing node $i$ is:

- A) $1/n$ (equal for all nodes)
- B) $k_i / \sum_j k_j$ (proportional to $i$'s current degree)
- C) $1/k_i$ (inversely proportional to degree)
- D) A fixed constant regardless of the network state

<details><summary>Show Answer</summary>

**B) $k_i / \sum_j k_j$ (proportional to $i$'s current degree)**

This is the "rich get richer" rule: nodes with more connections attract even more new connections, with probability exactly proportional to their current degree.

</details>

---

**Q73.** A network has 8 users with degrees A=4, B=3, C=5, D=3, E=3, F=4, G=3, H=3. A new user I joins. What is the probability that I connects to C?

- A) $5/8 = 0.625$
- B) $5/28 \approx 0.179$
- C) $1/8 = 0.125$
- D) $3/28 \approx 0.107$

<details><summary>Show Answer</summary>

**B) $5/28 \approx 0.179$**

Total degree sum = $4+3+5+3+3+4+3+3 = 28$. $P(\text{I} \to \text{C}) = k_C / \sum k_j = 5/28 \approx 0.179$. Note: the denominator is the total degree sum, NOT the number of nodes.

</details>

---

**Q74.** The Central Limit Theorem (CLT) applies to the Erdős–Rényi model but NOT to the Barabási–Albert model because:

- A) The Barabási–Albert model has too few nodes
- B) Edge formation in Barabási–Albert is **not** independent — each new edge depends on the current degree distribution
- C) The CLT only works for continuous distributions
- D) The Barabási–Albert model has no edges

<details><summary>Show Answer</summary>

**B) Edge formation in Barabási–Albert is not independent — each new edge depends on the current degree distribution**

The CLT requires independence of the random variables being summed. In preferential attachment, each new edge decision depends on the entire history of the network, violating independence.

</details>

---

**Q75.** In the BA model with $m_0 = 5$ initial nodes (fully connected) and $m = 3$ edges per new node, after adding 15 new nodes, the total number of edges is:

- A) 45
- B) 55
- C) 60
- D) 50

<details><summary>Show Answer</summary>

**B) 55**

Initial edges = $m_0(m_0-1)/2 = 5 \times 4/2 = 10$. New edges = $15 \times 3 = 45$. Total = $10 + 45 = 55$.

</details>

---

**Q76.** A scale-free (power law) network under **random failure** is:

- A) Extremely fragile — a few random removals destroy the network
- B) Highly robust — random removals almost always hit low-degree nodes, leaving hubs intact
- C) Equally vulnerable to random and targeted removals
- D) Completely immune to any failure

<details><summary>Show Answer</summary>

**B) Highly robust — random removals almost always hit low-degree nodes, leaving hubs intact**

Most nodes in a power law network have low degree. Random failure is very likely to hit these unimportant nodes, leaving the critical hubs unchanged and the network connected.

</details>

---

**Q77.** A scale-free network under **targeted attack** (removing highest-degree nodes first) is:

- A) Highly robust
- B) Moderately affected
- C) Extremely fragile — removing just the top few hubs can disconnect the entire network
- D) Unaffected because other nodes compensate

<details><summary>Show Answer</summary>

**C) Extremely fragile — removing just the top few hubs can disconnect the entire network**

Hubs are the structural backbone. Removing a handful of them disconnects the vast majority of low-degree nodes that depended on the hubs for connectivity.

</details>

---

**Q78.** Which of the following phenomena does **NOT** exhibit a power law distribution?

- A) Incoming hyperlinks on the WWW
- B) Heights of adult humans
- C) Number of downloads of songs
- D) Duration of telephone conversations

<details><summary>Show Answer</summary>

**B) Heights of adult humans**

Heights follow a normal (bell curve) distribution because height = sum of many independent genetic and environmental factors → CLT applies. All other options exhibit power law behavior.

</details>

---

## Topic 11 — Epidemics, Rich Get Richer, and the Long Tail

---

**Q79.** The Basic Reproductive Number $R_0$ is defined as:

- A) $R_0 = p + k$
- B) $R_0 = p \times k$
- C) $R_0 = p / k$
- D) $R_0 = k / p$

<details><summary>Show Answer</summary>

**B) $R_0 = p \times k$**

$R_0$ = probability of transmission per contact ($p$) × number of contacts ($k$). It represents the expected number of secondary infections from a single infected individual.

</details>

---

**Q80.** If $R_0 > 1$, which of the following is TRUE?

- A) The disease will certainly persist indefinitely
- B) The disease will persist with **positive probability**, but not with certainty
- C) The disease will certainly die out
- D) The disease will infect exactly $R_0$ people

<details><summary>Show Answer</summary>

**B) The disease will persist with positive probability, but not with certainty**

$R_0 > 1$ means the disease *can* become an epidemic, but all initial transmissions could still fail by random chance. Only $R_0 < 1$ guarantees extinction with certainty.

</details>

---

**Q81.** In the SIR model, the key property that distinguishes it from SIS is:

- A) Infected nodes can transmit the disease
- B) Recovered nodes gain **permanent immunity** and can never be reinfected
- C) The disease spreads through networks
- D) The model uses probability-based transmission

<details><summary>Show Answer</summary>

**B) Recovered nodes gain permanent immunity and can never be reinfected**

SIR: S → I → R (permanent immunity). SIS: S → I → S → I → ... (reinfection possible). The existence of the permanent "R" state is what defines SIR.

</details>

---

**Q82.** Measles follows the SIR model (not SIS) because:

- A) It has a high transmission probability $p$
- B) The infectious period $T_I$ is 8 days
- C) Infection confers **lifelong immunity** after recovery
- D) It spreads through hierarchical networks

<details><summary>Show Answer</summary>

**C) Infection confers lifelong immunity after recovery**

The SIR model applies specifically because recovered individuals become permanently immune. This has nothing to do with $p$, $T_I$, or network structure.

</details>

---

**Q83.** If $p = 0.25$ and $k = 12$, what is the expected number of infections at the **third** transmission generation?

- A) 3.0
- B) 9.0
- C) 27.0
- D) 1,260

<details><summary>Show Answer</summary>

**C) 27.0**

$R_0 = 0.25 \times 12 = 3.0$. Expected infections at level 3 = $R_0^3 = 3.0^3 = 27.0$.

</details>

---

**Q84.** The "20% of infected individuals causing 80% of transmissions" is an example of:

- A) Normal distribution
- B) Uniform probability
- C) Zipf's Law / power law pattern
- D) The SIR equilibrium condition

<details><summary>Show Answer</summary>

**C) Zipf's Law / power law pattern**

This extreme concentration — a small fraction producing the vast majority of output — is the hallmark of Zipf's Law and the power law distribution.

</details>

---

**Q85.** In the **percolation model** of epidemic spread, what does a "receptive channel" between two nodes mean?

- A) The disease is guaranteed to reach both nodes
- B) That specific edge **can** transmit the pathogen, but transmission requires a complete path of open edges from the source
- C) Both nodes are already infected
- D) The edge has been removed from the network

<details><summary>Show Answer</summary>

**B) That specific edge can transmit the pathogen, but transmission requires a complete path of open edges from the source**

A receptive (open) edge means the connection allows transmission. But the disease only reaches a node if **every edge** on the path from the source is open — a single open edge alone guarantees nothing.

</details>

---

**Q86.** In the Long Tail economics, approximately what fraction of total revenue comes from niche products (the "tail")?

- A) 10%
- B) 20%
- C) 50%
- D) 80%

<details><summary>Show Answer</summary>

**D) 80%**

The Long Tail principle shows that while top products have high individual sales, the aggregation of all niche products in the tail accounts for approximately 80% of total transactions.

</details>

---

**Q87.** In the music experiment that demonstrated the Rich Get Richer effect, what was the key finding?

- A) The best songs always won regardless of conditions
- B) When download counts were visible, different songs became "hits" in different experimental worlds due to early random variance
- C) Users always preferred the same genre
- D) Download counts had no effect on future downloads

<details><summary>Show Answer</summary>

**B) When download counts were visible, different songs became "hits" in different experimental worlds due to early random variance**

With visible popularity metrics, early random advantages snowballed via the feedback loop. Different portals produced completely different winners, proving that popularity was driven by initial luck, not intrinsic quality.

</details>

---

## Topic 12 — Small World Effect

---

**Q88.** Milgram's 1967 experiment demonstrated that:

- A) Social networks are random graphs
- B) Any two people in the US can be connected by approximately **6 intermediaries**, and ordinary people can find these short chains using local decisions
- C) Social networks have no clustering
- D) Weak ties do not exist in real networks

<details><summary>Show Answer</summary>

**B) Any two people in the US can be connected by approximately 6 intermediaries, and ordinary people can find these short chains using local decisions**

Milgram proved both the **existence** of short paths and the ability of people to **discover** them using only local knowledge of their contacts.

</details>

---

**Q89.** In the Watts-Strogatz model, what fraction of edges need to be randomly rewired to produce a small-world network (short paths + high clustering)?

- A) At least 50%
- B) At least 25%
- C) As little as ~1%
- D) Exactly 100%

<details><summary>Show Answer</summary>

**C) As little as ~1%**

The critical insight: even a tiny rewiring probability (~1%) creates enough long-range shortcuts to drastically reduce average path length while preserving the high clustering of the original regular lattice.

</details>

---

**Q90.** In Kleinberg's model on a 2D grid, the optimal distance exponent $k$ for greedy decentralized search is:

- A) $k = 0$
- B) $k = 1$
- C) $k = 2$
- D) $k = 4$

<details><summary>Show Answer</summary>

**C) $k = 2$**

Kleinberg proved that the optimal exponent $k$ equals the dimension $d$ of the grid. For a 2D grid, $k = 2$ creates a hierarchy of links at every distance scale, enabling greedy search in $O(\log^2 n)$ steps.

</details>

---

**Q91.** The critical distinction between "short paths exist" and "short paths are discoverable" was established by:

- A) Watts and Strogatz
- B) Milgram
- C) Kleinberg
- D) Erdős and Rényi

<details><summary>Show Answer</summary>

**C) Kleinberg**

Watts-Strogatz proved short paths exist (structural property). Kleinberg proved when those paths can be found by greedy local search (algorithmic property). A small-world network is NOT automatically searchable.

</details>

---

**Q92.** If a request passes through **6 intermediaries** before reaching the target, how many people were involved in the chain (including sender and receiver)?

- A) 6
- B) 7
- C) 8
- D) 5

<details><summary>Show Answer</summary>

**C) 8**

Chain = Sender + 6 intermediaries + Receiver = 8 total people. The sender and receiver are not counted as intermediaries.

</details>

---

**Q93.** In Kleinberg's model, when $k = 0$ (uniformly random long-range links), greedy search fails because:

- A) No short paths exist
- B) Random shortcuts provide no consistent "sense of direction" toward the target
- C) The network is disconnected
- D) All nodes have the same degree

<details><summary>Show Answer</summary>

**B) Random shortcuts provide no consistent "sense of direction" toward the target**

With $k=0$, long-range links jump to arbitrary locations. Each jump may land you farther from the target. Local greedy decisions can't systematically reduce distance because the links carry no distance information.

</details>

---

**Q94.** The Watts-Strogatz model proves:

- A) That greedy search is always efficient
- B) That short paths and high clustering can **coexist** through a small amount of random rewiring
- C) That all social networks have diameter 6
- D) That Kleinberg's exponent must be $k = 2$

<details><summary>Show Answer</summary>

**B) That short paths and high clustering can coexist through a small amount of random rewiring**

Watts-Strogatz addressed the seeming contradiction that real networks are both highly clustered (like lattices) and have short paths (like random graphs). Minimal rewiring achieves both simultaneously.

</details>

---

## Topic 13 — Viral Diffusion and Influence Maximization

---

**Q95.** A **K-core** of a graph is defined as:

- A) A clique of size $K$
- B) A maximal subgraph where every node has degree at least $K$
- C) The set of $K$ highest-degree nodes
- D) A tree with $K$ levels

<details><summary>Show Answer</summary>

**B) A maximal subgraph where every node has degree at least $K$**

A K-core requires every node within it to have $\geq K$ connections to other nodes also in the K-core. This is much weaker than a clique (which requires ALL pairs connected).

</details>

---

**Q96.** What is the difference between a **K-shell** and a **K-core**?

- A) They are the same thing
- B) The K-shell = nodes removed at iteration $K$; the K-core = the K-shell **plus all deeper shells**
- C) The K-core is a subset of the K-shell
- D) The K-shell contains all nodes in the graph

<details><summary>Show Answer</summary>

**B) The K-shell = nodes removed at iteration $K$; the K-core = the K-shell plus all deeper shells**

K-shell (bucket $B_K$) = only the nodes removed at step $K$. K-core = $B_K \cup B_{K+1} \cup \cdots \cup B_{\max}$ = all nodes surviving at least to iteration $K$.

</details>

---

**Q97.** A node has degree 500 but all 500 of its neighbors have degree 1. What is its coreness?

- A) 500
- B) 250
- C) 1
- D) 0

<details><summary>Show Answer</summary>

**C) 1**

In K-shell decomposition ($k=1$): all 500 neighbors have degree 1, so they are removed first. This drops the hub's degree to 0, so it too is removed at $k=1$. Despite massive degree, coreness = 1 (star topology trap).

</details>

---

**Q98.** **Pseudo-core** nodes are preferred over absolute core nodes for marketing campaigns because:

- A) They always have higher degrees
- B) They achieve **near-core-level cascade capacity** at significantly lower cost and greater accessibility
- C) They are located in the periphery
- D) They have the lowest coreness values

<details><summary>Show Answer</summary>

**B) They achieve near-core-level cascade capacity at significantly lower cost and greater accessibility**

Pseudo-core nodes sit in intermediate shells where cascade capacity plateaus near the core's level. They are more numerous, more reachable, and cheaper to engage than celebrities in the absolute innermost core.

</details>

---

**Q99.** In the **independent cascade model**, the simulation terminates when:

- A) All core users have adopted
- B) All users in the network have been exposed
- C) **No new users adopt** in an iteration
- D) Peripheral users reject the product

<details><summary>Show Answer</summary>

**C) No new users adopt in an iteration**

The termination condition is precise: when a round produces zero new activations, the cascade has reached its final state. This is NOT about exposure, rejection, or core adoption.

</details>

---

**Q100.** Why can targeting only high-degree nodes fail as a seeding strategy?

- A) High-degree nodes always guarantee large cascades
- B) Their audiences may **overlap significantly**, creating redundant exposure rather than expanded reach, and they may be structurally peripheral
- C) High-degree nodes cannot spread information
- D) All high-degree nodes are in the innermost core

<details><summary>Show Answer</summary>

**B) Their audiences may overlap significantly, creating redundant exposure rather than expanded reach, and they may be structurally peripheral**

Degree is a purely local measure. A high-degree node's connections might all point to the same community (overlapping audiences) or to low-degree leaves (star topology). Coreness, not degree, captures structural depth.

</details>

---

> **End of 100 MCQs** — Good luck with your exam! 🎯
