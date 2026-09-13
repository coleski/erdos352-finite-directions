# Frozen main target: Erdős #352

Status checked freshly on 12 September 2026. This is a research target, not a solved result.

Does there exist an absolute finite C>0 such that every Lebesgue-measurable A⊂R² with |A|≥C contains three points p,q,r with |det(q−p,r−p)|/2=1?

The original source says |A|>C; existence of a threshold is equivalent to the ≥ formulation by increasing C. The target is unrestricted finite positive measure. Infinite/unbounded positive-measure results, convex cases, fixed numbers of components, growing bounds in a containing square, and method obstructions do not resolve it.

## Original and current status audit

- The original 1978 paper was freshly downloaded from https://users.renyi.hu/~p_erdos/1978-40.pdf . Printed page 122 (PDF page 10) was rendered and inspected. It explicitly asks for an absolute C and distinguishes the known infinite-measure result. Local copies: Er78d.pdf, Er78d.txt, Er78d-page122.png.
- All 17 comments of https://www.erdosproblems.com/forum/discuss/352 were read from the freshly fetched forum-live.html. No complete main-question claim appears. The lattice model, finite computations, low-area branch, and May 2026 density theorem are explicitly partial.
- Both fresh Epoch manifest ids lists exclude no #352.
- Fresh https://jig.so/api/problems?limit=500&offset=0 and https://jig.so/api/problems/6c0254ae-c611-4442-a5c6-9c56a674bf2f were fetched. The actual API number is 132. The main root and finite-unrestricted obligation are open, claims=[], no main proof artifact. Its other proofs concern degenerate/explicit coordinates and a three-anchor compatibility-graph obstruction. The latter is public prior work and is not reused as a new contribution here.
- The current https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/352.lean contains an open statement with sorry, not a proof.
- The current https://github.com/KitaKen1/erdos352-koizumi-fn-upper-bound gives f(N) for N≤7 only. Its graph is explicitly a relaxation. The witness repository https://github.com/KitaKen1/erdos352-koizumi-n-avoiding-witness-table supplies finite lower witnesses, not a growing-area counterexample.
- Bulj–Kovač, https://arxiv.org/abs/2605.30033 , current v1 submitted 28 May 2026, explicitly leaves the original question open. Its unrestricted bound depends on the containing square. The introduction and the complete lower-bound Section 3 were read. Its increasing-area construction avoids only upward-oriented axis-aligned hyperbolic corners, not all unit-area triangles. This distinction is essential.

## Selected route

Test whether the full one-direction horizontal-slice constraints alone can force a constant area bound. A concrete construction in ONE-DIRECTION-OBSTRUCTION.md shows that they cannot. Root's extension, independently audited with exact constants in FINITE-DIRECTION-OBSTRUCTION.md, proves the same obstruction for any fixed finite list of directions. This rules out that route; it is neither a counterexample to the frozen main statement nor a novelty claim.
