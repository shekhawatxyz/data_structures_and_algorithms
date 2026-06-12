# Graph Programming Challenges

_Problems: 60._

A graduated sequence. Each level introduces a single new conceptual wrinkle on top of what came before. Sub-problems within a level explore that wrinkle from different angles — pick what stretches you; you don't have to do all of a–d.

---

## Conventions

- Vertices are labelled `0` to `n-1` unless a problem says otherwise.
- Default representation is the adjacency list: `list[list[int]]` for unweighted, `list[list[tuple[int, int]]]` for weighted (each entry is `(neighbour, weight)`).
- For directed graphs, `adj[u]` contains only successors of `u`. For undirected, both directions are present.
- "Graph" means simple graph (no self-loops, no parallel edges) unless stated otherwise.

---

## Level 1 — Representation

The graph as a thing that lives in memory.

- [ ] **1a — `build_adjacency_list`** — Status:

Build an adjacency list from a list of edges and a vertex count.
```python
def build_adjacency_list(n: int, edges: list[tuple[int, int]], directed: bool) -> list[list[int]]
```

- [ ] **1b — `build_adjacency_matrix`** — Status:

Same input, but output is an `n × n` matrix.
```python
def build_adjacency_matrix(n: int, edges: list[tuple[int, int]], directed: bool) -> list[list[int]]
```

- [ ] **1c — `adjlist_to_matrix` and `matrix_to_adjlist`** — Status:

Convert between the two representations. Two functions.

- [ ] **1d — `edges_from_adjlist`** — Status:

Produce the canonical edge list back out of an adjacency list. For undirected graphs each edge appears exactly once in the result.

---

## Level 2 — Basic queries

Reading a graph without modifying it.

- [ ] **2a — `degree_sequence`** — Status:

Return a list where index `i` is the degree of vertex `i`. For directed graphs, return `(in_degree, out_degree)` tuples.

- [ ] **2b — `has_edge`** — Status:

Given a representation and `(u, v)`, return whether the edge exists. Implement for both adjacency list and matrix; note the cost difference.

- [ ] **2c — `is_simple`** — Status:

Return whether the input graph (which may have been given carelessly) has no self-loops and no parallel edges.

- [ ] **2d — `two_hop_neighbours`** — Status:

Return the set of vertices `u ≠ v` such that there exists some `w` with `v–w` and `w–u` both edges. The bridge between query and traversal — neighbours-of-neighbours, no visited state needed yet.

---

## Level 3 — Mutation

The graph changes.

- [ ] **3a — `add_edge` and `remove_edge`** — Status:

Maintain adjacency-list representation under edge mutations. For undirected, both endpoints' lists update.

- [ ] **3b — `remove_vertex`** — Status:

Remove vertex `v` and every edge incident to it. Decide: do you renumber the remaining vertices, or leave a tombstone? Both are defensible — make the choice deliberately.

- [ ] **3c — `reverse_directed_graph`** — Status:

Given a directed graph, return its reverse: every edge flipped.

- [ ] **3d — `complement_graph`** — Status:

For a simple undirected graph, return its complement: an edge in the result iff there is no edge in the input (excluding self-loops).

---

## Level 4 — Depth-first search

Visiting every reachable vertex, systematically.

- [ ] **4a — `reachable_from`** — Status:

Return the set of vertices reachable from source `s`. Implement once recursively, once iteratively (with an explicit stack). The two should agree.

- [ ] **4b — `dfs_path`** — Status:

Return *any* path from `s` to `t`, or `None` if none exists.

- [ ] **4c — `count_components`** — Status:

Number of connected components in an undirected graph. Repeated DFS from each unvisited vertex.

- [ ] **4d — `component_labels`** — Status:

Return a list where `label[i]` is the component ID of vertex `i`. Assign IDs `0, 1, 2, …` in order of discovery.

---

## Level 5 — Breadth-first search

Layer by layer.

- [ ] **5a — `bfs_distances`** — Status:

Return `dist` where `dist[v]` is the shortest path length (in edges) from `s` to `v`, or `-1` if unreachable.

- [ ] **5b — `bfs_path`** — Status:

