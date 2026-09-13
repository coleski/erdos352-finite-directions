# Finite prescribed directions cannot force a constant area threshold

Collaborative proof: the reserve probe established a one-direction phase construction; root supplied the finite-direction extension, and this audit checks phase compatibility, quantitative errors, and same-row degeneracies.

This is a proof-method obstruction, NOT a counterexample to Erdős #352. No novelty claim is made.

## Theorem

For every finite collection D of unoriented line directions and every integer n≥2, there is a bounded open set A⊂R², a finite union of rectangles, with |A|≥n/16, such that no triangle with vertices in A has area 1 and a side parallel to any direction in D.

In particular no fixed finite list of base directions, even with all slices and all base lengths in those directions, can give a universal area bound. The original main question allows every direction and remains unresolved.

## 1. Compatible simultaneous phases

Separate the horizontal direction, if present. For every remaining direction let σ_l be its cotangent: a vector in that direction has coordinates (σ_l t,t). Vertical directions have σ_l=0.

Take a Q-basis for the span of the finitely many σ_l and clear all denominators. Thus there are Q-linearly independent β_1,...,β_r and integers c_lt such that

    σ_l=Σ_t c_lt β_t.

If all cotangents vanish, take r=0. Define

    C=max(1,max_l Σ_t|c_lt|),    M=max(0,max_l|σ_l|).

The field K=Q(β_1,...,β_r) is countable. Choose a_i∈(i,i+1/4), for i=1,...,n, algebraically independent over K. Such a finite choice exists by successively avoiding the countable algebraic closure of the previously generated field.

The following real numbers are linearly independent over Q:

    1;   β_t a_i (all t,i);   2/(a_j−a_i) (all i<j).      (1)

Proof: any putative relation evaluates a rational function over K at the algebraically independent tuple (a_i). It must therefore be the zero rational function. The distinct simple pole a_j=a_i forces the coefficient of 2/(a_j−a_i) to vanish, separately for every unordered pair. The remaining polynomial is constant plus linear terms in the a_i. Each coefficient Σ_t q_it β_t is zero, so Q-linear independence of the β_t forces all q_it=0, and the constant is zero too.

By Kronecker's simultaneous approximation theorem applied to (1), choose a positive integer k such that

    dist(k β_t a_i,Z)<1/(32C)      for all t,i,
    dist(k·2/(a_j−a_i), Z+1/2)<1/16    for all i<j.        (2)

For completeness, this application follows from the geometric-series proof of Weyl's criterion: every nontrivial integer character of the vector of nonconstant entries of (1) has an irrational frequency, hence zero limiting average. Trigonometric approximation gives equidistribution and therefore a visit to the indicated open box.

The integer coefficient representation of σ_l is important: it gives, for every i,h,l,

    dist(k σ_l(a_h−a_i), Z)<1/16.                        (3)

Allowing merely rational coefficients without clearing denominators would not justify this inference. This was checked explicitly in the audit.

## 2. Thin bands with one common periodic horizontal set

Put η=min_{i<j}(a_j−a_i)>0 and H=max_i a_i−min_i a_i+1. Choose ε>0 so small that

    ε≤1/128,
    ε≤η/4,
    ε≤1/(4(MH+1)),
    k ε(M+4/η²)≤1/16.                                  (4)

Let L=1/ε and define

    B={x∈(0,L): dist(kx,Z)<1/16},
    I_i=(a_i−ε/2,a_i+ε/2),
    A=B×(union_i I_i).

The bands are disjoint. Since B has periodic density 1/8 and period 1/k,

    |B|≥L/8−2/k≥L/16,

using L≥128 and k≥1. Hence |A|=nε|B|≥n/16. It is bounded, open, and a finite union of rectangles. Also, for all x,x'∈B,

    dist(k(x−x'),Z)<1/8.                                (5)

## 3. A horizontal side

Its two endpoints must lie in one band i. If the third point is in the same band, the area is <Lε/2=1/2.

Otherwise its third height is w∈I_j, j≠i, while the base height is y∈I_i. An area-one triangle would require the absolute horizontal difference to equal 2/|w−y|. The signed reciprocal differs from 2/(a_j−a_i) by at most 4ε/η², since |(w−y)−(a_j−a_i)|<ε and ε≤η/2. By (2) and (4), its k-phase has distance at least 1/2−1/16−1/16=3/8 from Z. This contradicts (5). The sign of the reciprocal is harmless because 1/2≡−1/2 mod Z.

## 4. A nonhorizontal prescribed side

Write its endpoints as P=(x,y), Q=(x',y') and let its direction have cotangent σ. Then x'−x=σ(y'−y). Write the third vertex as R=(z,w).

If P,Q belong to the same band, then |y'−y|<ε, |w−y|<H and |z−x|<L. Therefore

    2 area(PQR)
      = |(y'−y)[σ(w−y)−(z−x)]|
      < ε(MH+L) ≤ 1+1/4 < 2.

This excludes area 1. It also covers a third point in any other band. If y'=y then x'=x and the triangle is degenerate, consistent with this inequality.

It remains that P is in band i and Q in a different band j. Let R be in band h; h is allowed to equal i or j. If the area is 1, the determinant identity gives one of the two exact equations

    z−x = σ(w−y) ± 2/(y'−y).                            (6)

The expression on the right differs from

    σ(a_h−a_i) ± 2/(a_j−a_i)

by at most Mε+4ε/η². Thus its k-phase is, by (2), (3), and (4), at distance at least

    1/2−1/16−1/16−1/16=5/16

from Z. Equation (6) contradicts (5). This handles every placement of the third vertex and both triangle orientations, completing the theorem.

## Scope and checks

- The finite set of directions must be fixed before the construction. Both the Kronecker frequency and ε depend on it and on n.
- This does not construct one unbounded positive-measure avoiding set; ε changes with n. It therefore does not conflict with the known unbounded positive-measure theorem.
- The construction can and generally will contain unit-area triangles in other directions. No claim of unrestricted avoidance is made.
- The proof does not say that a number of directions allowed to grow with the set, or directions chosen adaptively from the set, are useless. It rules out only a fixed finite directional test as sufficient for a universal threshold.
- The exact distinction from the upward-right-corner construction in Bulj–Kovač, https://arxiv.org/html/2605.30033 , is that arbitrary third vertices and both signs are handled here, but there is no comparable effective bound in a containing square. No literature-priority claim is warranted from this bounded audit.

The original #352 main question remains open. This route is stalled because its proposed finite-direction conclusion is false, not because an estimate was merely too weak.
