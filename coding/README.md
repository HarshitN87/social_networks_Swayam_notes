# Coding Folder: NetworkX Examples

This folder contains corrected Python code for the graph concepts in the notes.

## Files

| File | Purpose |
|---|---|
| `networkx_intro.py` | Introduces basic NetworkX graph functions with comments. |
| `emergence_of_connectedness.py` | Simulates random edge addition until a graph becomes connected. |
| `community_bruteforce.py` | Implements a corrected brute-force two-community search for small graphs. |
| `community_girvan_newman.py` | Implements community detection using NetworkX's Girvan-Newman algorithm. |

## Setup

Install NetworkX if it is not already available:

```bash
pip install networkx
```

Then run any file:

```bash
python coding/networkx_intro.py
```

> **Note:** The brute-force community script is only appropriate for very small graphs because the number of possible partitions grows extremely quickly.

