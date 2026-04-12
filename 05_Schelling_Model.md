
# The Schelling Segregation Model

## 1. How Do We Decide to Choose a House?

In reality, people often state that they don't want to live in fully segregated neighborhoods. They simply want *at least a few* neighbors who share their background — not isolation, not uniformity. The **Schelling Segregation Model** proved something startling: even these modest, tolerant preferences reliably produce *extreme* global segregation. No racist policy required.

### The Rules of the Grid

Imagine a city as an N×N grid. Each cell is either **Type A**, **Type B**, or **Empty**. Every household looks at its 8 surrounding cells and evaluates a single question: *do I have enough same-type neighbors?*

The **Similarity Threshold (t)** is the minimum number of same-type neighbors needed to feel satisfied. If a household has fewer than t same-type neighbors, it becomes unhappy and relocates to a randomly chosen empty cell.
![alt text](images/image9.png)
The green-bordered cell is you (Type A). You scan your 8 orange-bordered neighbors and count 3 same-type (A) neighbors. If your threshold t = 3, you stay. If t = 4, you pack up and move — even though 3 out of 8 is a pretty tolerant 37.5% preference.

---

## 2. Grid Geometry and Neighbors

Not all cells have 8 neighbors. Position on the grid determines how many neighbors a cell can even *have* — and this creates hard mathematical ceilings for satisfaction at boundary positions.
![alt text](images/image.png)
The dashed lines represent the grid boundary — there is no cell beyond them. This creates a hard constraint: **a corner cell can never have more than 3 neighbors**, so setting t ≥ 4 makes it *mathematically impossible* for that cell to ever be satisfied. In a 10×10 grid, 4 corners + 32 edge cells = **36 out of 100 cells** are boundary-constrained.

---

## 3. The Ripple Effect of Relocation

When a single household moves, the satisfaction calculations of many others are immediately affected. This is what makes the model cascade so rapidly.
![alt text](images/image11.png)
One move triggers recalculations for: the mover itself (1) + up to 8 old neighbors + up to 8 new neighbors = **maximum 17 households** whose satisfaction status changes from a single decision. This is why the model cascades — each relocation destabilizes the surrounding cells, potentially triggering further moves in a chain reaction.

---

## 4. Is Homophily Inevitable? (The Checkerboard Paradox)

Extreme segregation is *not* mathematically inevitable. We can construct stable, perfectly integrated states — they're just nearly impossible to stumble upon through random movement.

The most elegant example is the **checkerboard configuration**:
![alt text](images/image12.png)
The geometry is elegant: in a checkerboard, the 4 orthogonal neighbors (up, down, left, right) are always the *opposite* type, while the 4 diagonal neighbors are always the *same* type. Every interior cell sits at exactly 4 same-type neighbors — perfectly balanced.

This layout is stable as long as t ≤ 4. The moment t = 5, *every single cell simultaneously* falls below its threshold. The whole grid shatters at once. There is no partial instability — it's a phase transition.

The crucial insight is this: the checkerboard is not unreachable because it's impossible, but because random moves will almost never produce it. Stumbling into this perfectly ordered state by accident is like shuffling a deck and drawing cards in perfect suit order — technically possible, practically never.

---

## 5. Threshold Variances and Convergence

The threshold t doesn't just control *how much* segregation occurs — it controls *how fast* the model converges and *how extreme* the final outcome is.
![alt text](images/image13.png)
The three panels capture the model's core surprise. At t = 2, even a very tolerant 25% preference produces *some* visible clustering. At t = 3, just 37.5% preference reliably produces **large distinct blocs** — more segregation than most individuals would say they wanted. At t = 6, the grid fractures into hard-edged territorial divides with a sharp boundary, and takes far longer to stabilize because finding a location with 6 same-type neighbors out of 8 is geometrically difficult until the clusters are already very large.

---

## The Core Takeaway

The Schelling model stands as one of the most elegant demonstrations in social science: **local micro-motives organically produce global macro-structures that no individual intended or chose.**

Nobody in the model is explicitly a segregationist. Nobody wants total homogeneity. Yet the aggregate outcome — driven purely by the ripple effects of individually modest preferences — is a world that looks deeply and deliberately divided. The integrated checkerboard exists in mathematics, but the segregated city emerges from reality.

> The fully executable Python simulation is available in `code/05_schelling_model.py`.