Return the shortest (fewest-edges) path from `s` to `t`, or `None`. Reconstruct using parent pointers.

- [ ] **5c — `bfs_layers`** — Status:

Return `layers` where `layers[k]` is the list of all vertices exactly `k` edges away from `s`.

- [ ] **5d — `multi_source_bfs`** — Status:

Given a set of sources `S`, return for each vertex its distance to the *nearest* source. The trick is in the initialisation.

---

## Level 6 — Cycles

Detection, finding, classifying.

- [ ] **6a — `has_cycle_undirected`** — Status:

Return `True` iff the undirected graph contains a cycle. Subtle point: how do you avoid a false positive on the parent edge during DFS?

- [ ] **6b — `has_cycle_directed`** — Status:

Return `True` iff the directed graph contains a cycle. The technique is genuinely different from 6a — DFS with three states (unvisited, in-progress, finished); a back-edge is the witness.

- [ ] **6c — `find_cycle_directed`** — Status:

Return one cycle as a list of vertices, or `None` if the graph is acyclic.

- [ ] **6d — `count_back_edges`** — Status:

During a DFS run on a directed graph, count the back edges. A primer for full edge classification later.

---

## Level 7 — Topological order

Linearising a DAG.

- [ ] **7a — `topological_sort_dfs`** — Status:

Return a topological order of a DAG, computed via DFS post-order reversal. Raise an error if the input has a cycle.

- [ ] **7b — `topological_sort_kahn`** — Status:

Same problem, computed via Kahn's algorithm: start from in-degree-zero vertices, process and remove, repeat.

- [ ] **7c — `is_dag`** — Status:

Return `True` iff the directed graph is acyclic. (Either approach above will do; or reuse `has_cycle_directed`.)

- [ ] **7d — `longest_path_in_dag`** — Status:

Length of the longest path in a DAG. The whole graph is the search space — but processed in the right order, the DP is one pass.

---

## Level 8 — Colouring and bipartiteness

Constraints propagating during traversal.

- [ ] **8a — `is_bipartite`** — Status:

Return `True` iff the undirected graph admits a 2-colouring (no edge connects same-coloured vertices). BFS or DFS — try both.

- [ ] **8b — `bipartition`** — Status:

Return the two colour classes as a pair of lists, or `None` if not bipartite.

- [ ] **8c — `odd_cycle`** — Status:

If the graph is not bipartite, return one odd-length cycle as the witness. Otherwise return `None`.

- [ ] **8d — `k_colourable_check`** — Status:

Given `k`, decide if the graph admits a `k`-colouring. NP-hard in general — backtracking is the expected approach.

---

## Level 9 — Weighted shortest paths

Edge weights enter.

- [ ] **9a — `dijkstra_distances`** — Status:

Single-source shortest distances on a graph with non-negative edge weights. Use a min-heap.

- [ ] **9b — `dijkstra_path`** — Status:

As 9a, but reconstruct the actual path from `s` to `t`.

- [ ] **9c — `bellman_ford`** — Status:

Single-source shortest distances tolerating negative edges. Detect a reachable negative cycle and signal it.

- [ ] **9d — `shortest_path_at_most_k_edges`** — Status:

Shortest distance from `s` to `t` using at most `k` edges. The Bellman-Ford skeleton with a generation counter is the right shape.

---

## Level 10 — All-pairs shortest paths

A different paradigm: DP over intermediate vertices.

- [ ] **10a — `floyd_warshall`** — Status:

Return distance matrix `D` where `D[i][j]` is the shortest distance from `i` to `j`. Handles negative edges; assume no negative cycles.

- [ ] **10b — `floyd_warshall_paths`** — Status:

As 10a, with path reconstruction. Maintain a `next` (or predecessor) matrix during the DP.

- [ ] **10c — `transitive_closure`** — Status:

For an unweighted directed graph, return the boolean matrix `R` where `R[i][j]` is `True` iff `j` is reachable from `i`. The Floyd-Warshall skeleton with logical OR for `min`.

- [ ] **10d — `graph_diameter`** — Status:

The largest shortest-path distance between any pair of vertices. For unweighted graphs, BFS-from-each-vertex is also viable — compare.

