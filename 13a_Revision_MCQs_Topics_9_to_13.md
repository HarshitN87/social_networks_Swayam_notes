# 50 Revision MCQs — Topics 9 to 13

> **How to use:** Each answer is hidden. Click **"Show Answer"** to reveal it. This file is designed specifically for revising Topics 9 through 13.

---

## Topic 9 — HITS and Recommender Systems

---

**Q1.** The fundamental premise of the HITS algorithm evaluates nodes on two distinct properties. What are they?

- A) In-degree and Out-degree
- B) Closeness and Betweenness
- C) Hubs and Authorities
- D) Modularity and Centrality

<details><summary>Show Answer</summary>

**C) Hubs and Authorities**

HITS assigns two scores to every node: a Hub score (evaluating the quality of its outgoing links) and an Authority score (evaluating the quality of its incoming links).

</details>

---

**Q2.** An excellent **Authority** in a network is mathematically defined as a node that:

- A) Points to many high-quality hubs
- B) Has an extremely high out-degree
- C) Is pointed to by many high-quality hubs
- D) Belongs to multiple communities

<details><summary>Show Answer</summary>

**C) Is pointed to by many high-quality hubs**

Authorities represent high-quality information sources. They earn high Authority scores when endorsed (linked to) by nodes that are recognized as good Hubs.

</details>

---

**Q3.** An excellent **Hub** is mathematically defined as a node that:

- A) Points to many high-quality authorities
- B) Is pointed to by many high-quality authorities
- C) Has the highest degree in the network
- D) Is surrounded by negative edges

<details><summary>Show Answer</summary>

**A) Points to many high-quality authorities**

Hubs serve as excellent directories or curators. They earn high Hub scores by pointing outward to recognized Authorities.

</details>

---

**Q4.** A major functional difference between PageRank and HITS is that HITS is typically computed on:

- A) The entire global network
- B) A small, dynamically generated subgraph localized around a specific search query
- C) Undirected social networks
- D) Randomly generated graphs

<details><summary>Show Answer</summary>

**B) A small, dynamically generated subgraph localized around a specific search query**

Unlike PageRank (which computes a static global score for the whole web), HITS is query-dependent. It first fetches a root set of relevant pages, expands to a base set, and computes its scores only within that subset.

</details>

---

**Q5.** In the update rules for HITS, it is absolutely critical to:

- A) Normalize both scores after each update step entirely
- B) Only update Hub scores and rarely update Authority scores
- C) Teleport out of dangling nodes
- D) Use only integer scores

<details><summary>Show Answer</summary>

**A) Normalize both scores after each update step entirely**

Because Hubs and Authorities mutually reinforce each other, the raw scores violently explode toward infinity if not normalized tightly at the end of each iteration.

</details>

---

**Q6.** When computationally updating HITS in a single sweep, why must you use values strictly from the *previous* round?

- A) It prevents integer overflow
- B) It reduces the algorithm to linear time
- C) Mixing old and newly-computed mid-round values biases the results based on the arbitrary order nodes are processed
- D) It forces the graph to be bipartite

<details><summary>Show Answer</summary>

**C) Mixing old and newly-computed mid-round values biases the results based on the arbitrary order nodes are processed**

Like Jacobi iteration, all updates for time $t$ must exclusively use the state of the network at time $t-1$ to ensure fair, symmetric calculation.

</details>

---

**Q7.** In bipartite Recommender Systems (e.g., Users and Products), how does the logic mirror HITS?

- A) Both completely ignore user behavior
- B) Users act like Hubs (pointing to items), and Products act like Authorities (pointed to by users)
- C) It calculates PageRank on the users
- D) Products point to other Products

<details><summary>Show Answer</summary>

**B) Users act like Hubs (pointing to items), and Products act like Authorities (pointed to by users)**

The bipartite math is identical. A good User (hub) buys highly-rated Products (authorities), and a good Product is bought by discerning Users.

</details>

---

**Q8.** A significant weakness of HITS when tested on large, loosely defined graphs is that:

- A) The algorithm never converges mathematically
- B) It requires a damping factor
- C) It is highly sensitive to irrelevant, dense clusters that happen to get scooped into the subgraph
- D) It only supports undirected edges

<details><summary>Show Answer</summary>

**C) It is highly sensitive to irrelevant, dense clusters that happen to get scooped into the subgraph**

