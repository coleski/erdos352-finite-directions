import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Topology.MetricSpace.ProperSpace.Real

namespace Statements.E352FiniteDirections

abbrev Point := ℝ × ℝ

def NonzeroDirection (d : Point) : Prop := d ≠ (0, 0)

def Parallel (p q d : Point) : Prop :=
  (q.1 - p.1) * d.2 = (q.2 - p.2) * d.1

noncomputable def TriangleArea (p q r : Point) : ℝ :=
  |(q.1 - p.1) * (r.2 - p.2) - (q.2 - p.2) * (r.1 - p.1)| / 2

def AvoidsPrescribedUnitTriangles (A : Set Point) (D : Finset Point) : Prop :=
  ∀ p ∈ A, ∀ q ∈ A, ∀ r ∈ A,
    TriangleArea p q r = 1 →
    ∀ d ∈ D, ¬ (Parallel p q d ∨ Parallel p r d ∨ Parallel q r d)

abbrev statement : Prop :=
  ∀ n : ℕ, 2 ≤ n → ∀ D : Finset Point,
    (∀ d ∈ D, NonzeroDirection d) →
    ∃ A : Set Point,
      IsOpen A ∧ Bornology.IsBounded A ∧
      MeasureTheory.volume A ≥ (n : ENNReal) / 16 ∧
      AvoidsPrescribedUnitTriangles A D

theorem target : statement := sorry

end Statements.E352FiniteDirections
