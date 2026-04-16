# 50 Revision MCQs — Topics 5 to 8

> **How to use:** Each answer is hidden. Click **"Show Answer"** to reveal it. This file is designed specifically for revising Topics 5 through 8.

---

## Topic 5 — Schelling Model

---

**Q1.** The main sociological insight of the Schelling model is that:

- A) Extreme segregation requires extreme racism
- B) Even mild individual preferences for similar neighbors can produce extreme macro-level segregation
- C) Integration usually happens naturally over time
- D) Random placement always maintains an integrated state

<details><summary>Show Answer</summary>

**B) Even mild individual preferences for similar neighbors can produce extreme macro-level segregation**

Schelling proved that "micro-motives" (wanting just 1/3 of your neighbors to look like you) diverge radically from "macro-behavior" (the entire city splitting into two massive homogenous blocks).

</details>

---

**Q2.** In the Schelling model, an agent decides to move if:

- A) They are surrounded by too many agents of their own type
- B) The fraction of their same-type neighbors falls below their personal tolerance threshold
- C) They have no empty adjacent cells
- D) A random timer expires

<details><summary>Show Answer</summary>

**B) The fraction of their same-type neighbors falls below their personal tolerance threshold**

Agents evaluate their immediate neighborhood. If the ratio of "like me" neighbors is below their threshold $t$, they become dissatisfied and seek to move.

</details>

---

**Q3.** What happens in a standard Schelling simulation if the threshold is set to 0.0 (0%)?

- A) The grid becomes perfectly segregated
- B) Agents swap places constantly but never settle
- C) No agents move; the initial random configuration strictly persists
- D) All agents crowd into the center of the grid

<details><summary>Show Answer</summary>

**C) No agents move; the initial random configuration strictly persists**

A threshold of 0 means agents are perfectly content regardless of their neighbors' identities. Since nobody is dissatisfied, zero moves occur.

</details>

---

**Q4.** A Schelling grid reaches **equilibrium** when:

- A) Exactly 50% of the grid is segregated
- B) No dissatisfied agents remain, OR no vacant valid spots exist for them to move to
- C) All agents are connected
- D) Every agent has exactly 8 neighbors

<details><summary>Show Answer</summary>

**B) No dissatisfied agents remain, OR no vacant valid spots exist for them to move to**

The simulation stops when no further valid moves can be made because everyone is either satisfied or trapped.

</details>

---

**Q5.** In a grid where agents evaluate 8 surrounding cells (Moore neighborhood), an agent with threshold = 0.5 needs at least:

- A) 2 same-type neighbors
- B) 4 same-type neighbors
- C) 5 same-type neighbors
- D) 8 same-type neighbors

<details><summary>Show Answer</summary>

**B) 4 same-type neighbors**

$50\%$ of 8 is 4. They require at least 4 neighbors of their own type to be satisfied.

</details>

---

**Q6.** The phenomenon where a single agent moving to satisfy their own threshold inadvertently causes multiple neighboring agents to become dissatisfied is called:

- A) Phase transition
- B) Cascading dissatisfaction
- C) Modularity tipping
- D) Triadic closure

<details><summary>Show Answer</summary>

**B) Cascading dissatisfaction**

One agent's solution (moving into a neighborhood) changes the demographics for everyone else already there, potentially triggering a chain reaction of new moves.

</details>

---

**Q7.** Which of the following is a fundamental **limitation** of the classic Schelling model?

- A) It uses a continuous, non-discrete geography
- B) It only models two binary types of agents (e.g., X and O) instead of complex real-world intersections
- C) It requires massive computational power
- D) It cannot show segregation

<details><summary>Show Answer</summary>

**B) It only models two binary types of agents (e.g., X and O) instead of complex real-world intersections**

The original model is binary and relies on a rigid grid. Real cities have multiple ethnic/income groups and highly variable geographic constraints.

</details>

---

**Q8.** "Empty cells" (vacancies) in the Schelling model act mathematically as:

- A) The required medium that permits the physical relocation of agents
- B) Barriers that prevent segregation
- C) Additional agents of a third type
- D) Magnets for different agent types