Without a global sense of page quality to anchor it, HITS can easily be hijacked by a tightly-knit, irrelevant community within the extracted base set.

</details>

---

**Q9.** For a user who buys item A and item B, Collaborative Filtering directly calculates similarities between:

- A) The hub scores of all users
- B) Items, based on how frequently identical sets of users purchase them both
- C) Shortest path distances
- D) The eigenvalues of the items

<details><summary>Show Answer</summary>

**B) Items, based on how frequently identical sets of users purchase them both**

Item-Item collaborative filtering looks at overlap in the bipartite graph: if the set of buyers for A heavily overlaps the buyers for B, A and B are deemed similar.

</details>

---

**Q10.** Node X points to Y and Z. Y has Authority 10; Z has Authority 20. Before normalization, what is X's new Hub score?

- A) 10
- B) 15
- C) 30
- D) 200

<details><summary>Show Answer</summary>

**C) 30**

A node's Hub score is simply the sum of the Authority scores of all the nodes it directly points to ($10 + 20 = 30$).

</details>

---

## Topic 10 — Power Law and Preferential Attachment

---

**Q11.** The defining visual characteristic of a Power Law distribution on a log-log plot is:

- A) A symmetric bell curve
- B) A flat horizontal line
- C) A downward-sloping straight diagonal line
- D) Multiple erratic spikes

<details><summary>Show Answer</summary>

**C) A downward-sloping straight diagonal line**

Because $\log(P(k)) = \log(ck^{-\alpha}) = \log(c) - \alpha \log(k)$. This is a linear equation $y = mx + b$ where the slope is $-\alpha$.

</details>

---

**Q12.** What does it mean for a network to be "scale-free"?

- A) The network has no defined nodes
- B) The degree distribution follows a power law, meaning it lacks a single characteristic "scale" (average degree) that meaningfully represents most nodes
- C) All nodes have scaled weights
- D) The network is perfectly balanced

<details><summary>Show Answer</summary>

**B) The degree distribution follows a power law, meaning it lacks a single characteristic "scale" (average degree) that meaningfully represents most nodes**

Unlike human heights where the average (roughly 5'7") is highly representative, a power law "average" is heavily skewed by extreme mega-hubs and represents virtually nobody in the network.

</details>

---

**Q13.** In the Barabási-Albert (BA) model, the fundamental mechanism driving the network structure is:

- A) Triadic closure
- B) Preferential attachment ("the rich get richer")
- C) Assortative mixing
- D) The linear threshold model

<details><summary>Show Answer</summary>

**B) Preferential attachment ("the rich get richer")**

New nodes preferentially connect to existing nodes with a probability exactly strictly proportional to the existing nodes' current degrees. High-degree nodes attract new edges far faster than low-degree nodes.

</details>

---

**Q14.** In the BA model, if node $i$ has degree 10 and the sum of all degrees in the entire network is 100, the probability a new incoming node connects to $i$ is:

- A) 10%
- B) 1%
- C) 5%
- D) 90%

<details><summary>Show Answer</summary>

**A) 10%**

Probability = $k_i / \sum k_j = 10 / 100 = 0.10$ (10%).

</details>

---

**Q15.** Why does the Central Limit Theorem (CLT) fail to predict the degree distribution of the BA model?

- A) The graph is undirected
- B) The BA model adds nodes in continuously growing numbers
- C) Edge creation is heavily inter-dependent (a node's chance of getting an edge today depends entirely on what happened yesterday), violating the independence assumption of the CLT
- D) The probability of connection is uniform

<details><summary>Show Answer</summary>

**C) Edge creation is heavily inter-dependent, violating the independence assumption of the CLT**

The CLT only applies to the sum of *independent* random variables (like the random Erdős-Rényi model). Preferential attachment is deeply history-dependent.

</details>

---

**Q16.** Power law networks display extreme robustness against **random failures** because:

- A) Their edges are indestructible
- B) The overwhelming majority of nodes have tiny degrees; random strikes almost certainly hit these periphery nodes, leaving the core hubs intact and the network connected
- C) All nodes have the exact same degree
- D) The network is heavily centralized

<details><summary>Show Answer</summary>

**B) The overwhelming majority of nodes have tiny degrees; random strikes almost certainly hit these periphery nodes**

