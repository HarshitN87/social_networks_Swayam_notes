# HITS, Recommender Systems & PageRank — Plain Language Notes

> **What this covers:** How do we decide which webpages, users, or papers are "important" in a network? This file explains three closely related ideas — Recommender Systems, the HITS algorithm, and PageRank — building from simple intuition all the way to the linear algebra behind them.

---

## Part 1 — Recommender Systems (The Warm-Up Idea)

### What is a Recommender System?

Imagine you're trying to find good YouTube channels about cooking. You could:
1. Ask your friend who watches a lot of cooking videos — they might recommend 5 channels.
2. Ask another friend who only watches one cooking channel — they recommend just that.

Now think about this: **whose recommendation do you trust more?**

You trust the friend who recommends only a few channels **if** those channels are genuinely great. And you trust a channel more if it's recommended by people whose other recommendations are also good.

This is exactly what a **recommender system** does. It creates a loop of trust:

```
Good channel → trusted recommender → more trusted → recommends better channels → ...
```

> **Key idea:** A recommender's quality goes up when its recommendations are good.
> A resource's quality goes up when good recommenders point to it.
> Each one improves the other — this is called **mutual reinforcement**.

---

### The Structure — A Bipartite Graph

In the course example, we have:
- **3 Recommenders** (think of them as YouTube channels that create "Top 5 lists")
- **5 Resources** (the actual content being recommended)

This forms what's called a **bipartite graph** — a graph with two separate groups where edges only go **from one group to the other**. No recommender points to another recommender. No resource points to another resource.

```
RECOMMENDERS             RESOURCES

    R1  ──────────────►  S1
    R1  ──────────────►  S2
    R2  ──────────────►  S2
    R2  ──────────────►  S3
    R2  ──────────────►  S4
    R3  ──────────────►  S1
    R3  ──────────────►  S5
```

In the diagram above, R1 endorses S1 and S2. R3 endorses S1 and S5. Notice that S1 gets endorsed by **two recommenders** (R1 and R3), so it might score higher than S5, which only has R3.

![Bipartite Recommender System — 3 recommenders, 5 resources, scoring cycle](images/hits_bipartite_recommender.svg)

---

### How Scoring Works

**Step 1 — Give everyone a starting score of 1.**

Both recommenders and resources start equal. Nobody is more important than anyone else yet.

**Step 2 — Update scores using these two rules:**

| Who? | Their new score = |
|---|---|
| **A Recommender** | Add up the scores of every resource it points to |
| **A Resource** | Add up the scores of every recommender that points to it |