<details><summary>Show Answer</summary>

**A) The required medium that permits the physical relocation of agents**

If the grid is 100% full, the model instantly freezes because agents have nowhere to go. Vacancies are strictly necessary for the dynamics to play out.

</details>

---

**Q9.** As the threshold $t$ gradually increases from 1/3 toward 1.0, the resulting segregation:

- A) Decreases
- B) Increases continuously
- C) Abruptly transitions from mixed to highly segregated, then eventually freezes because no valid spots exist
- D) Flips to integration

<details><summary>Show Answer</summary>

**C) Abruptly transitions from mixed to highly segregated, then eventually freezes because no valid spots exist**

At extremely high thresholds (e.g., >0.8), nobody can find a spot that satisfies them, so the system jams up or constantly churns.

</details>

---

**Q10.** The gap between "what individuals intend" and "what the population builds" in Schelling's work is a classic example of:

- A) Game theory optimization
- B) Emergent macro-behavior from micro-motives
- C) Preferential attachment
- D) A bipartite graph

<details><summary>Show Answer</summary>

**B) Emergent macro-behavior from micro-motives**

Emergence is when simple local rules interact to create complex, unpredicted global patterns.

</details>

---

**Q11.** If an agent has 5 filled neighbor slots and 3 empty neighbor slots, the ratio evaluated against the threshold is usually based on:

- A) Only the 5 filled slots
- B) All 8 slots
- C) Only empty slots
- D) The grid average

<details><summary>Show Answer</summary>

**A) Only the 5 filled slots**

Agents evaluate the fraction of their *actual* neighbors. If 2 out of 5 are the same type, their ratio is 40% (2/5). Empty slots do not count as neighbors.

</details>

---

**Q12.** If individuals are satisfied with 30% same-type neighbors, what is the usual global segregation percentage achieved in standard models by the end?

- A) 30%
- B) 50%
- C) Often upwards of 70%
- D) 0%

<details><summary>Show Answer</summary>

**C) Often upwards of 70%**

This proves Schelling's main thesis: wanting 30% similarity results in a city that is 70% segregated.

</details>

---

## Topic 6 — Structural Balance

---

**Q13.** A triangle in a signed network is considered **structurally balanced** if it contains:

- A) Only negative edges
- B) Exactly one negative edge
- C) Either zero or two negative edges
- D) Either one or three negative edges

<details><summary>Show Answer</summary>

**C) Either zero or two negative edges**

Balance requires an even number of negative edges. (+, +, +) has zero. (+, -, -) has two. Both are balanced.

</details>

---

**Q14.** The relationship configuration represented by (+, +, -) translates to:

- A) Mutual friendship
- B) "The enemy of my enemy is my friend"
- C) "The friend of my friend is my enemy"
- D) "The enemy of my enemy is my enemy"

<details><summary>Show Answer</summary>

**C) "The friend of my friend is my enemy"**

Two friends share a mutual enemy, but wait—in (+,+,-), A likes B, B likes C, but A hates C. This is psychologically stressful and structurally unbalanced.

</details>

---

**Q15.** Which psychological concept drives structural balance theory?

- A) Triadic closure
- B) Cognitive dissonance
- C) Social influence
- D) The rich get richer

<details><summary>Show Answer</summary>

**B) Cognitive dissonance**

People experience stress (dissonance) when their relationships don't align logically (e.g., two of your best friends hating each other). Changing the relationships relieves this stress.

</details>

---

**Q16.** The triad (-, -, -) is:

- A) Unbalanced
- B) Balanced
- C) Undefined because it has no positive edges
- D) The most stable configuration

<details><summary>Show Answer</summary>

**A) Unbalanced**

It has three negative edges (an odd number). "The enemy of my enemy is my enemy" creates a situation where two of the enemies are incentivized to team up against the third, pushing one edge to positive (+, -, -).

</details>

---

**Q17.** The **Balance Theorem** proves that if a completely connected graph is balanced, it can always be divided into:

- A) Three equally sized groups
- B) A single group of mutual friends, or exactly two warring factions
- C) A core and a periphery
- D) Randomly distributed clusters