Since ~80%+ of nodes are 1-degree or 2-degree leaves, shooting randomly will likely only sever a leaf, preserving the giant component.

</details>

---

**Q17.** Conversely, power law networks are extremely fragile against **targeted attacks** because:

- A) Taking down the handful of massive hubs instantly shatters the network into thousands of disconnected fragments
- B) Targeted attacks use viruses
- C) Removing leaves breaks the core
- D) Targeting randomizes the network

<details><summary>Show Answer</summary>

**A) Taking down the handful of massive hubs instantly shatters the network into thousands of disconnected fragments**

The entire structural integrity of a scale-free network hangs on a trivial percentage of massive nodes (hubs). Target those directly, and the entire system collapses immediately.

</details>

---

**Q18.** Which of the following is commonly NOT modeled as a power law distribution?

- A) City populations
- B) Net worth of individuals
- C) Scores on a standardized high school math test
- D) The frequency of words in a language (Zipf's Law)

<details><summary>Show Answer</summary>

**C) Scores on a standardized high school math test**

Test scores, like human heights and blood pressures, are driven by many independent additive factors, and thus form a normal (Gaussian/bell-curve) distribution, not a power law.

</details>

---

**Q19.** In the BA model setup, what role do the parameters $m_0$ and $m$ play?

- A) $m_0$ is the final limit of nodes; $m$ is the initial edges
- B) $m_0$ is a small initial connected core of nodes; $m$ is the number of edges each new incoming node brings with it
- C) They represent the thresholds for diffusion
- D) They represent community indices

<details><summary>Show Answer</summary>

**B) $m_0$ is a small initial connected core of nodes; $m$ is the number of edges each new incoming node brings with it**

The simulation starts with $m_0$ nodes. Every time a new node joins, it throws exactly $m$ edges into the network to attach to existing nodes.

</details>

---

**Q20.** A network where nodes gain edges randomly without regard to existing degrees is called:

- A) Erdős-Rényi (Random) graph
- B) Barabási-Albert graph
- C) Scale-free graph
- D) Bipartite graph

<details><summary>Show Answer</summary>

**A) Erdős-Rényi (Random) graph**

In ER graphs, new edges form with an equal independent probability $p$ everywhere, completely ignoring "rich get richer" dynamics, which creates a normal distribution rather than a power law.

</details>

---

## Topic 11 — Epidemics, Rich Get Richer, and Long Tail

---

**Q21.** In epidemic modeling, the Basic Reproductive Number, $R_0$, is formally defined as:

- A) The number of people who die
- B) The probability of transmission $p$ multiplied by the average number of network contacts $k$ per infected individual
- C) The total degree of the network
- D) The diameter of the graph

<details><summary>Show Answer</summary>

**B) The probability of transmission $p$ multiplied by the average number of network contacts $k$ per infected individual**

$R_0 = p \times k$. It gives the expected number of new infections directly caused by one infected individual in a susceptible population.

</details>

---

**Q22.** A terrifying but critical mathematical truth of epidemics is that if $R_0 > 1$:

- A) Everyone will definitely get sick
- B) The epidemic will spread with 100% certainty
- C) The epidemic has a positive (non-zero) mathematical probability of persisting, but early random luck could still cause it to die out
- D) The disease mutates to R0 < 1 automatically

<details><summary>Show Answer</summary>

**C) The epidemic has a positive (non-zero) mathematical probability of persisting, but early random luck could still cause it to die out**

$R_0 > 1$ guarantees a *chance* of an epidemic branch continuing indefinitely (like tossing a biased coin). Only $R_0 < 1$ guarantees mathematical *certainty* that it will die out.

</details>

---

**Q23.** What is the architectural difference that forces us to use the **SIR model** instead of the SIS model?

- A) The disease spreads rapidly
- B) Pathogens mutate
- C) Recovered individuals acquire lifelong, permanent immunity and can no longer be infected nor transmit the disease
- D) The disease uses probability $p$

<details><summary>Show Answer</summary>

**C) Recovered individuals acquire lifelong, permanent immunity and can no longer be infected nor transmit the disease**

SIR (Susceptible-Infected-Recovered) has an absorbing state (R). SIS (Susceptible-Infected-Susceptible) assumes no immunity against reinfection (e.g., the common cold).

</details>

---

