"""Controlled benchmark of the six sorting algorithms.

Run:  python benchmark_sorts.py
Outputs: results_raw.csv (every trial), results_summary.csv (medians),
         runtime_chart.png, and a printed results table.

Fairness controls
-----------------
* Datasets are generated ONCE per (size, condition) from a fixed seed, so every
  algorithm sorts exactly the same values.
* Each trial receives a fresh copy made BEFORE the timer starts; the sorts
  also copy internally, so the timed region is only the sort itself.
* time.perf_counter() is used, garbage collection is disabled while timing,
  and TRIALS = 3 trials per algorithm/condition; the MEDIAN is reported.
* Correctness is checked against a reference result outside the timed region.
* Quadratic algorithms are skipped for a size only if the projected runtime
  (previous size's median x 4) exceeds TIME_LIMIT_S; the skip is recorded.
"""

import csv
import gc
import random
import statistics
import time

from sorting_algorithms import ALGORITHMS, QUADRATIC, SortStats

SIZES = [1000, 2000, 4000, 8000]
CONDITIONS = ["random", "sorted", "reverse", "duplicates"]
TRIALS = 3
TIME_LIMIT_S = 8.0  # max projected seconds for ONE run of a quadratic sort
SEED = 2026


def make_data(size, condition):
    rng = random.Random(f"{SEED}-{size}-{condition}")
    if condition == "random":
        return [rng.randint(0, size * 10) for _ in range(size)]
    if condition == "sorted":
        return list(range(size))
    if condition == "reverse":
        return list(range(size, 0, -1))
    if condition == "duplicates":  # only ~10 distinct values
        return [rng.randint(0, 9) for _ in range(size)]
    raise ValueError(condition)


def run():
    raw, summary = [], []
    last_median = {}  # (algorithm, condition) -> median seconds at previous size
    for size in SIZES:
        for condition in CONDITIONS:
            source = make_data(size, condition)
            reference = sorted(source)  # outside timing, verification only
            for name, func in ALGORITHMS.items():
                key = (name, condition)
                projected = last_median.get(key, 0) * 4
                if name in QUADRATIC and projected > TIME_LIMIT_S:
                    reason = f"projected {projected:.1f}s > limit {TIME_LIMIT_S}s"
                    summary.append(dict(algorithm=name, condition=condition, size=size,
                                        median_s="", comparisons="", movements="",
                                        status=f"SKIPPED ({reason})"))
                    print(f"  skip {name:9s} {condition:10s} n={size}: {reason}")
                    continue
                times, stats_first = [], None
                for trial in range(1, TRIALS + 1):
                    fresh = list(source)  # fresh copy, made before timing
                    stats = SortStats()
                    gc.disable()
                    t0 = time.perf_counter()
                    result = func(fresh, stats)
                    elapsed = time.perf_counter() - t0
                    gc.enable()
                    assert result == reference, f"{name} incorrect ({condition}, n={size})"
                    times.append(elapsed)
                    if stats_first is None:
                        stats_first = stats
                    raw.append(dict(algorithm=name, condition=condition, size=size, trial=trial,
                                    seconds=f"{elapsed:.6f}", comparisons=stats.comparisons,
                                    movements=stats.movements))
                med = statistics.median(times)
                last_median[key] = med
                summary.append(dict(algorithm=name, condition=condition, size=size,
                                    median_s=f"{med:.6f}", comparisons=stats_first.comparisons,
                                    movements=stats_first.movements, status="OK"))
        print(f"finished n={size}", flush=True)
    return raw, summary


def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_chart(summary, path="runtime_chart.png"):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(12, 9), sharex=True)
    for ax, condition in zip(axes.flat, CONDITIONS):
        for name in ALGORITHMS:
            pts = [(r["size"], float(r["median_s"])) for r in summary
                   if r["algorithm"] == name and r["condition"] == condition and r["status"] == "OK"]
            if pts:
                ax.plot(*zip(*pts), marker="o", label=name)
        ax.set_title(f"{condition} data")
        ax.set_xscale("log", base=2)
        ax.set_yscale("log")
        ax.set_xlabel("input size n")
        ax.set_ylabel("median runtime (s)")
        ax.grid(True, which="both", alpha=0.3)
    axes[0][0].legend()
    fig.suptitle("Sorting runtime growth (median of 3 trials, log-log axes)")
    fig.tight_layout()
    fig.savefig(path, dpi=130)


def print_table(summary):
    print("\nMedian runtime in ms (comparisons / movements at largest run in parentheses omitted)")
    for condition in CONDITIONS:
        print(f"\n[{condition}]")
        print("algorithm  " + "".join(f"{n:>12}" for n in SIZES))
        for name in ALGORITHMS:
            cells = []
            for n in SIZES:
                r = next(x for x in summary if x["algorithm"] == name
                         and x["condition"] == condition and x["size"] == n)
                cells.append(f"{float(r['median_s'])*1000:12.2f}" if r["status"] == "OK" else f"{'skipped':>12}")
            print(f"{name:10s} " + "".join(cells))


if __name__ == "__main__":
    raw, summary = run()
    write_csv("results_raw.csv", raw)
    write_csv("results_summary.csv", summary)
    make_chart(summary)
    print_table(summary)