---

## Level 11 — Spanning trees

Greedy growth.

- [ ] **11a — `prim_mst`** — Status:

Minimum spanning tree of a connected undirected weighted graph, via Prim's algorithm with a min-heap. Return the MST as a list of edges.

- [ ] **11b — `mst_total_weight`** — Status:

Just the total weight of the MST.

- [ ] **11c — `mst_unique`** — Status:

Return `True` iff the MST is unique. Subtle — think about edges of equal weight that could substitute for each other.

- [ ] **11d — `second_best_mst`** — Status:

The second-best MST: a spanning tree of minimum weight among those that are *not* the MST. Classical approach: find the MST, then for each non-MST edge consider swapping it in.

---

## Level 12 — DFS edge classification and lowlink

The structural insights of DFS — this is where things deepen.

- [ ] **12a — `classify_edges_directed`** — Status:

During DFS of a directed graph, classify every edge as one of `tree`, `back`, `forward`, `cross`. Return a dict from edge to label.

- [ ] **12b — `find_bridges`** — Status:

In an undirected graph, find every bridge: edges whose removal disconnects the graph. Tarjan's lowlink technique.

- [ ] **12c — `find_articulation_points`** — Status:

In an undirected graph, find every articulation point: vertices whose removal disconnects the graph. Same lowlink machinery, different condition.

- [ ] **12d — `biconnected_components`** — Status:

Decompose an undirected graph into biconnected components. Maintain a stack of edges during DFS and pop the right ones at each articulation point.

---

## Level 13 — Strong connectivity

Directed connectivity is genuinely harder than undirected.

- [ ] **13a — `scc_kosaraju`** — Status:

Find all strongly connected components using Kosaraju's algorithm: DFS on the original graph to get finish times, then DFS on the reversed graph in reverse finish order.

- [ ] **13b — `scc_tarjan`** — Status:

Same problem, single-pass, using lowlink and a stack of unfinished vertices.

- [ ] **13c — `condensation`** — Status:

Build the condensation: collapse each SCC into one super-vertex; super-edges are inherited from the original graph. The result is a DAG.

- [ ] **13d — `is_semiconnected`** — Status:

A directed graph is semiconnected iff for every pair `(u, v)`, at least one of `u → v` or `v → u` is reachable. Hint: think about the condensation.

---

## Level 14 — Eulerian paths

Walking every edge exactly once.

- [ ] **14a — `eulerian_circuit_exists`** — Status:

Return `True` iff the (connected) graph admits an Eulerian circuit. Handle both undirected and directed cases — the degree conditions differ.

- [ ] **14b — `eulerian_path_exists`** — Status:

Return `True` iff the graph admits an Eulerian path (not necessarily a circuit).

- [ ] **14c — `find_eulerian_circuit`** — Status:

Return one Eulerian circuit using Hierholzer's algorithm: walk until stuck, then splice in sub-tours from vertices with unused edges.

- [ ] **14d — `find_eulerian_path`** — Status:

Return one Eulerian path. The standard trick: add a virtual edge between the two odd-degree vertices to reduce to the circuit case, then remove it from the result.

---

## Level 15 — Flow

The hardest level. A new conceptual machinery: residual graphs and augmenting paths.

- [ ] **15a — `max_flow_edmonds_karp`** — Status:

Maximum flow from source `s` to sink `t`, using BFS to find augmenting paths in the residual graph. (This is Ford-Fulkerson with BFS — Edmonds-Karp.)

- [ ] **15b — `min_cut`** — Status:

Find a minimum `s`–`t` cut. After max flow, the cut is implicit in the residual graph: it's the set of vertices reachable from `s` in the residual.

- [ ] **15c — `bipartite_matching`** — Status:

Maximum matching in a bipartite graph, by reduction to max-flow. Add a super-source, a super-sink, unit capacities everywhere.

- [ ] **15d — `vertex_disjoint_paths`** — Status:

Maximum number of internally vertex-disjoint paths from `s` to `t`, by reduction to max-flow. The trick is node-splitting: replace each non-source/sink vertex `v` with two vertices `v_in` and `v_out` connected by a unit-capacity edge.
