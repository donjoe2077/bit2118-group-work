"""Task 09 extension - eigenvalues and eigenvectors.

PART 1: add one link (A-D) to the original network and see how importance changes.
PART 2: new case - PageRank of five web pages (directed links, damping factor 0.85).
The tiny link structure is ASSUMED.
"""
import numpy as np

# ---------------- PART 1: parameter change ----------------
base = np.array([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]], dtype=float)
more = base.copy()
more[0, 3] = more[3, 0] = 1.0       # new link between A and D


def centrality(adj):
    vals, vecs = np.linalg.eig(adj)
    i = np.argmax(vals.real)
    v = np.abs(vecs[:, i].real)
    return vals.real[i], v / v.sum()


print("PART 1 - adding a link between A and D")
for name, adj in (("original", base), ("with A-D link", more)):
    lam, c = centrality(adj)
    print(f"{name:>14}: dominant eigenvalue={lam:.4f}, importance A,B,C,D = {np.round(c, 4)}")
print()

# ---------------- PART 2: new case ----------------
pages = ["Home", "News", "Blog", "Shop", "Contact"]
links = {0: [1, 2], 1: [2], 2: [0], 3: [2, 4], 4: [3]}   # page -> pages it links to
n = len(pages)

M = np.zeros((n, n))                    # column j spreads page j's score across its links
for j, outs in links.items():
    for i in outs:
        M[i, j] = 1.0 / len(outs)


def pagerank(d):
    G = d * M + (1 - d) / n * np.ones((n, n))
    vals, vecs = np.linalg.eig(G)
    k = np.argmax(vals.real)
    v = np.abs(vecs[:, k].real)
    return vals.real[k], v / v.sum(), G


print("PART 2 - PageRank")
for d in (0.85, 0.5):
    lam, pr, G = pagerank(d)
    print(f"damping {d}: dominant eigenvalue={lam:.4f}")
    for p, s in sorted(zip(pages, pr), key=lambda t: -t[1]):
        print(f"   {p:<8}{s:.4f}")

# Cross-check with power iteration (repeated multiplication)
_, pr_eig, G = pagerank(0.85)
v = np.ones(n) / n
for _ in range(100):
    v = G @ v
print("Power iteration matches eigenvector:", np.allclose(v, pr_eig, atol=1e-8))
