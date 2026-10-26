"""Correctness tests for all six algorithms.

Run:  python test_sorts.py
The independent reference check uses Python's built-in sorted(). It is used
ONLY here, to verify results - never inside the algorithm implementations.
"""

import random
import unittest

from sorting_algorithms import ALGORITHMS, SortStats


def make_datasets(seed=11):
    rng = random.Random(seed)
    return {
        "empty": [],
        "one_item": [42],
        "two_items_swapped": [2, 1],
        "all_equal": [7] * 50,
        "duplicates": [rng.randint(0, 5) for _ in range(200)],
        "already_sorted": list(range(100)),
        "reverse_sorted": list(range(100, 0, -1)),
        "random": [rng.randint(-1000, 1000) for _ in range(300)],
        "negatives_and_zero": [0, -5, 3, -5, 0, 9, -1],
    }


class SortingTests(unittest.TestCase):
    pass


def _make_test(name, func, label, data):
    def test(self):
        original = list(data)
        stats = SortStats()
        result = func(data, stats)
        self.assertEqual(result, sorted(original), f"{name} wrong on {label}")
        self.assertEqual(data, original, f"{name} modified its input on {label}")
        self.assertGreaterEqual(stats.comparisons, 0)
        self.assertGreaterEqual(stats.movements, 0)
    return test


for _name, _func in ALGORITHMS.items():
    for _label, _data in make_datasets().items():
        setattr(SortingTests, f"test_{_name}_{_label}", _make_test(_name, _func, _label, _data))


class StabilityNote(unittest.TestCase):
    def test_sorted_input_is_cheap_for_insertion_and_bubble(self):
        data = list(range(200))
        for name in ("Insertion", "Bubble"):
            stats = SortStats()
            ALGORITHMS[name](data, stats)
            self.assertEqual(stats.comparisons, 199, f"{name} should be O(n) on sorted input")


if __name__ == "__main__":
    unittest.main(verbosity=1)
