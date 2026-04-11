# Granovetter and the Strength of Weak Ties

## The Main Idea

Mark Granovetter's famous argument, known as the **strength of weak ties**, explains why acquaintances can be surprisingly valuable in social networks.

The rough observation is:

> People often hear about jobs, opportunities, and new information from acquaintances rather than from their closest friends or family.

This does **not** mean close friends are unimportant. Instead, it means close friends often live in social worlds similar to ours, while acquaintances may connect us to different circles.

---

## Why Weak Ties Matter

Close friends usually have high overlap with us:

- They may know the same people.
- They may hear the same news.
- They may belong to the same neighborhood, school, workplace, or online circle.

Weak ties, such as acquaintances or distant relatives, are often connected to different parts of the network. Because of this, they can bring:

- Job referrals
- New ideas
- Invitations to unfamiliar communities
- Access to different social or professional circles
- Information that has not already circulated among our close friends

> **Key insight:** Weak ties are powerful because they often act as bridges between otherwise separated social worlds.

---

## Triads and Triadic Closure

A **triad** is a set of three people or nodes. Suppose you know `A` and `B`.

If `A` and `B` do not know each other, the triad is open:

```text
You -- A
 |
 B
```

If `A` and `B` also know each other, the triad is closed:

```text
You -- A
 |    /
 B --
```

This process is called **triadic closure**.

### Why Triadic Closure Happens

Triadic closure is common because:

1. Mutual friends create opportunities to meet.
2. Trust is easier when a shared friend exists.
3. People with common social contexts often share interests.
4. Social events naturally bring friends-of-friends together.

---

## Clustering Coefficient

The **clustering coefficient** measures how connected your friends are to each other.

For a person `v`, the local clustering coefficient is:

```text
number of edges among v's friends / number of possible edges among v's friends
```

If `v` has `d` friends, the maximum possible number of edges among those friends is:

```text
d(d - 1) / 2
```

So:

```text
clustering coefficient = actual friend-friend edges / possible friend-friend edges
```

| Value | Meaning |
|---|---|
| `1` | All of your friends are friends with each other. |
| Near `0` | Very few of your friends know each other. |
| `0` | None of your friends know each other. |

> **Correction:** The raw note said "if it not 0 then none of them are friends." The precise statement is: if the clustering coefficient is `0`, none of the friends are connected to each other. If it is nonzero, at least one pair of friends is connected.

---

## Clustering and Social Support

Some sociological studies have observed that people at risk of social isolation or mental-health distress may have lower local clustering or weaker embedded support structures. This should be interpreted carefully:

- Network measures can reveal patterns of social support.
- They do not, by themselves, diagnose individual mental-health outcomes.
- Human behavior is shaped by many factors beyond graph structure.

> **Careful interpretation:** A low clustering coefficient may indicate fewer mutually reinforcing social ties, but it should never be treated as a complete explanation of serious outcomes such as suicide.

---

## Neighborhood Overlap and Embeddedness

The **neighborhood overlap** of an edge between two people `A` and `B` measures how many mutual friends they share relative to their total neighborhood.

A common version is:

```text
neighborhood overlap(A, B)
= common neighbors of A and B / neighbors of A or B, excluding A and B themselves
```

In simpler words:

> It measures how embedded the relationship is in a shared social circle.

### Embeddedness

**Embeddedness** is often described as the number of common friends shared by two connected people.

Higher embeddedness often suggests:

- Stronger social reinforcement
- More trust
- More shared context
- More stable relationships

However, high embeddedness is not always better. If all of your friendships are highly embedded, you may be trapped in one social circle and miss information from outside communities.

---

## Bridges, Local Bridges, and Weak Ties

A **bridge** is an edge whose removal disconnects the graph.

If two groups are connected by exactly one edge, that edge is a bridge:

```text
Group 1 -- bridge -- Group 2
```

Removing it separates the two groups.

A **local bridge** is weaker than a full bridge. An edge is a local bridge if its endpoints have no mutual friends. In other words, it is not part of any triangle.

| Concept | Meaning |
|---|---|
| Bridge | Removing the edge disconnects the graph. |
| Local bridge | The endpoints have no shared neighbor; the edge is not part of a triangle. |
| Weak tie | A social connection that is not deeply embedded in a shared friend group. |

Local bridges are often weak ties, and weak ties are often useful because they connect different social regions.

---

## Strong Triadic Closure

The principle of **strong triadic closure** says:

> If `A` has strong ties to both `B` and `C`, then there is pressure for `B` and `C` to become connected.

This does not mean the `B-C` relationship must always exist. It means it is socially likely because:

- `A` may introduce them.
- They may meet repeatedly through `A`.
- Trust may transfer through their shared strong connection.

If `A` has strong ties to `B` and `C`, but `B` and `C` are not connected, then the network contains a structurally important open triad.

---

## Empirical Validation with Phone Data

Large-scale communication data, such as mobile-phone call records, has been used to test ideas related to Granovetter's hypothesis.

Researchers often use proxies such as:

- Call duration
- Call frequency
- Reciprocation
- Number of mutual contacts
- Whether an edge acts like a bridge or local bridge

The general pattern supports the theory:

> Ties with higher communication intensity tend to be more embedded and less likely to act as local bridges.

In other words, strong ties often sit inside dense clusters, while weak ties are more likely to connect separate parts of the network.

---

## Online Relationships

Social media creates multiple kinds of relationships:

| Relationship Type | Description |
|---|---|
| Passive engagement | You do not directly communicate, but you still know what is happening in someone's life. |
| One-way relationship | One person sends messages or attention, but the other rarely responds. |
| Reciprocal relationship | Both people communicate with each other. |
| Maintained relationship | People remain lightly connected through likes, views, comments, or occasional reactions. |

Many social-media relationships are **maintained relationships**: they are not deep friendships, but they keep a weak connection alive.

---

## Closure, Brokerage, and Social Capital

Social capital refers to the value created by a person's position in a social network.

Two important mechanisms are **closure** and **brokerage**.

### Closure

Closure means that friends-of-friends become friends. It creates:

- Trust
- Cooperation
- Social support
- Shared norms

### Brokerage

Brokerage means connecting people or groups that do not already share mutual friends. It creates:

- Access to new information
- Innovation
- Opportunity flow
- Cross-community coordination

| Mechanism | Strength | Risk |
|---|---|---|
| Closure | Builds trust and support. | Can become redundant or insular. |
| Brokerage | Brings novel information and opportunities. | Can be fragile if trust is low. |

> A healthy social network usually needs both closure and brokerage: enough dense ties for trust, and enough bridging ties for new information.

---

## Summary

- Weak ties are valuable because they connect us to different social worlds.
- Triadic closure explains why friends-of-friends often become friends.
- Clustering coefficient measures how connected a person's friends are to each other.
- Embeddedness measures how many shared social contexts a tie has.
- Bridges and local bridges often represent important weak ties.
- Strong triadic closure predicts that if two people share a strong mutual friend, they are more likely to form a tie.
- Closure builds trust; brokerage brings novelty and opportunity.

