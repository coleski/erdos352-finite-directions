# Finite prescribed directions cannot force unit-area triangles

This package records a proof-method obstruction for
[Erdős problem #352](https://www.erdosproblems.com/352). It does **not**
solve or refute the original problem, which permits triangle sides in every
direction.

Jig statement: https://jig.so/p/132?s=5

## Theorem

For every finite collection `D` of unoriented line directions and every
integer `n >= 2`, there is a bounded open set `A` in the plane, expressible as
a finite union of rectangles, such that

```text
area(A) >= n/16,
```

and no triangle with all three vertices in `A` has area one and a side
parallel to a direction in `D`.

Consequently, checking all slices and all base lengths in any one fixed finite
set of directions cannot establish a universal area threshold for the
original problem.

## Files

- `FINITE-DIRECTION-OBSTRUCTION.md`: complete proof and precise scope.
- `ONE-DIRECTION-OBSTRUCTION.md`: the precursor construction.
- `TARGET-352.md`: original question, current-status review, and prior work.
- `phase_probe.py`: an exact/numerical exploration aid; it is not used as a
  proof premise.

The proof combines algebraically independent band heights with simultaneous
Kronecker approximation, then uses thin periodic horizontal strips. The
finite-direction extension was separately audited for phase compatibility,
quantitative error margins, orientations, and same-band degeneracies.

## Status

This is AI-assisted research produced with Codex and independently reviewed
by a separate Codex agent. No claim of external peer review or exhaustive
worldwide novelty is made. The unrestricted Erdős #352 remains open.
