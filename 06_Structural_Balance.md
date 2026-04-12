# Structural Balance Theory

## 1. Introduction to Signed Complete Graphs

To model faction dynamics — in workplaces, friend groups, or international diplomacy — we represent relationships as a **complete signed network**: every pair of nodes is connected, and every connection carries either a positive ($+$) or negative ($-$) sign. Positive ties mean friendship or alliance; negative ties mean hostility or enmity.

## 2. Triadic Stability: The Psychological Tension

The fundamental unit of analysis is the **triangle** — any three nodes and the three edges connecting them. There are exactly four possible sign combinations, and each is either stable or unstable based on a simple psychological rule.

![alt text](images/image14.png)

The quick rule for stability: **count the negative edges**. A triangle is stable if it has 0 or 2 negatives — never 1 or 3. The "friend of my friend" and "enemy of my enemy" principles are both satisfied. With 1 negative ($+ + -$), one person is caught between two enemies they both like — the "choose me" pressure. With 3 negatives ($- - -$), all three hate each other, but two will inevitably recognize a shared opponent and flip one edge to positive.

---

## 3. The Balance Theorem

These local triadic rules produce a remarkable global consequence. If a complete signed graph contains **zero unstable triangles**, the entire network must split into exactly one or two groups.

![alt text](images/image15.png)

Inside each faction, every pair is friends (all green). Across the divide, every pair is enemies (all red dashed). Any triangle you draw will either be entirely within one faction ($+ + +$) or straddle the divide with exactly two members from one side ($+ - -$). Both are stable — zero unstable triangles anywhere. This is why large conflicts are almost always **bipolar** rather than three-way: a three-way mutual hostility ($- - -$) is unstable and rapidly collapses into two sides.

For the case study: a company of 30 splitting into Faction A (18) vs Faction B (12) produces:

$$
18 \times 12 = 216 \text{ negative edges}
$$

---

## 4. The Proof of the Balance Theorem

How do we *prove* any balanced complete graph must produce exactly two factions? The argument is elegant — you only need to pick one node and let logic do the rest.

![alt text](images/image16.png)

The proof works in three forced steps:

**Step 1 — Inside Team A:** X is friends with both Y and Z. If Y and Z were enemies, triangle X-Y-Z would be ($+ + -$) — unstable. So Y and Z *must* be friends. Team A is universally positive internally.

**Step 2 — Inside Team B:** X is enemies with both U and V. If U and V were also enemies, triangle X-U-V would be ($- - -$) — unstable. So U and V *must* be friends. Team B is also universally positive internally.

**Step 3 — Across teams:** X is friends with Y ($+$) and enemies with U ($-$). If Y and U were friends, triangle X-Y-U would be ($+ + -$) — unstable. So Y and U *must* be enemies. All cross-faction edges are negative.

Since X was chosen arbitrarily, this logic applies from any starting node. The result is always the same: two clean hostile camps with no exceptions.

---

## 5. Identifying Coalitions in Code

Given a finalized stable graph, extracting the two factions is a simple modified BFS:

![alt text](images/image17.png)

The BFS terminates with two perfectly separated coalitions. Because the graph is structurally balanced, the algorithm never encounters a contradiction — no node will be assigned to both coalitions simultaneously. The guarantee from the theorem ensures this will always cleanly resolve into exactly two groups.

> The full Python implementation — building the complete signed graph, iteratively resolving unstable triangles, and extracting the two factions — is in `code/06_structural_balance.py`.