**Q24.** Using a branching process model, if an individual infects $R_0$ people, what is the expected number of infections at transmission level $i$?

- A) $i \times R_0$
- B) $R_0^i$
- C) $R_0 + i$
- D) The network diameter

<details><summary>Show Answer</summary>

**B) $R_0^i$**

Assuming a pure branching tree without cycles, Level 1 = $R_0$, Level 2 = $R_0 \times R_0$, Level 3 = $R_0^3$, etc.

</details>

---

**Q25.** Salganik's famous "Music Lab" experiment involving artificial song ranking portals brilliantly demonstrated that:

- A) Better songs always rise to the top regardless of UI
- B) When users can see which songs are popular, early arbitrary randomness violently compounds (via Rich-Get-Richer), causing totally different songs to become huge hits in different alternate-reality worlds
- C) Users hate popular songs
- D) Music taste is genetically coded

<details><summary>Show Answer</summary>

**B) When users can see which songs are popular, early arbitrary randomness violently compounds, causing totally different songs to become huge hits in different alternate-reality worlds**

This proved that success is highly sensitive to initial random conditions and feedback loops, entirely separating "objective quality" from "final popularity."

</details>

---

**Q26.** The "Long Tail" economic phenomenon generated by the internet describes markets where:

- A) The top 10% of items generate 100% of revenue
- B) Huge individual sales of massive blockbusters are roughly equaled or eclipsed by the aggregated sales of millions of highly niche items
- C) Sales randomly fluctuate
- D) Everyone buys exactly 1 item

<details><summary>Show Answer</summary>

**B) Huge individual sales of massive blockbusters are roughly equaled or eclipsed by the aggregated sales of millions of highly niche items**

The internet removes physical shelf space limitations, allowing the massively long tail of niche products (with very few sales each) to cumulatively dominate economic models.

</details>

---

**Q27.** "Zipf's Law" defines a specific relationship observable in language (and network hubs) where an item's frequency is strictly proportional to:

- A) Its length
- B) $1 / \text{Rank}$
- C) Normal distribution variance
- D) Its betweenness centrality

<details><summary>Show Answer</summary>

**B) $1 / \text{Rank}$**

The 2nd most frequent item occurs 1/2 as often as the 1st. The 3rd most frequent occurs 1/3 as often as the 1st. This is a classic Power Law behavior.

</details>

---

**Q28.** A primary distinction between **biological epidemics** and **social/idea cascades** is:

- A) Biological epidemics involve thresholds and payoffs
- B) Social cascades are typically involuntary; pathogens are chosen strategically
- C) Epidemics are involuntary, somewhat random, and have invisible sources; Idea cascades involve voluntary evaluation, cognitive choice, and known sources
- D) Epidemics spread on complete graphs; ideas don't

<details><summary>Show Answer</summary>

**C) Epidemics are involuntary, somewhat random, and have invisible sources; Idea cascades involve voluntary evaluation, cognitive choice, and known sources**

You don't usually know *who* gave you the flu, and you didn't *choose* to accept it. You usually know exactly who recommended a movie, and you deliberately made a cognitive decision to watch it.

</details>

---

**Q29.** In a percolation model mapping contact paths, a required condition for Node Z to be infected by Node A is:

- A) Node A and Node Z must share a local bridge
- B) There must exist a continuous, fully connected path consisting entirely of "open" (transmitting) edges between A and Z
- C) Node Z must actively want to be infected
- D) The clustering coefficient must be 1

<details><summary>Show Answer</summary>

**B) There must exist a continuous, fully connected path consisting entirely of "open" (transmitting) edges between A and Z**

Every single edge on the path chain must randomly successfully "roll" true (probability $p$) for the contagion to traverse the distance.

</details>

---

**Q30.** The recursive calculation $q_n = 1 - (1 - p \cdot q_{n-1})^k$ represents:

- A) Modularity score
- B) The probability that an epidemic originating at the root of a tree persists to at least depth $n$
- C) The threshold for a behavior cascade
- D) Triadic closure

<details><summary>Show Answer</summary>

**B) The probability that an epidemic originating at the root of a tree persists to at least depth $n$**

This fixed-point analysis function allows epidemiologists to calculate the exact structural probability of a pathogen avoiding early extinction.

</details>

---

## Topic 12 — Small World Effect

---

