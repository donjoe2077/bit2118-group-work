# Task 09 – Eigenvalues and Eigenvectors

**Concept:** Av = λv; an eigenvector keeps its direction under A and is scaled by λ.
**Code:** `code/Task_09_eigenvalues.py` · **Extension:** `extensions/Task_09_ext_pagerank.py`

## B. Inputs and mathematical operations
- **Input:** adjacency matrix of a 4-node network (A–B, A–C, B–C, B–D, C–D).
- **Operations:** `np.linalg.eig`, pick the largest eigenvalue, normalise its eigenvector to sum to 1 (importance), check ‖Av − λv‖.

## Output of the original program
```
All eigenvalues: [ 2.5616 -0.     -1.5616 -1.    ]
Dominant eigenvalue: 2.561552812808829
A: 0.2192   B: 0.2808   C: 0.2808   D: 0.2192
Verification error: 1.5e-15
```

## C. Changing an input
Adding a link between A and D turns the network into a complete graph (every node linked to every other). The dominant eigenvalue becomes exactly 3 and all four nodes get importance 0.25: with identical connections nobody is more influential.

## D. Interpretation
B and C connect to three nodes each, so they score highest (0.2808); A and D connect to two (0.2192). The verification error near 1e-15 proves the vector satisfies Av = λv. A larger dominant eigenvalue means a more densely connected network.

## E. New case – PageRank of five web pages
- **Assumptions:** pages Home, News, Blog, Shop, Contact; links Home→News,Blog; News→Blog; Blog→Home; Shop→Blog,Contact; Contact→Shop; damping factor 0.85 (a surfer follows a link 85 % of the time).
- **Method:** build the Google matrix and take the eigenvector of eigenvalue 1; checked by repeated multiplication (power iteration).
- **Output (d = 0.85):** Blog 0.3498, Home 0.3273, News 0.1691, Shop 0.0869, Contact 0.0669. With d = 0.5 the scores even out (Blog 0.2835 … Contact 0.1429).
- **Interpretation:** Blog ranks first because three pages point to it. Lower damping adds more random jumping, which flattens the ranking. Power iteration matches the eigenvector solution.