**Step 3 — Normalize (scale down the scores so they don't grow forever)**

After updating, divide each node's score by the total score of everyone in its group.

$$
\text{Normalized score of } x = \frac{\text{score of } x}{\text{sum of all scores in the same group}}
$$

**Why normalize?** Without it, every round the numbers just keep getting bigger. Normalization keeps everything between 0 and 1, so we're comparing proportions — not growing piles of numbers.

**Step 4 — Repeat Steps 2 and 3 around 200 times.** After enough rounds, the scores stop changing. This is called **convergence** — the system has found its stable answer.

#### Tiny Worked Example

Say we have 2 recommenders (R1, R2) and 2 resources (S1, S2):
- R1 → S1, S2
- R2 → S2

**Round 0 (start):** R1=1, R2=1, S1=1, S2=1

**Round 1 — Update resources:**
- S1's new score = score of R1 (only R1 points to S1) = **1**
- S2's new score = score of R1 + score of R2 = 1 + 1 = **2**

**Round 1 — Normalize resources (total = 1+2 = 3):**
- S1 = 1/3 ≈ **0.33**
- S2 = 2/3 ≈ **0.67**

S2 scores higher because two recommenders point to it. Makes sense!

**Round 1 — Update recommenders:**
- R1's new score = S1 + S2 = 0.33 + 0.67 = **1.0**
- R2's new score = S2 = **0.67**

**Round 1 — Normalize recommenders (total = 1.0+0.67 = 1.67):**
- R1 = 1.0/1.67 ≈ **0.60**
- R2 = 0.67/1.67 ≈ **0.40**

R1 ranks higher because it recommends more (and highly-endorsed) resources.

---

### Why Does It Converge?

After enough rounds, the numbers reach a **steady state** — each round produces the exact same values as the previous one. This happens because:

1. **Normalization keeps values bounded** — they can't grow forever.
2. **Each round is essentially a matrix multiplication** — mathematically guaranteed to stabilize.
3. **The Perron-Frobenius theorem** (fancy maths) says: for any well-behaved system like this, there is exactly one stable solution, and the iteration always finds it.

> Think of it like shaking a jar of sand. No matter how you start shaking it, eventually the sand settles into the same lowest-energy arrangement. The network's scores do the same thing.

---

## Part 2 — The HITS Algorithm

### From Bipartite to Any Graph

The recommender system we just studied was **bipartite** — two separate groups. But most real networks (the web, social media, citations) don't have this clean separation. Any page can link to any page.

**HITS** (Hyperlink-Induced Topic Search) is the version of the same idea that works on **any directed graph**. The key twist: instead of one score per node, every node gets **two scores**.

---

### Two Scores per Node: Hub and Authority

Every node in a HITS-analyzed network plays two roles at the same time:

| Score | Name | What it means in plain English |
|---|---|---|
| **Hub score** $h(v)$ | "Good pointer" | You are a good hub if you link to many high-quality pages |
| **Authority score** $a(v)$ | "Good destination" | You are a good authority if many good hubs link to you |

**A helpful analogy:**

- **Hub** = A knowledgeable librarian who always recommends the best books. Their value comes from how good their recommendations are.
- **Authority** = A brilliant textbook that every great librarian recommends. Its value comes from how many trusted librarians endorse it.

A great librarian (hub) makes books more famous. Famous books (authorities) make the librarian more credible. They lift each other up — mutual reinforcement.

> **Origin:** HITS was invented by Jon Kleinberg in 1999 to rank websites. Early web directories (like Yahoo's) were exactly this: the directory was the hub, and the websites it listed were authorities.

---

### The Two Formulas (Explained Simply)

**Hub score formula:**

$$
h(v) = \sum_{\text{all pages } u \text{ that } v \text{ links to}} a(u)
$$

**In plain English:** Your hub score = add up the authority scores of everyone you link to.

If you link to 3 pages with authority scores 5, 3, and 2 → your hub score = 5+3+2 = **10**.

---

**Authority score formula:**

$$
a(v) = \sum_{\text{all pages } u \text{ that link to } v} h(u)
$$

**In plain English:** Your authority score = add up the hub scores of everyone who links to you.

If 2 hubs with scores 3 and 5 link to you → your authority score = 3+5 = **8**.

![HITS Algorithm — Hub & Authority Mutual Reinforcement](images/hits_hub_authority.svg)

---

### Step-by-Step: How to Run HITS

Here's the full algorithm in simple steps:

**Step 1:** Give every node a hub score of 1 and an authority score of 1.

**Step 2:** Update authority scores
→ For each node, add up the hub scores of *all nodes that point to it*.

**Step 3:** Update hub scores
→ For each node, add up the authority scores of *all nodes it points to*.

**Step 4:** Normalize
→ Divide every hub score by the total of all hub scores (so they sum to 1).
→ Divide every authority score by the total of all authority scores.

**Step 5:** Go back to Step 2 and repeat until the numbers stop changing.

> **Important rule:** Always do Steps 2 and 3 using the scores from the *previous* round, not the updated ones mid-round. If you mix current and previous values, you'll get wrong results.

---

### Worked Example: Calculating Scores

**Question:** A user on a social platform is followed by two hubs. Those hubs have hub scores of **3** and **5**. What is the user's authority score before normalization?

**Answer:**
$$a(\text{user}) = 3 + 5 = \mathbf{8}$$

That's it! Just add up all the hub scores of nodes pointing to you.

---

**Question:** A research paper is cited by two other papers. Those papers have hub scores of **1.5** and **2.5**. What is this paper's authority score before normalization?

**Answer:**

a(\text{paper}) = 1.5 + 2.5 = \mathbf{4.0}

Once again, you just add up the hub scores of the papers pointing to it.

---

### HITS vs. PageRank: When to Use Which?

| | HITS | PageRank |
|---|---|---|
| **How many scores per node?** | Two (hub + authority) | One (a single rank) |
| **Best used for** | Focused, topic-specific queries | Ranking an entire large network |
| **Applied to** | A small subgraph built per query | The whole graph, once |
| **Stability** | Sensitive — adding/removing a few nodes can change rankings a lot | Stable — small changes don't shift rankings much |
| **Convergence** | Yes, always converges | Yes, always converges (with damping) |
| **Main weakness** | Easily thrown off by irrelevant parts of the graph; no global sense of importance | Sink nodes (pages with no links) break it — needs the damping factor fix |

> **Why HITS struggles on large graphs:** Imagine running HITS on all of Twitter. Adding just one new popular user can cascade changes through millions of hub/authority scores. HITS works beautifully on a small set of fitness-related accounts, but poorly on all 300 million users at once. PageRank handles the big picture far better.

---

## Part 3 — PageRank: Your Rank Depends on Who Points to You

### The Core Idea (No Maths Yet)

**PageRank** was created by Larry Page and Sergey Brin — the founders of Google — to rank web pages. The insight was beautifully simple:

> **A page is important if important pages link to it.**

This seems circular (you need to know who's important *to* know who's important) but it can be solved with iteration, just like our recommender system.

**Think of it this way:** Imagine every page on the web has some "coins." At each round:
- Every page takes all its coins and distributes them equally to every page it links to.
- Pages that receive coins from many important (rich) pages accumulate more coins.
- After enough rounds, the coin distribution stabilizes. Pages with the most coins = most important.

**The conservation rule:** The total coins in the system never changes. If A gives coins to B and C, A ends up with zero, but B and C each got some. No coins are created or destroyed. This is identical to the bipartite recommender normalization.

---

### Three-Node Example: Walking Through Every Step

Let's make this concrete. We have three nodes: **A**, **B**, **C**.

**The links:**
- A → C (A points only to C)
- C → B (C points only to B)
- B → A and B → C (B splits its coins equally: 50% to A, 50% to C)

**Starting values:** Each node gets 1/3 of the total (equal share to start).

```
A = 1/3    B = 1/3    C = 1/3
```

#### Iteration 1: What happens?

**Node A** only receives from B (which gives 50% of its coins to A):

$$
A_{new} = \frac{1}{2} \times B_{old} = \frac{1}{2} \times \frac{1}{3} = \frac{1}{6} \approx 0.167
$$

**Node B** only receives from C (which gives all of its coins to B):

$$
B_{new} = C_{old} = \frac{1}{3} \approx 0.333
$$

**Node C** receives from both A (all of A's coins) and B (50% of B's coins):

$$
C_{new} = A_{old} + \frac{1}{2} \times B_{old} = \frac{1}{3} + \frac{1}{6} = \frac{2}{6} + \frac{1}{6} = \frac{3}{6} = \frac{1}{2} = 0.500
$$

After Iteration 1: **A = 0.167, B = 0.333, C = 0.500** ✅ (total = 1.0, conserved)

#### What happens over time?

| Round | A | B | C |
|---|---|---|---|
| 0 (start) | 0.333 | 0.333 | 0.333 |
| 1 | 0.167 | 0.333 | 0.500 |
| 2 | 0.167 | 0.500 | 0.333 |
| 3 | 0.250 | 0.333 | 0.417 |
| 5 | 0.208 | 0.389 | 0.403 |
| 10 | 0.200 | 0.401 | 0.399 |
| **∞ (converged)** | **0.200** | **0.400** | **0.400** |

The values wobble around at first, then gradually settle. After enough rounds, the numbers lock in.

**Final answer:** A = 0.2, B = 0.4, C = 0.4. The ratio is **A : B : C = 1 : 2 : 2**.

> **What this tells us:** Node A is the least important — it only receives from B (which splits its value). B and C are equally important. This makes intuitive sense: B and C form a "feeding loop" — C feeds B and gets fed back from A, while B gets fed by C.

![PageRank 3-Node Iteration — Convergence to A=0.2, B=0.4, C=0.4](images/hits_pagerank_iteration.svg)

---

### The General PageRank Formula

For any node $v$ in any directed graph:

$$
PR(v) = \sum_{\text{all nodes } u \text{ that link to } v} \frac{PR(u)}{\text{number of outgoing links from } u}
$$

**Breaking this down:**
- Look at everyone who links to you.
- Each of them gives you a fraction of their score.
- The fraction they give is: their score ÷ how many total links they have going out.

**Why divide by outgoing links?** Because if someone links to 100 pages, each page only gets 1/100th of their score. But if someone links to only 2 pages, each gets 1/2. A selective endorser is more valuable.

---

### Five-Node Example: System of Equations

In a 5-node network (A, B, C, D, E), the PageRank of each node depends on its neighbors. Suppose:
- C has 3 outgoing links (so it gives 1/3 of its value to each neighbor)
- A receives from C only → $A = \frac{C}{3}$
- E provides half its value to B → $B = A + \frac{E}{2}$
- E receives from both D (fully) and C (1/3 share) → $E = D + \frac{C}{3}$

All these equations are happening simultaneously and are all interdependent. You can't solve one without knowing the others. That's why we don't try to solve them with algebra — we just **iterate** (guess, update, repeat) until the numbers converge.

---

## Part 4 — The Matrix Behind PageRank

### Why Matrices?

Doing the PageRank update for thousands or millions of nodes by hand is impossible. Matrices let us do all the updates for **every node at once** with a single multiplication.

### Step 1: Represent the Network as a Column Vector

The current scores of all nodes are stored in a column vector. For our 3-node example with initial scores of 1/3 each:

$$
\mathbf{r}^{(0)} = \begin{bmatrix} 1/3 \\ 1/3 \\ 1/3 \end{bmatrix} \leftarrow \text{(A's score, B's score, C's score)}
$$

### Step 2: Build the Transition Matrix M

The **transition matrix** M tells us "how does each node distribute its score to others?"

**Rule for filling in matrix M:**
- Look at each column. Column $j$ represents node $j$.
- For every node that $j$ links to, put $\frac{1}{\text{out-degree of } j}$ in that row.
- Everywhere else, put 0.

For our A→C, C→B, B→A+C graph (rows = destination, columns = source):

$$
M = \begin{bmatrix}
\text{row A} \\ \text{row B} \\ \text{row C}
\end{bmatrix}
= \begin{bmatrix}
0 & \frac{1}{2} & 0 \\
0 & 0 & 1 \\
1 & \frac{1}{2} & 0
\end{bmatrix}
$$

**Reading the columns:**
- **Column 1 (A):** A only links to C → A's entire score goes to row C → $M_{3,1} = 1$
- **Column 2 (B):** B links to both A and C, splitting 50/50 → $M_{1,2} = \frac{1}{2}$ and $M_{3,2} = \frac{1}{2}$
- **Column 3 (C):** C only links to B → $M_{2,3} = 1$

### Step 3: One Matrix Multiply = One Round of Updates

$$
\mathbf{r}^{(t+1)} = M \cdot \mathbf{r}^{(t)}
$$

Let's verify this gives us the right answer for Iteration 1:

$$
M \cdot \mathbf{r}^{(0)} = \begin{bmatrix} 0 & 1/2 & 0 \\ 0 & 0 & 1 \\ 1 & 1/2 & 0 \end{bmatrix} \begin{bmatrix} 1/3 \\ 1/3 \\ 1/3 \end{bmatrix}
$$

- Row A: $0 \times \frac{1}{3} + \frac{1}{2} \times \frac{1}{3} + 0 \times \frac{1}{3} = \frac{1}{6}$ ✅
- Row B: $0 \times \frac{1}{3} + 0 \times \frac{1}{3} + 1 \times \frac{1}{3} = \frac{1}{3}$ ✅
- Row C: $1 \times \frac{1}{3} + \frac{1}{2} \times \frac{1}{3} + 0 \times \frac{1}{3} = \frac{1}{2}$ ✅

This matches what we computed manually! ✅

After $k$ rounds: $\mathbf{r}^{(k)} = M^k \cdot \mathbf{r}^{(0)}$ (apply M repeatedly, k times).

---

## Part 5 — Markov Matrices: Why This Always Works

### What is a Markov Matrix?

A **Markov matrix** (also called a stochastic matrix) is any matrix where **every column adds up to exactly 1**.

Check our matrix M:
- Column 1: $0 + 0 + 1 = 1$ ✅
- Column 2: $\frac{1}{2} + 0 + \frac{1}{2} = 1$ ✅
- Column 3: $0 + 1 + 0 = 1$ ✅

**Why does this column-sum-to-1 rule matter?**

It's the mathematical way of saying: **every coin that leaves a node must land somewhere**. If you have 0.4 units at node B, and B links to A and C equally, then 0.2 goes to A and 0.2 goes to C. The total stays 0.4. Nothing is created. Nothing disappears.

Because of this property, the total across all nodes stays constant through every multiplication:

$$
\text{(total before)} = \text{(total after)} \quad \text{always}
$$

This guarantees that the system won't explode to infinity or collapse to zero. **A stable equilibrium must always exist.**

---

### Why Does It Converge? (The Eigenvalue Explanation)

This is the deep mathematics behind why repeated multiplication always settles down.

**What's an eigenvalue?** When you multiply a matrix M by a special vector $\mathbf{v}$, the result might be the same vector, just scaled:

$$
M \mathbf{v} = \lambda \mathbf{v}
$$
Here, $\lambda$ is the **eigenvalue** and $\mathbf{v}$ is the **eigenvector**. Think of it as: the matrix stretches this vector by a factor of $\lambda$ but doesn't rotate it.

**Key fact about Markov matrices:** Every Markov matrix has a **largest eigenvalue of exactly 1**. All other eigenvalues have absolute value **less than 1** (i.e., $|\lambda| < 1$).

**Now here's the key insight:**

Any starting vector $\mathbf{r}^{(0)}$ can be split into a combination of eigenvectors:

$$
\mathbf{r}^{(0)} = c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_n \mathbf{v}_n
$$

After applying M repeatedly ($k$ times):

$$
\mathbf{r}^{(k)} = c_1 \lambda_1^k \mathbf{v}_1 + c_2 \lambda_2^k \mathbf{v}_2 + \cdots + c_n \lambda_n^k \mathbf{v}_n
$$

Now think about what happens as $k$ gets very large:
- $\lambda_1 = 1$ → $1^k = 1$ → the first term **stays constant forever**
- $|\lambda_2| < 1$ → $\lambda_2^k \to 0$ → the second term **fades to zero**
- $|\lambda_3| < 1$ → $\lambda_3^k \to 0$ → the third term **also fades to zero**
- … and so on for all other terms

**What's left?** Only the first term: $c_1 \mathbf{v}_1$. Everything else vanished.

$$
\mathbf{r}^{(k)} \xrightarrow{k \to \infty} c_1 \mathbf{v}_1
$$

The final stable PageRank vector is just the **dominant eigenvector** of M (the one associated with $\lambda = 1$).

![Markov Matrix Structure & Eigenvalue Convergence Proof](images/hits_markov_eigenvalue.svg)

#### What Does This Mean in Plain English?

| Mathematical Fact | What It Means for PageRank |
|---|---|
| $\lambda_1 = 1$ | There is one "final answer" vector that never changes when M is applied to it |
| All other $|\lambda_i| < 1$ | The "noise" from your starting guess fades away, round by round |
| Convergence guaranteed | No matter what scores you start with, you always end up at the same final ranking |
| PageRank = dominant eigenvector | The stable rankings are a fundamental property of the **structure** of the graph, not your initial guess |

> **Key takeaway:** It doesn't matter if you start with all 1s, all 0.2s, or any random values. You'll always converge to the same final PageRank values. This is what makes PageRank trustworthy — it's not biased by where you start.

### The Steady-State Equation

When PageRank has converged, multiplying by M doesn't change anything:

$$
M \mathbf{r}^* = \mathbf{r}^*
$$

This literally says: "The score distribution after one round is identical to the score distribution before." The system is at rest. The PageRank vector $\mathbf{r}^*$ is the eigenvector of M with eigenvalue 1.

---

## Part 6 — The Dangling Node Problem & The Damping Fix

### What's a Dangling Node?

A **dangling node** is a page with **no outgoing links**. In our matrix, its entire column is all zeros — it receives coins just fine, but it never passes them on to anyone.

**The problem:** All those coins pile up at the dangling node and are never recirculated. Eventually, all coins in the system pool at dangling nodes and disappear from the rest of the graph. The column no longer sums to 1 — the Markov property breaks — and convergence is no longer guaranteed.

**Real example:** A newly published research paper. It cites nothing yet. Every day, other papers can cite it (it receives rank), but it doesn't cite back (it gives rank to nobody). Without special handling, this breaks PageRank.

---

### The Fix: Teleportation (Damping Factor)

**The idea:** What if the random surfer, instead of always following a link, sometimes just jumps to a completely random page? This prevents them from getting trapped at a dead end.

With **damping factor** $d$ (usually around 0.85):
- With probability $d$: follow a random outgoing link (normal behavior)
- With probability $1-d$: jump to any random page in the entire network

The modified PageRank formula:

$$
PR(v) = \frac{1-d}{n} + d \sum_{u \to v} \frac{PR(u)}{|N^+(u)|}
$$

**Breaking this down:**
- $\frac{1-d}{n}$: a small baseline score that every node gets just for existing (the "teleportation" share)
- $d \sum \ldots$: the standard PageRank contribution from incoming links, but discounted by factor $d$

With $d = 0.85$:
- 85% of your score comes from people who specifically linked to you
- 15% comes from the "jump to random page" effect (spread equally across all $n$ pages)

**What this achieves:**
1. Even dangling nodes now distribute their rank (via the 15% random jump).
2. Every node can now reach every other node (even without a direct link path).
3. The matrix is a valid Markov matrix again.
4. Convergence is guaranteed.

---

## Part 7 — Assignment Case Study Answers

### Case Study 1: Social Media Platform

A social media company tried HITS and PageRank to rank users by influence.

| Question | ✅ Correct Answer | Why |
|---|---|---|
| A user is a strong hub because they... | **Follow many authoritative users** | Hub score = sum of authority scores of who you follow. More + better followees = higher hub score |
| Why did HITS perform poorly on the full graph? | **It is sensitive to irrelevant parts of the graph** AND **it lacks a global notion of importance** | HITS works best on a focused subgraph. On the entire network, unrelated nodes pollute the scores |
| A user is followed by hubs scoring 3 and 5. Authority score? | **8** | $a = 3 + 5 = 8$ |
| Why was PageRank preferred for global ranking? | **Uses the entire link structure** | One consistent calculation over the whole graph |
| What makes PageRank converge? | **Damping factor < 1** AND **handling dangling nodes** | Damping fixes teleportation; dangling node handling restores Markov property |

> ⚠️ **Partial credit trap:** HITS failing has **TWO correct answers**. Writing only one gives you 0.5/1.

---

### Case Study 2: Web Search Engine

A search engine used link analysis to rank billions of webpages.

| Question | ✅ Correct Answer | Why |
|---|---|---|
| HITS is better suited than PageRank for... | **Topic-specific searches** | HITS builds a focused subgraph per query — perfect for focused topics, bad for everything |
| What mechanisms prevent PageRank from getting stuck? | **Random jumps** + **Redistributing rank from dangling nodes** + **Following links most of the time** | All three together ensure valid probability flow at every step |
| A page gets links from pages with PR 0.2, 0.1, 0.3. Total incoming contribution? | **0.6** | $0.2 + 0.1 + 0.3 = 0.6$ (simple addition before damping is applied) |
| Why are dangling nodes a problem? | **They absorb probability mass** | Their column in M is all zeros; scores flow in but never flow out → total drops below 1 |
| Why must probabilities from one page sum to 1? | **To represent a valid random walk** | If probabilities don't sum to 1, the matrix isn't stochastic → no convergence guarantee |

> ⚠️ **Partial credit trap (0.66 trap):** For "mechanisms that prevent PageRank getting stuck," there are THREE correct answers. Missing "following links most of the time" costs you ⅓ of the mark.

---

### Case Study 3: Academic Citation Network

A firm ranked research papers by influence using citation graphs.

| Question | ✅ Correct Answer | Why |
|---|---|---|
| What makes a paper an "authority"? | **Is cited by many influential papers** | Authority score = sum of hub scores of papers that cite you |
| How can someone manipulate HITS scores? | **Creating hub papers that cite many works** AND **excessive self-citations** | HITS is localized — targeted citation spamming can shift hub/authority scores |
| A paper is cited by papers with hub scores of 1.5 and 2.5. Its authority score? | **4.0** | $1.5 + 2.5 = 4.0$ |
| Why is PageRank resistant to manipulation? | **Uses global normalization and damping** | Local cheating barely moves a global score that's spread across millions of nodes |
| Which network properties help PageRank stability? | **High connectivity** AND **presence of hubs** | Connected networks propagate rank quickly; hubs act as fast-spreading relay stations |

> ⚠️ **Partial credit trap:** For stability factors, both "high connectivity" AND "presence of hubs" are correct. Community isolation actually hurts stability (rank gets trapped in isolated clusters).

---

## Part 8 — Formula Cheat Sheet

### HITS Formulas

**Hub update** (for every node v):

$$
h(v) \leftarrow \sum_{\text{nodes } u \text{ that } v \text{ links to}} a(u)
$$

**Authority update** (for every node v):

$$
a(v) \leftarrow \sum_{\text{nodes } u \text{ that link to } v} h(u)
$$

Memory trick: **Hub looks OUT** (sum of authorities it points to). **Authority looks IN** (sum of hubs pointing at it).

### PageRank Formulas

**Basic (no damping):**

$$
PR(v) = \sum_{u \to v} \frac{PR(u)}{|N^+(u)|}
$$

**With damping (the real version):**

$$
PR(v) = \frac{1-d}{n} + d \sum_{u \to v} \frac{PR(u)}{|N^+(u)|}
$$

### Normalization (Bipartite System)

$$
\text{Normalized}(x) = \frac{\text{Score}(x)}{\text{Sum of all scores in same group}}
$$

### Markov Matrix Rule

$$
\text{Every column of M sums to } 1 \quad \Leftrightarrow \quad \text{Total rank is conserved every round}
$$

### Convergence Formula

$$
\mathbf{r}^{(k)} = M^k \mathbf{r}^{(0)} \xrightarrow{k \to \infty} c_1 \mathbf{v}_1 \quad \text{(the dominant eigenvector)}
$$

### Steady State (Convergence Condition)

$$
M \mathbf{r}^* = \mathbf{r}^* \quad \longleftrightarrow \quad \text{"Applying M one more time changes nothing"}
$$

---

## Part 9 — Exam Traps to Watch Out For

> [!WARNING]
> **Trap 1: Mixing up hub and authority update directions**
>
> **Hub update uses authority scores of OUT-neighbors** (the nodes you point to).
> **Authority update uses hub scores of IN-neighbors** (the nodes that point to you).
> Getting this backwards produces completely wrong calculations.

> [!WARNING]
> **Trap 2: Only one answer for "why HITS fails on large graphs"**
>
> There are **two** correct answers: (1) sensitive to irrelevant parts, (2) lacks global notion of importance. The assignment awards 0.5 if you write only one.

> [!WARNING]
> **Trap 3: What's wrong with dangling nodes?**
>
> The answer is: they **absorb probability mass**. They do NOT "reduce authority scores" or "break hub calculations" (those are wrong). The specific problem is that their column in M sums to 0, not 1 — so probability leaks out of the system.

> [!CAUTION]
> **Trap 4: Three mechanisms for PageRank avoiding getting stuck (not two)**
>
> All three are correct: (1) random jumps, (2) redistributing rank from dangling nodes, (3) **following links most of the time**. Leaving out the third costs ⅓ of the marks (you'd get 0.66/1 instead of 1/1).

> [!CAUTION]
> **Trap 5: "Uniform degree distribution" helps PageRank stability**
>
> It does NOT. Uniform distribution means no hubs, which actually slows down rank propagation. The correct answers are **high connectivity** and **presence of hubs**.

> [!NOTE]
> **Good news — convergence:** Both HITS and PageRank (with damping) are mathematically guaranteed to converge regardless of the starting values. You never need to worry about whether they'll converge — they always do.

> [!NOTE]
> **HITS converges but is unstable:** HITS *does* converge, but adding or removing even one node from the graph can shift the converged values dramatically. PageRank is stable to small changes. "HITS converges" and "HITS is stable" are different statements — only the first is always true.

---

## Part 10 — Big Picture Summary

Here's the whole topic in simple terms:

**Recommender Systems** → Two groups (recommenders, resources). Recommenders score high if their resources are good. Resources score high if good recommenders endorse them. Iterate → normalize → repeat until stable.

**HITS** → Same idea, but every node plays BOTH roles (hub and authority). Hub = good pointer. Authority = good destination. They reinforce each other. Works best on small, focused subgraphs.

**PageRank** → Every node has one score. You get score proportional to who links to you, weighted by their score and how selective they are. Works well globally. Needs damping factor to handle dead ends.

**The Maths** → All three are forms of iterated matrix multiplication on a Markov matrix. The scores always converge because the dominant eigenvalue is 1 and all others shrink to zero. The final stable scores are the dominant eigenvector of the transition matrix.

```
Problem: "Who is important in this network?"
   ↓
Model links as a directed graph
   ↓
Build a transition matrix M (columns sum to 1)
   ↓
Start with equal scores r⁰
   ↓
Multiply: rᵏ⁺¹ = M · rᵏ   (repeat ~100-200 times)
   ↓
Scores converge (λ₁=1 dominates, others decay to 0)
   ↓
Final scores = PageRank / HITS authority or hub scores
```

---

> See [`07_PageRank_and_Web_Graph.md`](07_PageRank_and_Web_Graph.md) for worked damping factor calculations and the random walk simulation method.
> See [`code/07_pagerank.py`](code/07_pagerank.py) for the Python implementation.