**Q31.** Stanley Milgram's 1967 letter-forwarding experiment uncovered two massive structural insights regarding human society. They were:

- A) Everyone is connected, and everyone has a high degree
- B) Extremely short paths (roughly 6 degrees) exist globally, AND ordinary people are shockingly capable of finding those paths using only localized, greedy knowledge
- C) Short paths do not exist, and people forward mail randomly
- D) Social networks form perfect grid lattices

<details><summary>Show Answer</summary>

**B) Extremely short paths exist globally, AND ordinary people are shockingly capable of finding those paths using only localized, greedy knowledge**

The "discoverability" via decentralized routing is the most remarkable part. People navigated a 300-million node network in 6 steps using only local names.

</details>

---

**Q32.** In the Watts-Strogatz model, a small-world network is generated starting from a highly clustered regular ring lattice by doing what?

- A) Replacing it with a Barabasi-Albert tree
- B) Iteratively deleting nodes
- C) Randomly "rewiring" a tiny fraction (e.g., 1%) of the local edges to point to distant random nodes across the graph
- D) Changing it into a completely connected clique

<details><summary>Show Answer</summary>

**C) Randomly "rewiring" a tiny fraction (e.g., 1%) of the local edges to point to distant random nodes across the graph**

These few random shortcuts act as global wormholes, drastically destroying the long path diameter of the lattice while preserving its high local clustering structure.

</details>

---

**Q33.** What profound theoretical paradox did Watts and Strogatz resolve?

- A) Why all hubs are connected
- B) The mathematical coexistence of massive localized clustering (lots of tight triangles) AND tiny global path lengths (nobody is far apart)
- C) Why degree distributions follow a power law
- D) Disproving the existence of homophily

<details><summary>Show Answer</summary>

**B) The mathematical coexistence of massive localized clustering AND tiny global path lengths**

Random networks have short paths but zero clustering. Lattices have massive clustering but terrible path lengths. WS proved you can have both simultaneously.

</details>

---

**Q34.** Jon Kleinberg extended Watts-Strogatz by demonstrating that for humans to successfully execute decentralized greedy search (Milgram's experiment):

- A) The random shortcuts cannot be completely random; they must follow a specific distance-based distribution to provide a "sense of direction"
- B) Everyone must know the full topology of the network
- C) The graph must be bipartite
- D) Random shortcuts must be removed

<details><summary>Show Answer</summary>

**A) The random shortcuts cannot be completely random; they must follow a specific distance-based distribution to provide a "sense of direction"**

If shortcuts are truly uniform random, a letter jumps wildly across the country, making greedy search impossible. Humans rely on a structured hierarchy of distances.

</details>

---

**Q35.** In Kleinberg's model constructed on a 2D grid, the probability of a shortcut connecting to a node at distance $d$ is proportional to $d^{-k}$. The greedy search algorithm only achieves stunningly fast $O(\log^2 n)$ efficiency when the exponent $k$ is perfectly equal to:

- A) 0
- B) 1
- C) 2
- D) Infinity

<details><summary>Show Answer</summary>

**C) 2**

Kleinberg proved the optimal $k$ equals the dimension of the grid ($d=2$). This exponent provides the mathematically exact fractal balance of local, medium, and massive long-range jumps necessary to zoom in on a target efficiently.

</details>

---

**Q36.** In Kleinberg's model, if $k = 0$ (meaning every possible node in the grid has an equal chance of receiving the shortcut, essentially Watts-Strogatz), greedy search completely fails. Why?

- A) It removes all shortcuts
- B) Because shortcuts provide wild, unguided jumps devoid of geographic homophily. You jump randomly but can't consistently narrow the distance to the target.
- C) Because it turns the grid into a tree
- D) Because the clustering coefficient reaches zero

<details><summary>Show Answer</summary>

**B) Because shortcuts provide wild, unguided jumps devoid of geographic homophily. You jump randomly but can't consistently narrow the distance to the target.**

Without distance clustering, local decisions don't yield geometric progress.

</details>

---

**Q37.** In Kleinberg's model, if $k$ approaches infinity, what happens to the network?

- A) It becomes a perfectly connected clique
- B) All shortcuts become intensely local, meaning it degrades back into a regular lattice with agonizingly long path diameters
- C) Greedy search becomes $O(1)$
- D) The network disconnects