<details><summary>Show Answer</summary>

**B) A single group of mutual friends, or exactly two warring factions**

This is the brilliant global conclusion of balance theory: local triangle rules mathematically force the entire globe into maximum two factions (e.g., Axis vs Allies).

</details>

---

**Q18.** If a network is partitioned into two factions where everyone inside faction A are friends, everyone inside faction B are friends, and everyone in A hates everyone in B, then every triangle in the graph must be:

- A) (+, +, +)
- B) (+, -, -)
- C) Either (+, +, +) or (+, -, -)
- D) Unbalanced

<details><summary>Show Answer</summary>

**C) Either (+, +, +) or (+, -, -)**

Triangles contained entirely *within* A or B are (+, +, +). Triangles spanning across the factions (two nodes in A, one in B) are (+, -, -). Thus, all triangles are balanced.

</details>

---

**Q19.** How does structural balance generalize to cycles larger than triangles (e.g., squares, pentagons)?

- A) Only triangles matter for balance
- B) A cycle is balanced if and only if it contains an even number of negative edges
- C) All cycles must be purely positive
- D) It depends on the cluster density

<details><summary>Show Answer</summary>

**B) A cycle is balanced if and only if it contains an even number of negative edges**

This cycle characterization proves that multiplying the signs of the edges around any closed loop must result in a positive sign (+) for the network to be balanced.

</details>

---

**Q20.** If A hates B, and B hates C, structural balance predicts that A and C will be:

- A) Enemies
- B) Friends
- C) Neutral
- D) Cannot be determined

<details><summary>Show Answer</summary>

**B) Friends**

To resolve the triad into a balanced state (+, -, -), the relationship between A and C must become positive. "The enemy of my enemy is my friend."

</details>

---

**Q21.** Which configuration is known to be the most volatile (resolves the fastest) in human social networks?

- A) (+, +, +)
- B) (+, -, -)
- C) (+, +, -)
- D) All resolve equally fast

<details><summary>Show Answer</summary>

**C) (+, +, -)**

Having two good friends who hate each other creates intense immediate social pressure to either reconcile them (to +++) or drop one of them (to +--).

</details>

---

**Q22.** A network completely lacking any negative edges is structurally:

- A) Unbalanced
- B) Balanced
- C) Not enough information
- D) Impossible

<details><summary>Show Answer</summary>

**B) Balanced**

A network with zero negative edges consists entirely of (+,+,+) triangles, which satisfies the condition of having an even number (zero) of negative edges.

</details>

---

**Q23.** In international relations, what major historical event is often modeled using structural balance theory sliding into two factions?

- A) The fall of the Roman Empire
- B) The alliances preceding World War I (Allied vs Central Powers)
- C) The spread of the Black Death
- D) The industrial revolution

<details><summary>Show Answer</summary>

**B) The alliances preceding World War I (Allied vs Central Powers)**

As treaties and rivalries shifted, the network naturally organized into two distinct, mutually hostile alliance blocs predicted by the Balance Theorem.

</details>

---

**Q24.** Weak structural balance theory modifies the original theorem by allowing which unbalanced triad to be considered temporarily stable?

- A) (+, +, -)
- B) (-, -, -)
- C) (+, -, -)
- D) None

<details><summary>Show Answer</summary>

**B) (-, -, -)**

Weak structural balance allows for (-, -, -) because in reality, multiple distinct factions can all mutually hate each other (e.g., 3 opposing armies), meaning the network can split into more than two factions.

</details>

---

## Topic 7 — PageRank and Web Graph

---

**Q25.** The foundational idea behind Google's PageRank algorithm is that an important page:

- A) Has the most text on it
- B) Is pointed to by other important pages
- C) Directly pays for its rank
- D) Always points to important pages

<details><summary>Show Answer</summary>

**B) Is pointed to by other important pages**

Ranking is not just based on in-degree (quantity of links) but on the recursive *quality* of incoming links.

</details>

---

**Q26.** In the absence of teleportation, if node A has 3 outgoing links and a PageRank score of 9, how much score does it pass to each of the 3 nodes it points to?

