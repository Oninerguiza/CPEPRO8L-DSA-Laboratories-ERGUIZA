# Laboratory Submission Recheck

**Course:** CPEPRO8L — Data Structures and Algorithms Laboratory  
**Student:** Nino Eliezer Erguiza  
**Repository:** `Oninerguiza/CPEPRO8L-DSA-Laboratories-ERGUIZA`  
**Recheck date:** August 26, 2026  
**Status:** Provisional repository-based evaluation

## Recheck Summary

- Labs found: **1–6**
- Newly evaluated: **Labs 5 and 6**
- Missing from the current sequence: **Lab 7**
- All submitted Python files compile successfully.
- Both new implementations pass all functional and edge-case tests.
- None of the six corrections from the August 14 recheck were applied.

## Evaluation Criteria

| Criterion | Weight |
|---|---:|
| Program Correctness and Functionality | 40% |
| Code Quality and Organization | 20% |
| Analysis and Understanding | 20% |
| Documentation (`README.md`) | 10% |
| GitHub Repository Organization and Submission | 10% |
| **Total** | **100%** |

## Updated Results

| Laboratory | Correctness /40 | Code /20 | Analysis /20 | Documentation /10 | Repository /10 | Grade |
|---:|---:|---:|---:|---:|---:|---:|
| Lab 1 | 40 | 17 | 19 | 9 | 8 | **93/100** |
| Lab 2 | 40 | 18 | 19 | 8 | 9 | **94/100** |
| Lab 3 | 40 | 18 | 20 | 8 | 9 | **95/100** |
| Lab 4 | 40 | 18 | 19 | 7 | 9 | **93/100** |
| Lab 5 | 40 | 17 | 19 | 6 | 7 | **89/100** |
| Lab 6 | 40 | 18 | 19 | 6 | 7 | **90/100** |
| **Average of submitted labs** | **40.0** | **17.7** | **19.2** | **7.3** | **8.2** | **92.3/100** |

If Labs 1–7 are all required and every missing laboratory receives zero, the completion-adjusted grade is **79.1/100**. Apply this only according to the instructor's deadline and missing-submission policy.

## Verified Tests

- Labs 1–4: all previously passing tests remain passing.
- Lab 5: 27-point harness — LIFO ordering, `IndexError` on empty-stack pop, `peek` semantics, `is_empty` transitions, the required expressions (`{[()()]}`, `{[(])}`, `{[()]}`), and edge cases including empty strings, lone closers, `)(`, `(((`, mismatched nesting, deep nesting, and non-bracket characters. All five report expressions independently verified correct; the `{[()]}` stack trace replays exactly.
- Lab 6: FIFO ordering, full-capacity behavior, overflow rejection with unchanged state, underflow warning, freed-slot reuse across wraparound, slot clearing on dequeue, exact `display` format, and a 200-operation stress test matched against a reference queue. The report's 10-row state table matches actual execution row for row.

## Important Documentation Finding

- **Lab 5:** the report's "console capture" includes a block of five customized expression tests that the submitted source file never executes — the program prints only the two required lines. The five results shown are independently correct, but the capture was not produced by running the source.
- **Labs 5 and 6:** quoted error/warning messages do not match the source (`"pop from empty stack"` vs the actual `"Cannot pop from an empty stack."`; `"Cannot enqueue."` vs the actual `"Queue overflow: cannot enqueue."`), so parts of the captures cannot be reproduced as printed.
- **Labs 5 and 6:** reports are named `LAB REPORT 5.md` and `LAB REPORT 6.md`, while the specification requires `README.md`; both files' tables also list a `README.md` that does not exist in the folder.

## Corrections Required

1. Rename `LAB REPORT 5.md` and `LAB REPORT 6.md` to `README.md`, and fix the Files-table entries that reference a nonexistent README.
2. Make the Lab 5 five-expression capture real: either remove the block or extend the Lab 5 source driver to actually run and print those five tests.
3. Correct the quoted exception and warning messages in both reports to match the source strings.
4. Rename `task1_references.py.py` to `task1_references.py` — outstanding since August 14.
5. Make every README source-code reference match the submitted filenames (Lab 1–4 references are all stale) — outstanding since August 14.
6. Add or remove the broken Lab 2 `Screenshot.png` reference — outstanding since August 14.
7. Repair or remove the Lab 4 screenshot link, which now points to a file in the wrong folder — outstanding since August 14.
8. Add a root `README.md` with an overview and laboratory links — outstanding since August 14.
9. Submit Lab 7 when required.
10. Remove `LABCHECK.md` from the repository before final submission; it is an instructor document, not a deliverable.

## Instructor Note

Labs 5 and 6 are functionally the strongest evidence yet in this repository — the implementations passed every independent test, and the Lab 6 trace is accurate to the operation. The deductions concentrate entirely on documentation: misnamed reports, captures the source does not produce, and no progress on the six corrections identified on August 14. Scores may be adjusted for deadlines, late submissions, missing laboratories, or an oral/code defense.