<details><summary>Show Answer</summary>

**B) All shortcuts become intensely local, meaning it degrades back into a regular lattice with agonizingly long path diameters**

Since probability drops sharply with distance squared, an infinite $k$ means no long-range wormholes ever form. You must walk step-by-step.

</details>

---

**Q38.** Which routing strategy defines "Greedy Decentralized Search"?

- A) Fetching the whole graph and running BFS
- B) At each step, handing the message to the friend in your address book who is geometrically (or socially) closest to the final target
- C) Giving the message to the hub with the highest degree
- D) Randomly tossing the message to any friend

<details><summary>Show Answer</summary>

**B) At each step, handing the message to the friend in your address book who is geometrically (or socially) closest to the final target**

You evaluate your friends based solely on their distance to the target coordinate, entirely blind to the overarching network topology.

</details>

---

**Q39.** The Watts-Strogatz model generates a small-world network, but its mathematical degree distribution:

- A) Exactly mirrors a purely scale-free power law
- B) Has massive hubs with degrees of 10,000
- C) Forms a tight, binomial-esque peak localized around the initial lattice degree, fundamentally lacking massive hubs
- D) Follows a uniform distribution

<details><summary>Show Answer</summary>

**C) Forms a tight, binomial-esque peak localized around the initial lattice degree, fundamentally lacking massive hubs**

WS rewires edges uniformly, so the degree distribution stays bunched tightly together. It fails to recreate the massive Power Law hubs seen in real social networks.

</details>

---

**Q40.** In Milgram's experiment, participants were given basic attributes of the target (occupation, location). These attributes mathematically act as:

- A) Epidemic transmission variables
- B) Coordinates in a multi-dimensional social space used to calculate "distance" for the greedy routing decisions
- C) Balance constraints
- D) Values for the PageRank transition matrix

<details><summary>Show Answer</summary>

**B) Coordinates in a multi-dimensional social space used to calculate "distance" for the greedy routing decisions**

"Boston" handles geographic distance. "Stockbroker" handles occupational/social distance. These allow senders to aggressively narrow the gap at every hop.

</details>

---

## Topic 13 — Viral Diffusion and Influence Maximization

---

**Q41.** A **K-core** of a network is strictly defined as a maximal distinct subgraph where:

- A) Every node is connected to exactly K other nodes
- B) Every node has a mathematical degree of at least K, *specifically connecting to other nodes that are also inside the K-core*
- C) Every node has exactly degree K
- D) There are K fully connected cliques

<details><summary>Show Answer</summary>

**B) Every node has a mathematical degree of at least K, specifically connecting to other nodes that are also inside the K-core**

It's a dense, deeply connected skeletal substructure. Every resident must maintain dense connections with *each other*.

</details>

---

**Q42.** The **K-shell** peeling algorithm is used to determine a node's coreness index. The nodes assigned to K-shell '3' ($B_3$) are those that:

- A) Have degree 3 in the initial global network
- B) Are the 3rd nodes to be removed
- C) Are iteratively removed and collapse during the sequence when the threshold $k$ is raised to exactly 3
- D) Never get removed

<details><summary>Show Answer</summary>

**C) Are iteratively removed and collapse during the sequence when the threshold $k$ is raised to exactly 3**

We "peel" the network like an onion. Any node living on the absolute outer edge of the graph at $k=3$ is ripped away and assigned coreness 3.

</details>

---

**Q43.** It is possible for a massive "Hub" node with a degree of 1,000 to have a terrible coreness index of 1 because of the "Star Topology Trap". How?

- A) It is not possible; degree logically guarantees coreness
- B) All 1,000 of its neighbors have degree 1 (meaning they are fragile leaves). The moment the $k=1$ peeling occurs, all its neighbors vanish instantly, stripping the hub to degree 0 and killing it in the very first round
- C) Its PageRank is too small
- D) It belongs to multiple components

<details><summary>Show Answer</summary>

**B) All 1,000 of its neighbors have degree 1. The moment the $k=1$ peeling occurs, all its neighbors vanish instantly, stripping the hub to degree 0...**

A hub connecting to absolute nobodies has zero structural depth or staying power. It's an illusion of influence.

</details>

---

**Q44.** For orchestrating viral marketing diffusion, empirical cascade data routinely proves that placing seed nodes in the **"Pseudo-core"** (mid-level K-shells) is deeply superior because:

