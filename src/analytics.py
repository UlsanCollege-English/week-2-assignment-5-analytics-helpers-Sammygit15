# src/analytics.py
from typing import List, Optional

def chunk(lst: List, size: int) -> List[List]:
    """Split lst into chunks of length size. Last chunk may be shorter.
       Raise ValueError if size <= 0.
    """
    if size <= 0:
        raise ValueError("chunk size must be > 0")
    return [lst[i:i+size] for i in range(0, len(lst), size)]


def running_total(start: int, deltas: List[int]) -> List[int]:
    """Return cumulative sums starting from start."""
    totals = []
    current = start
    for d in deltas:
        current += d
        totals.append(current)
    return totals


def index_of_first_at_least(lst: List[int], threshold: int) -> Optional[int]:
    """Return the index of the first element >= threshold, or None if not found."""
    for i, val in enumerate(lst):
        if val >= threshold:
            return i
    return None
