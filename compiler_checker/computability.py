"""Computability-theory notes for the project."""
GENERAL_RESULT = (
    "For sufficiently expressive programs, universal semantic equivalence is undecidable. "
    "Finite testing over a finite input set and restricted terminating language is decidable, "
    "but cannot establish equivalence for all programs and inputs."
)

def finite_test_scope(input_count: int, step_bound: int) -> bool:
    return input_count >= 0 and step_bound >= 0
