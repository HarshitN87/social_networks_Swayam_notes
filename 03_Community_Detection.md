# Community Detection

## What is a Community?
In a graph, a community is fundamentally defined as a distinct subset of nodes that are highly connected to each other, but hold very few connections pointing to the exterior rest of the network.

A "valid partitioning" of a graph maximizes:
- **Intra-community connections**: High (many edges residing safely inside the defined group)
- **Inter-community connections**: Low (few edges pointing outside the group)

![alt text](image3.png)

## How to Determine Communities in a True Graph?
To successfully identify independent communities, we naturally search for the weak points of a graph. If we locate and aggressively disconnect the edges holding independent groups together, the graph will inevitably shatter into its isolated true communities. 

But how do we methodically find these edges? We analyze their "flow" and centrality.

### What is Edge Betweenness? *(Requested Definition)*
**Edge Betweenness Centrality** is defined structurally as the number of **shortest paths** that pass through a particular target edge in the network.

Imagine all nodes trying to communicate with each other using the single most efficient route. An edge that securely connects two massive but completely distinct communities acts as an indispensable funnel. Every shortest path spanning Community 1 to Community 2 *must* forcibly flow across this single edge bridge. 

Therefore, edges acting as community bottlenecks yield phenomenally high **betweenness** values.

## Girvan-Newman Algorithm
The Girvan-Newman algorithm automates community detection elegantly using edge betweenness:
1. Dynamically calculate the edge betweenness centrality for every edge currently active in the graph.
2. Identify the singular edge holding the **highest betweenness score**.
3. **Remove** that edge from the system.
4. Immediately recalculate betweenness for all remaining edges (since traffic will now naturally divert to novel paths).
5. Repeat steps 2-4 systematically until the graph completely fragments into disconnected components (representing the respective communities).
