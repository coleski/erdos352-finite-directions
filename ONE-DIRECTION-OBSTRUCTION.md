# Full horizontal-slice constraints do not give a uniform area bound

This is a rigorous obstruction to a proposed proof route for #352, not a counterexample to #352 and not a novelty claim.

## Proposition

For every integer n≥2 there is a bounded open set A_n⊂R², a finite union of rectangles, with area at least n/16 and containing no area-one triangle with a horizontal side. Rotating gives the same conclusion for any one prescribed direction. Both orientations and an arbitrary location of the third vertex are excluded; the third vertex is not required to align vertically with a base endpoint.

## Phase selection

Choose distinct primes p_1,...,p_n and put a_i=√p_i. For each fixed i, the numbers

    1, d_ij=2/(a_j−a_i), j≠i

are linearly independent over Q. Indeed, rationalization rewrites any relation as a rational linear combination of 1,√p_1,...,√p_n, and the coefficient of √p_j for j≠i is 2q_j/(p_j−p_i). These radicals and 1 are independent: in their multiquadratic field, subtract the automorphism changing the sign of a single radical, forcing its coefficient to vanish.

Consequently there is a positive integer k_i such that

    3/8 < {k_i d_ij} < 5/8  for every j≠i.                 (1)

This is the elementary Kronecker simultaneous approximation theorem. One short justification is Weyl's criterion: for every nonzero integer vector h, h·d_i is irrational, so the averages of exp(2πit h·d_i), t=1,...,T, tend to zero by the geometric-series formula. Trigonometric approximation then gives equidistribution in the torus, hence a visit to the positive-volume box (3/8,5/8)^(n−1).

Alternatively, to avoid any radical-field fact, choose a_1,...,a_n algebraically independent in (1,2). A rational relation among 1 and 2/(a_j−a_i) would be a zero rational function. Its pole in a_j forces the coefficient belonging to j to vanish. The same equidistribution argument applies.

## Exact construction

Let η=min_{i≠j}|a_i−a_j|>0 and K=max_i k_i. Choose

    0<ε≤min(η/4, η²/(128K), 1/128),  L=1/ε.

Set

    I_i=(a_i−ε/2,a_i+ε/2),
    B_i={x∈(0,L): dist(k_i x,Z)<1/16},
    A_n=union_i (B_i×I_i).

The I_i are disjoint, and each B_i is a finite union of open intervals. The periodic set defining B_i has density 1/8 and period 1/k_i. Thus

    |B_i|≥L/8−2/k_i≥L/16,

where the last inequality follows from L≥128 and k_i≥1. Therefore |A_n|=Σ_i ε|B_i|≥n/16.

## All horizontal-base triangles are excluded

Suppose (x,y),(x',y),(z,w) belong to A_n. Since the bands are disjoint, the two base points belong to a single B_i×I_i.

If w∈I_i too, then |x−x'|<L and |w−y|<ε. The triangle area is <Lε/2=1/2, hence is not 1.

Otherwise w∈I_j with j≠i. If its area were 1, then

    |x−x'|=2/|w−y|.                                    (2)

Since |(w−y)−(a_j−a_i)|<ε and ε≤η/2,

    |2/(w−y)−d_ij|≤4ε/η².

Multiplying by k_i makes this error at most 1/32 (and hence at most 1/16). By (1), the distance of k_i·2/(w−y) to Z is at least 5/16. Absolute values do not change distance to Z, so (2) implies

    dist(k_i(x−x'),Z)≥5/16.

But x,x'∈B_i imply dist(k_i(x−x'),Z)<1/8, a contradiction. This proves the proposition.

## Exact implication for the attempted measure mechanism

Write A_y={x:(x,y)∈A} and Y={y:A_y is nonempty}. Absence of a unit-area triangle with a horizontal base is EXACTLY the collection of conditions

    2/(z−y) ∉ A_y−A_y, for every y,z∈Y with y≠z.        (3)

The construction satisfies every condition in (3) while its area is unbounded with n. Thus there is no uniform integral bound on Σ/∫|A_y| deducible solely from the full slice/difference-set restrictions (3). A proof for the original problem must use information from other base directions; merely optimizing a single-direction Steinhaus/difference-set estimate cannot close the question.

This is stronger in configuration scope than the upward-right-corner restriction used in the lower construction of Bulj–Kovač, Section 3, https://arxiv.org/html/2605.30033 . It has no comparable effective growth rate in a square, and it is not a replacement or improvement of their theorem. That paper's rotational averaging explicitly uses information absent in (3).

## Bounded computational probe

phase_probe.py searches integer frequencies for the first eight primes and then certifies every phase inequality with exact rational intervals enclosing the square roots. It also certifies the common ε perturbation inequalities. Numerical search is only witness discovery; the final fixed-frequency checks use rational arithmetic. This does not verify or assert unrestricted avoidance.

## Status

The one-direction route is stalled for a decisive reason: its intended uniform-bound conclusion is false. No increasing-area family avoiding ALL unit-area triangles has been produced. No finite universal C for the original problem has been proved.