- A) 9 to each
- B) 3 to each
- C) 1 to each
- D) It absorbs the score

<details><summary>Show Answer</summary>

**B) 3 to each**

A node distributes its PageRank equally among its outgoing links: $PR(A) / \text{out-degree}(A) = 9/3 = 3$.

</details>

---

**Q27.** A "dangling node" in the context of PageRank is a node that:

- A) Only points to itself
- B) Has an in-degree of 0
- C) Has an out-degree of 0
- D) Belongs to multiple strongly connected components

<details><summary>Show Answer</summary>

**C) Has an out-degree of 0**

It has no outgoing links and acts as a "sink," absorbing rank from the network but never passing it on.

</details>

---

**Q28.** Why do dangling nodes computationally break the basic PageRank algorithm?

- A) They cause the transition matrix to have a column of all zeroes, ruining the Markov property and causing scores to drain out of the system.
- B) They raise scores to infinity.
- C) They cause the graph to become un-directed.
- D) They reverse the flow of PageRank.

<details><summary>Show Answer</summary>

**A) They cause the transition matrix to have a column of all zeroes, ruining the Markov property and causing scores to drain out of the system.**

If a column sums to 0, total rank is not conserved during matrix multiplication, and all eigenvalues fall below 1.

</details>

---

**Q29.** The purpose of the PageRank **damping factor ($d$)**, commonly set to 0.85, is to:

- A) Make the math easier
- B) Ensure that a "random surfer" occasionally teleports to a random page, preventing them from getting stuck in sinks or infinite loops
- C) Force all pages to have the same PageRank
- D) Count the number of incoming links

<details><summary>Show Answer</summary>

**B) Ensure that a "random surfer" occasionally teleports to a random page, preventing them from getting stuck in sinks or infinite loops**

Teleportation guarantees that the graph is strongly connected mathematically, ensuring a unique steady-state vector exists.

</details>

---

**Q30.** With a damping factor $d$ and total nodes $N$, the equation for the PageRank $PR(v)$ of node $v$ is:

- A) $PR(v) = \frac{1-d}{N} + d \sum_{u \to v} \frac{PR(u)}{out(u)}$
- B) $PR(v) = d + \frac{1-d}{N} \sum_{u \to v} PR(u)$
- C) $PR(v) = \frac{1-d}{N}$
- D) $PR(v) = d \times in(v)$

<details><summary>Show Answer</summary>

**A) $PR(v) = \frac{1-d}{N} + d \sum_{u \to v} \frac{PR(u)}{out(u)}$**

This formula splits the score into two parts: the guaranteed baseline rank from random teleportation, and the rank passed through normal link following.

</details>

---

**Q31.** The column sums of a standard valid PageRank transition matrix must equal:

- A) N
- B) 0
- C) 1
- D) The node's degree

<details><summary>Show Answer</summary>

**C) 1**

Markov transition matrices must be column-stochastic, meaning probabilities in each column sum exactly to 1 (100% of the rank is distributed).

</details>

---

**Q32.** According to the Perron-Frobenius theorem, why does PageRank iteratively converge?

- A) Because the network is bipartite
- B) Because the stochastic, irreducible matrix has a unique dominant eigenvalue of exactly 1
- C) Because it removes negative edges
- D) Because we start all nodes at 0

<details><summary>Show Answer</summary>

**B) Because the stochastic, irreducible matrix has a unique dominant eigenvalue of exactly 1**

The teleportation factor makes the matrix irreducible and strictly positive. The theorem guarantees the largest eigenvalue is 1, and repeated multiplication converges to its associated eigenvector.

</details>

---

**Q33.** A small cycle of pages that exclusively point to each other without linking outward is known as a:

- A) Hub and authority pair
- B) Spider trap
- C) Bipartite cluster
- D) Giant component

<details><summary>Show Answer</summary>

**B) Spider trap**

A spider trap is a closed loop. Without a damping factor, random surfers get stuck in the cycle, gradually sucking up all the PageRank in the network.

</details>

---

**Q34.** Unlike an undirected social network, the World Wide Web graph is highly:

