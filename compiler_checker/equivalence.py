"""Comparison of observable results in the restricted terminating model."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Observation:
    status: str
    value: int | None = None

def equivalent(source: Observation, target: Observation) -> bool:
    return source == target