- A) They are significantly cheaper to acquire than absolute innermost core nodes, yet generate surprisingly near-identical large-scale cascades
- B) They have the highest degree centralities in the graph
- C) They form spider traps
- D) They instantly activate all peripheral users

<details><summary>Show Answer</summary>

**A) They are significantly cheaper to acquire than absolute innermost core nodes, yet generate surprisingly near-identical large-scale cascades**

Pseudo-core nodes sit on the ridge of the influence plateau. Marketing ROI here is staggering compared to overpaying superstars in the absolute core.

</details>

---

**Q45.** In the **Independent Cascade Model** of diffusion, the core systemic simulation strictly terminates when:

- A) $R_0 < 1$
- B) The entire network is fully infected
- C) A full time-step iteration executes and registers **zero new node adoptions**
- D) The seed set vanishes

<details><summary>Show Answer</summary>

**C) A full time-step iteration executes and registers zero new node adoptions**

The contagion process pushes forward strictly until the infection frontier hits dead ends everywhere simultaneously and no new conversions trigger.

</details>

---

**Q46.** The "Influence Maximization" algorithmic problem defined by Kempe, Kleinberg, and Tardos asks:

- A) How to calculate PageRank without a damping factor
- B) Given a strict budget $k$, which specific $k$ nodes should be chosen as the initial active seed set to generate the maximum possible absolute expected cascade size?
- C) How to find the shortest path in a dynamic graph
- D) How to maximize modularity density

<details><summary>Show Answer</summary>

**B) Given a strict budget $k$, which specific $k$ nodes should be chosen as the initial active seed set to generate the maximum possible absolute expected cascade size?**

This is the Holy Grail of modern marketing algorithm design on social networks.

</details>

---

**Q47.** The Influence Maximization problem is technically NP-Hard. However, researchers proved that a greedy step-by-step approximation algorithm mathematically guarantees an influence spread equal to at least:

- A) 100% of optimal
- B) 63% (technically $1 - 1/e$) of the mathematically perfect optimal solution
- C) 50% of optimal
- D) The logarithm of optimal

<details><summary>Show Answer</summary>

**B) 63% (technically $1 - 1/e$) of the mathematically perfect optimal solution**

Because the influence function is "submodular," greedy addition algorithmically bounds the worst-case scenario exceptionally well.

</details>

---

**Q48.** In influence math, "Submodularity" is the formal formalization of which economic principle?

- A) Inflationary pricing
- B) The rich get richer
- C) Diminishing marginal returns
- D) Zero-sum games

<details><summary>Show Answer</summary>

**C) Diminishing marginal returns**

Adding a 10th influencer to your marketing campaign invariably reaches fewer *new/unique* users than adding your very 1st influencer did, because their social networks increasingly overlap.

</details>

---

**Q49.** Why does naively selecting the absolute Top-K highest degree nodes sequentially often fail to maximize viral marketing spread?

- A) High degree nodes are usually isolated from one another
- B) Massive "audience overlap". The top nodes are likely tightly clustered together, repeatedly exposing the exact same users inside an echo chamber while entirely neglecting the rest of the network
- C) Degree centrality actually measures betweenness centrality
- D) They lack weak ties

<details><summary>Show Answer</summary>

**B) Massive "audience overlap". The top nodes are likely tightly clustered together, repeatedly exposing the exact same users inside an echo chamber...**

You want influencers distributed across varied, structurally distinct communities, rather than 5 influencers who all talk strictly to the exact same demographic.

</details>

---

**Q50.** In structural decomposition, a node with high coreness but surprisingly low degree is likely:

- A) Structurally impossible
- B) Deeply embedded securely inside a deeply intertwined core clique where it relies entirely on the structural strength of a small, hyper-connected internal community
- C) Situated as a dangling node
- D) Placed on a global bridge

<details><summary>Show Answer</summary>

**B) Deeply embedded securely inside a deeply intertwined core clique where it relies entirely on the structural strength of a small, hyper-connected internal community**

A node with degree 15 can have coreness 15 if absolutely all 15 of its friends also mutually connect to each other forming a clique, creating an incredibly resilient, impossible-to-peel structural block.

</details>

---
> **End of Revision MCQs** — Excellent work! 🎯