- A) Symmetric
- B) Directed
- C) Balanced
- D) Complete

<details><summary>Show Answer</summary>

**B) Directed**

Hyperlinks are one-way streets. Page A linking to Page B does not mean Page B links back to Page A.

</details>

---

**Q35.** The steady-state vector mathematically represents:

- A) The degrees of all nodes
- B) The long-term probability of a random surfer being at any given page
- C) The distance between the highest and lowest ranked nodes
- D) The clustering coefficient

<details><summary>Show Answer</summary>

**B) The long-term probability of a random surfer being at any given page**

At equilibrium, multiplying by the transition matrix returns the exact same vector. The scores reflect the percentage of time a random surfer spends on each page.

</details>

---

**Q36.** True or False: In standard PageRank without teleportation, if the entire network forms a perfect circle (A→B→C→...→A), every node will eventually receive an identical PageRank score.

- A) True
- B) False

<details><summary>Show Answer</summary>

**A) True**

Due to perfect symmetry, the rank flows infinitely in a circle, and all nodes will have an equal score of $1/N$.

</details>

---

**Q37.** In a large real-world network, how many iterations does the PageRank algorithm typically need to converge reasonably?

- A) Only 1
- B) Exactly N iterations
- C) Around 30 to 50 iterations
- D) Over a million

<details><summary>Show Answer</summary>

**C) Around 30 to 50 iterations**

Due to the power method and the separation between the largest eigenvalue (1) and the second largest (roughly equal to the damping factor 0.85), it converges very fast.

</details>

---

## Topic 8 — Diffusion and Cascades

---

**Q38.** In the linear threshold model, a node adopts a new behavior B if the fraction of its neighbors using B is:

- A) Less than $q$
- B) Exactly 100%
- C) Greater than or equal to its threshold $q$
- D) Greater than 0%

<details><summary>Show Answer</summary>

**C) Greater than or equal to its threshold $q$**

Once the proportion reaches the tipping point threshold $q$, the node flips.

</details>

---

**Q39.** If the payoff for sticking with old behavior A is $a$, and the payoff for adopting new behavior B is $b$, the mathematical threshold $q$ for switching to B is:

- A) $q = a / b$
- B) $q = a / (a + b)$
- C) $q = b / (a + b)$
- D) $q = a \times b$

<details><summary>Show Answer</summary>

**B) $q = a / (a + b)$**

The threshold is proportional to the value of the old technology. If $a$ is very high (A is very good), the threshold to switch to B will be very high.

</details>

---

**Q40.** A network cascade succeeds when:

- A) It stops at the seed nodes
- B) It gets blocked by a cluster
- C) It propagates from the seed nodes to flip every reachable node in the network to the new behavior
- D) The clustering coefficient becomes 1

<details><summary>Show Answer</summary>

**C) It propagates from the seed nodes to flip every reachable node in the network to the new behavior**

A total cascade achieves 100% adoption.

</details>

---

**Q41.** The **Cluster Density Theorem** mathematically defines an impenetrable cluster as a set of nodes where the internal edge density is strictly greater than:

- A) $q$
- B) $1 - q$
- C) $q^2$
- D) $p \times k$

<details><summary>Show Answer</summary>

**B) $1 - q$**

If the internal density is $> 1-q$, then any node inside the cluster has at most $< q$ connections to the outside. Therefore, even if the entire outside adopts B, the nodes inside will never reach the threshold $q$ required to switch.

</details>

---

**Q42.** "Bilingual" nodes in diffusion networks refer to individuals who:

- A) Speak two languages natively
- B) Can adopt both technology A and B simultaneously, bridging structurally rigid groups
- C) Always reject new technology
- D) Are isolated from the network

<details><summary>Show Answer</summary>

**B) Can adopt both technology A and B simultaneously, bridging structurally rigid groups**

By absorbing the cost of maintaining both (like installing MacOS and Windows), they lower the neighborhood threshold for others, acting as a catalyst for the cascade to penetrate dense clusters.

</details>

---

**Q43.** The subset of early adopters who initiate the cascade are referred to as the:

