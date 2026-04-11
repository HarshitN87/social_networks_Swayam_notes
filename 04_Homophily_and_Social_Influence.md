# Homophily and Social Influence

## 1. The Contagion of Happiness

In social networks, emotions and states can flow like a contagion across ties. A famous finding in sociology is that happiness is contagious up to **three levels of degree**. 

If you become happy, the effect ripples outward through the network:
1. **Level 1:** Your friends are more likely to be happy.
2. **Level 2:** Your friends' friends (people you may not even know) are more likely to be happy.
3. **Level 3:** Your friends' friends' friends are more likely to be happy.

Beyond three degrees of separation, the influence generally fades out. This highlights the powerful extent of connectedness—the structure of the network facilitates the flow of emotions across long distances.

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

$$ \text{Similarity}(A, B) = \frac{| \text{Articles edited by A} \cap \text{Articles edited by B} |}{| \text{Articles edited by A} \cup \text{Articles edited by B} |} $$

If Editor A edits exactly the same set of articles as Editor B, the similarity is 1. If they edit completely distinct sets, the similarity is 0.

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
$$ P(k) \propto 1 - (1 - p)^k $$
Where $p$ is the baseline probability that any single common friend successfully introduces B and C.

---

## 5. The Evolutionary Fatman Model (Code)

To tie together **Selection**, **Social Influence**, and **Closure**, we can implement an evolutionary network model (often referred to in computational social science as the "Fatman Evolutionary Model", simulating the contagion of BMI/obesity markers or fitness behavior).

In this Python model:
1. People select friends with similar fitness levels (Selection).
2. People form new friendships because of common friends (Closure).
3. People's fitness levels adjust to match the average of their friends (Social Influence).

> The fully commented source code is available in: [`code/04_fatman_model.py`](code/04_fatman_model.py).

