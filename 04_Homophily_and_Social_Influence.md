# Homophily and Social Influence

## 1. The Contagion of Happiness

In social networks, emotions and states can flow like a contagion across ties. A famous finding in sociology is that happiness is contagious up to **three levels of degree**. 

If you become happy, the effect ripples outward through the network:
1. **Level 1:** Your friends are more likely to be happy.
2. **Level 2:** Your friends' friends (people you may not even know) are more likely to be happy.
3. **Level 3:** Your friends' friends' friends are more likely to be happy.

Beyond three degrees of separation, the influence generally fades out. This highlights the powerful extent of connectedness—the structure of the network facilitates the flow of emotions across long distances.

**Calculating Total Network Influence:**
Theoretically, the total number of people influenced across three degrees can be estimated by combining the average friends across three network levels (e.g., Level 1 + Level 2 + Level 3 connections). However, calculating this theoretical maximum (e.g. multiplying direct friends × their friends × their friends) often produces a number that **exceeds the population size**. This mathematical overshoot indicates that networks have **substantial overlap and strong network clustering effects**.

---

## 2. Homophily

**Homophily** (literally meaning "love of the same") is the tendency for individuals to associate and bond with similar others. In lay terms: *"birds of a feather flock together."* People tend to be friends with those who share similar characteristics, ages, races, beliefs, or interests.

### Detecting and Measuring Homophily in a Network
Given a network, how do we know if it exhibits homophily, and to what extent? We compare the actual network against a baseline **random mixing model**.

Assume a network has two types of nodes: **Type A** and **Type B**.
- Let $p$ be the fraction of Type A nodes.
- Let $q$ be the fraction of Type B nodes ($p + q = 1$).

If we pick an edge entirely at random, what is the probability it connects two nodes of *different* types (a cross-type edge), assuming no homophily exists? 
The probability of selecting one node of A and one node of B is $p \times q$. Since an edge can be (A-B) or (B-A), the expected probability of a cross-type edge under random mixing is **$2pq$**.

- If the actual fraction of cross-type edges in the network is **significantly less than $2pq$**, the network exhibits **Homophily** (nodes strongly prefer connecting with their own type).
- If the fraction is significantly greater than $2pq$, the network exhibits **Heterophily** (nodes prefer connecting with opposite types).

> **Example:** 
> Suppose a high school consists of 60% boys ($p = 0.6$) and 40% girls ($q = 0.4$). 
> Under random link formation, the expected fraction of boy-girl friendships is $2 \times 0.6 \times 0.4 = \mathbf{0.48}$ (or 48%). 
> If we map the actual friendship network and find that only **10%** of friendships cross gender lines, this network exhibits very strong homophily (10% is much less than the expected 48%).

### The Homophily Coefficient
We can quantify the exact strength of homophily in a network using the **Homophily Coefficient**:

$$
\text{Homophily Coefficient} = 1 - \frac{\text{Actual Cross-Type Friendships}}{\text{Expected Cross-Type Friendships}}
$$

**Case Study Validations:**
1. **Majors:** If random formation is expected to produce 208 cross-major friendships (e.g., CS vs Business students), but only 78 exist in reality, the coefficient is $1 - (78 / 208) = 1 - 0.375 = \mathbf{0.625}$.
2. **Gender:** If we observe 60 platonic cross-gender friendships but expect 118 based on random mixing, the coefficient is $1 - (60 / 118) = \mathbf{0.49}$.

---

## 3. Selection vs. Social Influence

When we observe homophily in a network (friends are similar to each other), it is primarily driven by two distinct processes:

1. **Selection:** We choose to form ties with people because they are *already* similar to us. (Similarity $\rightarrow$ Friendship).
2. **Social Influence:** We become *more* similar to our friends over time because we interact with them. (Friendship $\rightarrow$ Similarity).

**The Big Question:** In a given network, what proportion of friendships formed due to selection, and what proportion is driven by social influence? To untangle this, researchers investigate the timeline of interactions.

### The Wikipedia Dataset Research
To answer this question, researchers analyzed a vast dataset of Wikipedia editors, mapping out *who talks to whom* and *how similar the topics they edit are*.

The findings clearly separated the two mechanisms along a timeline:
- **Selection:** Editors initiated conversations because they were already similar (they were editing articles on similar topics, which gave them a reason to talk in the first place).
- **Social Influence:** *After* they started talking, they continually influenced each other over time, gradually editing even more overlapping articles and becoming increasingly similar.

### Defining a Similarity Measure
To quantify the above phenomena, we need a mathematical measure of similarity between two individuals. A straightforward approach is to evaluate the overlap in their interests or traits.

**Example: Jaccard Similarity**  
For the Wikipedia dataset, similarity between Editor A and Editor B can be defined by the ratio of the intersection of their edited articles to the union of their edited articles:

$$
\text{Similarity}(A, B) = \frac{| \text{Articles edited by A} \cap \text{Articles edited by B} |}{| \text{Articles edited by A} \cup \text{Articles edited by B} |}
$$

If Editor A edits exactly the same set of articles as Editor B, the similarity is 1. If they edit completely distinct sets, the similarity is 0.

### Quantifying the Magnitude of Effects
By tracking a network longitudinally, we can calculate the exact proportion driven by each mechanism:
- **Selection Effect Magnitude** = (Similarity at First Interaction) - (Baseline Pre-Interaction Similarity)
- **Social Influence Effect Magnitude** = (Final/Plateau Similarity) - (Similarity at First Interaction)