- A) K-core
- B) Giant component
- C) Seed set
- D) Hubs

<details><summary>Show Answer</summary>

**C) Seed set**

These are the nodes exogenously flipped to B at $T=0$. Strategic marketing focuses on optimally choosing this exact seed set.

</details>

---

**Q44.** The fundamental difference between a coordination game cascade and an information cascade is:

- A) Coordination games are irrational; information cascades are rational
- B) Coordination cascades depend heavily on network structure and explicit payoffs; information cascades are driven by observing sequences of actions, often ignoring private signals
- C) Information cascades only happen on bipartite graphs
- D) Coordination cascades don't use thresholds

<details><summary>Show Answer</summary>

**B) Coordination cascades depend heavily on network structure and explicit payoffs; information cascades are driven by observing sequences of actions, often ignoring private signals**

Coordination games are "I want to be compatible with my friends." Information cascades are "I don't know the answer, but those people seem to know, so I will copy them."

</details>

---

**Q45.** How do you forcefully break a blocking cluster to allow a cascade to continue?

- A) Increase the threshold $q$
- B) Increase the benefit of technology A
- C) Ensure the initial seed set includes key nodes *inside* the dense cluster
- D) Remove all weak ties

<details><summary>Show Answer</summary>

**C) Ensure the initial seed set includes key nodes inside the dense cluster**

If the cascade bounces off the rigid outer wall of a dense cluster, the only mathematical way to take the cluster is to plant seeds inside it so the contagion spreads from within.

</details>

---

**Q46.** If $q = 0.40$ (40% B-neighbors needed to switch), what internal density of A-users is required to block the cascade from entering?

- A) $> 0.40$
- B) $> 0.50$
- C) $> 0.60$
- D) $> 1.00$

<details><summary>Show Answer</summary>

**C) $> 0.60$**

The formula is internal density $> 1 - q$. $1 - 0.40 = 0.60$. A cluster where members have more than 60% of their friendships within the cluster will reject the cascade of B.

</details>

---

**Q47.** Complex contagions (like costly behaviors or high-tech adoptions) differ from simple contagions (like rumors or viruses) because:

- A) They spread primarily through weak ties
- B) They require multiple reinforcing signals (thresholds) rather than just a single contact
- C) They can never create cascades
- D) They do not involve networks

<details><summary>Show Answer</summary>

**B) They require multiple reinforcing signals (thresholds) rather than just a single contact**

A disease requires 1 edge (simple contagion). Adopting a new expensive behavior requires seeing 5 friends do it (complex contagion).

</details>

---

**Q48.** Weak ties are paradoxically **bad** at spreading complex contagions because:

- A) Weak ties transmit diseases
- B) Complex contagions require high reinforcement, and a single weak tie rarely pushes a node over its required threshold $q$
- C) They increase betweenness centrality
- D) They cannot bridge structural holes

<details><summary>Show Answer</summary>

**B) Complex contagions require high reinforcement, and a single weak tie rarely pushes a node over its required threshold $q$**

A weak tie provides one single signal. If you need 40% of your friends to adopt something, one acquaintance mentioning it won't trigger you to switch. Dense clusters (strong ties) are better for complex contagions.

</details>

---

**Q49.** Financial contagions spread through direct contractual obligations rather than mere imitation. This is best modeled mathematically by:

- A) Balance sheets where dropping asset values trigger insolvency, which cascades to creditors
- B) The PageRank teleportation factor
- C) The Schelling segregation grid
- D) Strong triadic closure

<details><summary>Show Answer</summary>

**A) Balance sheets where dropping asset values trigger insolvency, which cascades to creditors**

When a bank fails, it literally defaults on loans owed to other banks, directly degrading their balance sheets and triggering a mechanical cascade.

</details>

---

**Q50.** In the linear threshold model, nodes switch back to behavior A if the number of B-users drops back below $q$.

- A) True
- B) False

<details><summary>Show Answer</summary>

**B) False**

In the standard irreversible cascade model, once a node adopts the new technology B, it stays with B permanently. The diffusion is monotonic.

</details>

---
> **End of Revision MCQs** — Great job! 🎯