*Example:* If a baseline similarity is $0.14$, spikes to $0.31$ at first interaction, and plateaus at $0.48$ after a year:
- Selection Effect = $0.31 - 0.14 = \mathbf{0.17}$
- Social Influence Effect = $0.48 - 0.31 = \mathbf{0.17}$
- **Ratio** = $0.17 / 0.17 = \mathbf{1.00}$ (meaning both mechanisms contribute equally).

To determine whether cross-group friendships result from selection or influence, researchers examine similarity measures of pairs before and after friendship. A steep pre-interaction increase indicates Selection.

### Friendship Pathways:
- Pairs with **High Initial Similarity** follow a **selection-dominated** formation pathway.
- Pairs with **Low Initial Similarity** (who converge to high similarity eventually) demonstrate an **influence-dominated** formation pathway.
*Example of pure influence:* If 89% of new coffee drinkers already had at least two coffee-drinking friends prior to adopting the habit, it suggests habit adoption via social exposure.

---

## 4. Closure Mechanisms

How does a network naturally evolve to close triangles and form closely-knit clusters? This happens through different types of "closures":

1. **Triadic Closure:** If node A and node B share a common friend, C, they are highly likely to become friends themselves over time.
2. **Focal Closure:** Two people who share a common *focus* or activity (e.g., attending the same club, working at the same company) are more likely to become friends. The focus acts as a bridge between strangers.
   - *Example:* Two strangers, Alice and Bob, both attend the local Friday chess club. Because of this shared focal point, they are extremely likely to become friends.
3. **Membership Closure:** A person is more likely to join a new group, activity, or focus if they already have a friend who is a member of it.
   - *Example:* Charlie plays tennis every weekend, but his friend Dave currently does not. Because of Charlie's membership, Dave is socially influenced and is highly likely to eventually join the tennis club himself.

### Quantifying the Effect of Triadic Closure
If user B and user C have $k$ common friends, what is the exact probability of them becoming friends?

Sociological data indicates that the probability of forming a link increases as the number of common friends $k$ increases, but it comes with **diminishing marginal returns**. 
- Acquiring your 1st common friend significantly increases the chance of creating a tie.
- Going from 10 to 11 common friends adds very little extra probability compared to going from 0 to 1.

Empirically, the probability $P(k)$ often behaves somewhat like:

$$
P(k) \propto 1 - (1 - p)^k
$$

Where $p$ is the baseline probability that any single common friend successfully introduces B and C.

---

## 5. The Evolutionary Fatman Model (Code)

To rigorously model how attributes like Body Mass Index (BMI) evolve alongside network topology, researchers use the **Fatman Evolutionary Model**. 

### 1. Node Types & Visualization
- **Person Nodes:** Visualized in blue. Size is proportional to BMI ($\text{Size} = \text{BMI} \times 20$). *Purpose:* Demonstrates homophily visually by making similarly-sized nodes more likely to connect.
- **Social Foci Nodes:** Visualized in red with fixed size ($1000$). 
*(Note: For a person with BMI 32, their size is 640. The ratio of foci size to this person size is $1000 / 640 = \mathbf{1.56}$.)*

### 2. Homophily Probability Formula
The probability of a friendship forming through homophily is based on BMI similarity:

$$
P(u,v) = \frac{1}{|BMI_u - BMI_v| + 1000}
$$

*Why add 1000?* It ensures probability remains inversely proportional to BMI diff, prevents division by zero, and scales probabilities down to allow for gradual network evolution.
*(Example: For BMIs 22 and 28, diff is 6, probability is $1/1006 \approx \mathbf{0.00099}$)*

### 3. Closure Probability Formula
The probability of forming a connection through closure is:

$$
P(\text{connection}) = 1 - (1 - p)^k
$$

- **$k$** represents the **total number of common neighbors** (combining mutual friends AND shared social foci).
- Because $k$ accounts for both, **Triadic Closure** and **Focal Closure** are captured by the *exact same formula*.
- **Membership Closure** occurs between a person and a social focus when they share a common person neighbor. 
- *Constraints:* At least one of the connecting nodes must be a Person node. Closure cannot physically happen between two Foci nodes.
*(Example: If $k=3$ and $p=0.1$, $P = 1 - (1 - 0.1)^3 = 1 - 0.729 = \mathbf{0.271}$)*

### 4. Tracking Social Influence Indirectly
Social influence is modeled **indirectly** through the mechanism of shared contexts (Social Foci), rather than direct peer-to-peer numerical averaging.
- *Example:* When membership closure causes an individual to enroll in a gym (due to a friend), the individual begins losing weight (BMI drops by 1 point per iteration, bounded between 15 and 40). This demonstrates social influence via shared context.
- What if Person X's friend Person Y goes to an eat-out restaurant, and X starts going too and gains BMI? This full sequence is: **Membership Closure** (X learns about the restaurant from Y) $\rightarrow$ **Social Influence** (X adopts the habit of going there and their BMI increases).

### 5. Graph Dynamics and Snapshots
- **Edge Persistence:** In this model, new edges only arrive with time; **existing edges are never deleted**. The theoretical implication is that network density monotonically increases, potentially masking the dynamic effects of social influence on attribute changes.
- **Data Storage:** The model generates and saves network snapshots in separate **GML files** at each time step (rather than continuously updating one file). Separate snapshots preserve complete evolution history, enabling retrospective analysis of density changes and obesity patterns across time.
- **Edge Math:** If the simulation starts with 100 people and 5 foci (each person perfectly assigned 1 focus $\rightarrow$ 100 initial edges). If Focal Closure adds 45 edges and Membership Closure adds 30 edges, the total edges = $100 + 45 + 30 = \mathbf{175}$.

> The fully commented source code simulating these abstract principles is available in: [`code/04_fatman_model.py`](code/04_fatman_model.py).
